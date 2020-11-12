import threading
import logging
from typing import List, Optional, TYPE_CHECKING

import zmq

from .messages import MessageBase, InvokeSyscall, SyscallReturn, RetrieveMemory, RetrieveMemoryReturn, SyncMemory, \
    RetrieveMemoryReturnResult, TargetStrlen, TargetStrlenResponse
from .actions import BaseAction, SyscallReturnAction, WriteMemoryAction

if TYPE_CHECKING:
    from angr import SimState
    from angr.calling_conventions import SimCCSyscall


_l = logging.getLogger(name=__name__)


class Session:
    def __init__(self, socket):
        self.socket = socket
        self.event = threading.Event()


class Bureau:
    def __init__(self, project):
        self.project = project
        self.states: List[Optional['SimState']] = [None] * 10  # TODO: Implement sessions so we support multiple agents

        # zeromq
        self.zmq_context = zmq.Context()
        self.zmq_sessions: List[Session] = [ ]
        self.zmq_port: Optional[int] = None

        self.serve_thread: Optional[threading.Thread] = None

    def start(self):
        socket = self.zmq_context.socket(zmq.REP)
        port = 5555
        while port < 65536:
            try:
                socket.bind("tcp://*:%d" % port)
                _l.debug("ZMQ socket binds to port %d." % port)
                break
            except zmq.error.ZMQError:
                # port in use. try the next port
                port += 1
                if port == 65536:
                    # over max port
                    raise RuntimeError("Run out of usable TCP port.")

        self.zmq_port = port
        self.zmq_sessions.append(Session(socket))

        # handler thread
        self.serve_thread = threading.Thread(target=self.serve, daemon=True)
        self.serve_thread.start()

    def serve(self):
        tmp = self.zmq_sessions[0].socket.recv()
        assert tmp  # non-empty
        self.zmq_sessions[0].event.set()

    def invoke_syscall(self, state: 'SimState', num: int, args: List, syscall_cc: 'SimCCSyscall') -> List[BaseAction]:
        self.states[0] = state

        msg = InvokeSyscall(num, args)
        _l.debug("Sending %r.", msg)

        actions: List[BaseAction] = [ ]

        # wait until the socket is ready
        _l.debug("invoke_syscall(): Waiting for the socket to become ready.")
        self.zmq_sessions[0].event.wait()
        _l.debug("invoke_syscall(): Socket is ready.")
        self.zmq_sessions[0].socket.send(msg.serialize())

        # expect a SyscallReturn or a RetrieveMemory
        while True:
            msg = self.zmq_sessions[0].socket.recv()
            ret = MessageBase.unserialize(msg)
            _l.debug("Got a message: %r", ret)

            if isinstance(ret, SyscallReturn):
                # syscall execution completes
                actions.append(SyscallReturnAction(ret.retval))
                break
            elif isinstance(ret, RetrieveMemory):
                # the agent is asking for memory data
                state = self.states[0]
                data = state.memory.load(ret.addr, ret.size)
                if state.solver.symbolic(data):
                    _l.debug("Data is symbolic. Cannot retrieve memory. Abort.")
                    r = RetrieveMemoryReturn(RetrieveMemoryReturnResult.ABORT, None)
                else:
                    _l.debug("Send concrete data back to the syscall agent.")
                    r = RetrieveMemoryReturn(RetrieveMemoryReturnResult.OK, state.solver.eval(data, cast_to=bytes))
                self.zmq_sessions[0].socket.send(r.serialize())
            elif isinstance(ret, SyncMemory):
                # the agent is sending us back some memory data
                actions.append(WriteMemoryAction(ret.addr, ret.data))
                self.zmq_sessions[0].socket.send(b"\x61")  # just send something back...
            elif isinstance(ret, TargetStrlen):
                # the agent needs to know the length of a string in memory
                state = self.states[0]
                strlen, _, match_indices = state.memory.find(ret.addr, b'\0', 4096, max_symbolic_bytes=1)  # I think 0 will break things
                if strlen.symbolic:
                    maxidx = max(match_indices) + 1
                else:
                    maxidx = max(match_indices)
                r = TargetStrlenResponse(maxidx)
                self.zmq_sessions[0].socket.send(r.serialize())


        assert isinstance(ret, SyscallReturn)

        self.states[0] = None

        return actions
