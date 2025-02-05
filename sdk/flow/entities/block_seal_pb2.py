# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flow/entities/block_seal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='flow/entities/block_seal.proto',
  package='flow.entities',
  syntax='proto3',
  serialized_options=b'Z\010entities',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x66low/entities/block_seal.proto\x12\rflow.entities\"\x85\x01\n\tBlockSeal\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x0c\x12\x1c\n\x14\x65xecution_receipt_id\x18\x02 \x01(\x0c\x12$\n\x1c\x65xecution_receipt_signatures\x18\x03 \x03(\x0c\x12\"\n\x1aresult_approval_signatures\x18\x04 \x03(\x0c\x42\nZ\x08\x65ntitiesb\x06proto3'
)




_BLOCKSEAL = _descriptor.Descriptor(
  name='BlockSeal',
  full_name='flow.entities.BlockSeal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_id', full_name='flow.entities.BlockSeal.block_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='execution_receipt_id', full_name='flow.entities.BlockSeal.execution_receipt_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='execution_receipt_signatures', full_name='flow.entities.BlockSeal.execution_receipt_signatures', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_approval_signatures', full_name='flow.entities.BlockSeal.result_approval_signatures', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=50,
  serialized_end=183,
)

DESCRIPTOR.message_types_by_name['BlockSeal'] = _BLOCKSEAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockSeal = _reflection.GeneratedProtocolMessageType('BlockSeal', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKSEAL,
  '__module__' : 'flow.entities.block_seal_pb2'
  # @@protoc_insertion_point(class_scope:flow.entities.BlockSeal)
  })
_sym_db.RegisterMessage(BlockSeal)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
