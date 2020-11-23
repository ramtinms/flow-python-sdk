# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flow/entities/account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='flow/entities/account.proto',
  package='flow.entities',
  syntax='proto3',
  serialized_options=b'Z\010entities',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x66low/entities/account.proto\x12\rflow.entities\"\xce\x01\n\x07\x41\x63\x63ount\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0f\n\x07\x62\x61lance\x18\x02 \x01(\x04\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x0c\x12\'\n\x04keys\x18\x04 \x03(\x0b\x32\x19.flow.entities.AccountKey\x12\x38\n\tcontracts\x18\x05 \x03(\x0b\x32%.flow.entities.Account.ContractsEntry\x1a\x30\n\x0e\x43ontractsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\x8f\x01\n\nAccountKey\x12\r\n\x05index\x18\x01 \x01(\r\x12\x12\n\npublic_key\x18\x02 \x01(\x0c\x12\x11\n\tsign_algo\x18\x03 \x01(\r\x12\x11\n\thash_algo\x18\x04 \x01(\r\x12\x0e\n\x06weight\x18\x05 \x01(\r\x12\x17\n\x0fsequence_number\x18\x06 \x01(\r\x12\x0f\n\x07revoked\x18\x07 \x01(\x08\x42\nZ\x08\x65ntitiesb\x06proto3'
)




_ACCOUNT_CONTRACTSENTRY = _descriptor.Descriptor(
  name='ContractsEntry',
  full_name='flow.entities.Account.ContractsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='flow.entities.Account.ContractsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='flow.entities.Account.ContractsEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=253,
)

_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='flow.entities.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='flow.entities.Account.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='balance', full_name='flow.entities.Account.balance', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='flow.entities.Account.code', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keys', full_name='flow.entities.Account.keys', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contracts', full_name='flow.entities.Account.contracts', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ACCOUNT_CONTRACTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=253,
)


_ACCOUNTKEY = _descriptor.Descriptor(
  name='AccountKey',
  full_name='flow.entities.AccountKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='flow.entities.AccountKey.index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='flow.entities.AccountKey.public_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sign_algo', full_name='flow.entities.AccountKey.sign_algo', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash_algo', full_name='flow.entities.AccountKey.hash_algo', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weight', full_name='flow.entities.AccountKey.weight', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='flow.entities.AccountKey.sequence_number', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revoked', full_name='flow.entities.AccountKey.revoked', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=256,
  serialized_end=399,
)

_ACCOUNT_CONTRACTSENTRY.containing_type = _ACCOUNT
_ACCOUNT.fields_by_name['keys'].message_type = _ACCOUNTKEY
_ACCOUNT.fields_by_name['contracts'].message_type = _ACCOUNT_CONTRACTSENTRY
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['AccountKey'] = _ACCOUNTKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {

  'ContractsEntry' : _reflection.GeneratedProtocolMessageType('ContractsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ACCOUNT_CONTRACTSENTRY,
    '__module__' : 'flow.entities.account_pb2'
    # @@protoc_insertion_point(class_scope:flow.entities.Account.ContractsEntry)
    })
  ,
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'flow.entities.account_pb2'
  # @@protoc_insertion_point(class_scope:flow.entities.Account)
  })
_sym_db.RegisterMessage(Account)
_sym_db.RegisterMessage(Account.ContractsEntry)

AccountKey = _reflection.GeneratedProtocolMessageType('AccountKey', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTKEY,
  '__module__' : 'flow.entities.account_pb2'
  # @@protoc_insertion_point(class_scope:flow.entities.AccountKey)
  })
_sym_db.RegisterMessage(AccountKey)


DESCRIPTOR._options = None
_ACCOUNT_CONTRACTSENTRY._options = None
# @@protoc_insertion_point(module_scope)