# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/function.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import primitives_pb2 as protos_dot_primitives__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/function.proto',
  package='angr.protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x15protos/function.proto\x12\x0b\x61ngr.protos\x1a\x17protos/primitives.proto\"\xaf\x02\n\x08\x46unction\x12\n\n\x02\x65\x61\x18\x01 \x01(\x04\x12\x15\n\ris_entrypoint\x18\x03 \x01(\x08\x12\"\n\x06\x62locks\x18\x02 \x03(\x0b\x32\x12.angr.protos.Block\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06is_plt\x18\x07 \x01(\x08\x12\x12\n\nis_syscall\x18\x08 \x01(\x08\x12\x17\n\x0fis_simprocedure\x18\t \x01(\x08\x12\x11\n\treturning\x18\n \x01(\x08\x12\x13\n\x0b\x62inary_name\x18\x0b \x01(\t\x12&\n\x05graph\x18\x0c \x01(\x0b\x32\x17.angr.protos.BlockGraph\x12\x1a\n\x12\x65xternal_functions\x18\r \x03(\x04\x12\x11\n\talignment\x18\x0e \x01(\x08\x12\x12\n\nnormalized\x18\x0f \x01(\x08\x62\x06proto3'
  ,
  dependencies=[protos_dot_primitives__pb2.DESCRIPTOR,])




_FUNCTION = _descriptor.Descriptor(
  name='Function',
  full_name='angr.protos.Function',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ea', full_name='angr.protos.Function.ea', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_entrypoint', full_name='angr.protos.Function.is_entrypoint', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blocks', full_name='angr.protos.Function.blocks', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='angr.protos.Function.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_plt', full_name='angr.protos.Function.is_plt', index=4,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_syscall', full_name='angr.protos.Function.is_syscall', index=5,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_simprocedure', full_name='angr.protos.Function.is_simprocedure', index=6,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='returning', full_name='angr.protos.Function.returning', index=7,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binary_name', full_name='angr.protos.Function.binary_name', index=8,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graph', full_name='angr.protos.Function.graph', index=9,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_functions', full_name='angr.protos.Function.external_functions', index=10,
      number=13, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alignment', full_name='angr.protos.Function.alignment', index=11,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normalized', full_name='angr.protos.Function.normalized', index=12,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=367,
)

_FUNCTION.fields_by_name['blocks'].message_type = protos_dot_primitives__pb2._BLOCK
_FUNCTION.fields_by_name['graph'].message_type = protos_dot_primitives__pb2._BLOCKGRAPH
DESCRIPTOR.message_types_by_name['Function'] = _FUNCTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Function = _reflection.GeneratedProtocolMessageType('Function', (_message.Message,), {
  'DESCRIPTOR' : _FUNCTION,
  '__module__' : 'protos.function_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.Function)
  })
_sym_db.RegisterMessage(Function)


# @@protoc_insertion_point(module_scope)
