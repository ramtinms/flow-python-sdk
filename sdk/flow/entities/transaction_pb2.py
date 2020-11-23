# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flow/entities/transaction.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='flow/entities/transaction.proto',
  package='flow.entities',
  syntax='proto3',
  serialized_options=b'Z\010entities',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x66low/entities/transaction.proto\x12\rflow.entities\"\xd0\x03\n\x0bTransaction\x12\x0e\n\x06script\x18\x01 \x01(\x0c\x12\x11\n\targuments\x18\x02 \x03(\x0c\x12\x1a\n\x12reference_block_id\x18\x03 \x01(\x0c\x12\x11\n\tgas_limit\x18\x04 \x01(\x04\x12<\n\x0cproposal_key\x18\x05 \x01(\x0b\x32&.flow.entities.Transaction.ProposalKey\x12\r\n\x05payer\x18\x06 \x01(\x0c\x12\x13\n\x0b\x61uthorizers\x18\x07 \x03(\x0c\x12@\n\x12payload_signatures\x18\x08 \x03(\x0b\x32$.flow.entities.Transaction.Signature\x12\x41\n\x13\x65nvelope_signatures\x18\t \x03(\x0b\x32$.flow.entities.Transaction.Signature\x1aG\n\x0bProposalKey\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0e\n\x06key_id\x18\x02 \x01(\r\x12\x17\n\x0fsequence_number\x18\x03 \x01(\x04\x1a?\n\tSignature\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0e\n\x06key_id\x18\x02 \x01(\r\x12\x11\n\tsignature\x18\x03 \x01(\x0c*c\n\x11TransactionStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\r\n\tFINALIZED\x10\x02\x12\x0c\n\x08\x45XECUTED\x10\x03\x12\n\n\x06SEALED\x10\x04\x12\x0b\n\x07\x45XPIRED\x10\x05\x42\nZ\x08\x65ntitiesb\x06proto3'
)

_TRANSACTIONSTATUS = _descriptor.EnumDescriptor(
  name='TransactionStatus',
  full_name='flow.entities.TransactionStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINALIZED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXECUTED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEALED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=517,
  serialized_end=616,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONSTATUS)

TransactionStatus = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONSTATUS)
UNKNOWN = 0
PENDING = 1
FINALIZED = 2
EXECUTED = 3
SEALED = 4
EXPIRED = 5



_TRANSACTION_PROPOSALKEY = _descriptor.Descriptor(
  name='ProposalKey',
  full_name='flow.entities.Transaction.ProposalKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='flow.entities.Transaction.ProposalKey.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_id', full_name='flow.entities.Transaction.ProposalKey.key_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='flow.entities.Transaction.ProposalKey.sequence_number', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=379,
  serialized_end=450,
)

_TRANSACTION_SIGNATURE = _descriptor.Descriptor(
  name='Signature',
  full_name='flow.entities.Transaction.Signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='flow.entities.Transaction.Signature.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_id', full_name='flow.entities.Transaction.Signature.key_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='flow.entities.Transaction.Signature.signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=452,
  serialized_end=515,
)

_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='flow.entities.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='script', full_name='flow.entities.Transaction.script', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='flow.entities.Transaction.arguments', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reference_block_id', full_name='flow.entities.Transaction.reference_block_id', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas_limit', full_name='flow.entities.Transaction.gas_limit', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proposal_key', full_name='flow.entities.Transaction.proposal_key', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payer', full_name='flow.entities.Transaction.payer', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authorizers', full_name='flow.entities.Transaction.authorizers', index=6,
      number=7, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload_signatures', full_name='flow.entities.Transaction.payload_signatures', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='envelope_signatures', full_name='flow.entities.Transaction.envelope_signatures', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TRANSACTION_PROPOSALKEY, _TRANSACTION_SIGNATURE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=515,
)

_TRANSACTION_PROPOSALKEY.containing_type = _TRANSACTION
_TRANSACTION_SIGNATURE.containing_type = _TRANSACTION
_TRANSACTION.fields_by_name['proposal_key'].message_type = _TRANSACTION_PROPOSALKEY
_TRANSACTION.fields_by_name['payload_signatures'].message_type = _TRANSACTION_SIGNATURE
_TRANSACTION.fields_by_name['envelope_signatures'].message_type = _TRANSACTION_SIGNATURE
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.enum_types_by_name['TransactionStatus'] = _TRANSACTIONSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {

  'ProposalKey' : _reflection.GeneratedProtocolMessageType('ProposalKey', (_message.Message,), {
    'DESCRIPTOR' : _TRANSACTION_PROPOSALKEY,
    '__module__' : 'flow.entities.transaction_pb2'
    # @@protoc_insertion_point(class_scope:flow.entities.Transaction.ProposalKey)
    })
  ,

  'Signature' : _reflection.GeneratedProtocolMessageType('Signature', (_message.Message,), {
    'DESCRIPTOR' : _TRANSACTION_SIGNATURE,
    '__module__' : 'flow.entities.transaction_pb2'
    # @@protoc_insertion_point(class_scope:flow.entities.Transaction.Signature)
    })
  ,
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'flow.entities.transaction_pb2'
  # @@protoc_insertion_point(class_scope:flow.entities.Transaction)
  })
_sym_db.RegisterMessage(Transaction)
_sym_db.RegisterMessage(Transaction.ProposalKey)
_sym_db.RegisterMessage(Transaction.Signature)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
