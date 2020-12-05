# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='status.proto',
  package='dfa.rpc',
  syntax='proto3',
  serialized_options=b'\n\007dfa.rpcP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cstatus.proto\x12\x07\x64\x66\x61.rpc\x1a\x19google/protobuf/any.proto\"]\n\x06Status\x12\x1b\n\x04\x63ode\x18\x01 \x01(\x0e\x32\r.dfa.rpc.Code\x12\x0f\n\x07message\x18\x02 \x01(\t\x12%\n\x07\x64\x65tails\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Any*\xc0\x04\n\x04\x43ode\x12\x06\n\x02OK\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\x0c\n\x08\x41\x43\x43\x45PTED\x10\x02\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x03\x12\x10\n\x0cUNAUTHORIZED\x10\x04\x12\x14\n\x10PAYMENT_REQUIRED\x10\x05\x12\r\n\tFORBIDDEN\x10\x06\x12\r\n\tNOT_FOUND\x10\x07\x12\x16\n\x12METHOD_NOT_ALLOWED\x10\x08\x12\x12\n\x0eNOT_ACCEPTABLE\x10\t\x12\x17\n\x13PROXY_AUTH_REQUIRED\x10\n\x12\x13\n\x0fREQUEST_TIMEOUT\x10\x0b\x12\x0c\n\x08\x43ONFLICT\x10\x0c\x12\x08\n\x04GONE\x10\r\x12\x13\n\x0fLENGTH_REQUIRED\x10\x0e\x12\x17\n\x13PRECONDITION_FAILED\x10\x0f\x12\x15\n\x11PAYLOAD_TOO_LARGE\x10\x10\x12\x10\n\x0cURI_TOO_LONG\x10\x11\x12\x19\n\x15UNSUPPORTED_MIME_TYPE\x10\x12\x12\x19\n\x15RANGE_NOT_SATISFIABLE\x10\x13\x12\x16\n\x12\x45XPECTATION_FAILED\x10\x14\x12\x14\n\x10UPGRADE_REQUIRED\x10\x15\x12\x19\n\x15INTERNAL_SERVER_ERROR\x10\x16\x12\x13\n\x0fNOT_IMPLEMENTED\x10\x17\x12\x0f\n\x0b\x42\x41\x44_GATEWAY\x10\x18\x12\x17\n\x13SERVICE_UNAVAILABLE\x10\x19\x12\x13\n\x0fGATEWAY_TIMEOUT\x10\x1a\x12\"\n\x1ePROTOCOL_VERSION_NOT_SUPPORTED\x10\x1b\x42\x0b\n\x07\x64\x66\x61.rpcP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])

_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='dfa.rpc.Code',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCEPTED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BAD_REQUEST', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNAUTHORIZED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_REQUIRED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FORBIDDEN', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METHOD_NOT_ALLOWED', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_ACCEPTABLE', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROXY_AUTH_REQUIRED', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_TIMEOUT', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONFLICT', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GONE', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LENGTH_REQUIRED', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRECONDITION_FAILED', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAYLOAD_TOO_LARGE', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='URI_TOO_LONG', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_MIME_TYPE', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RANGE_NOT_SATISFIABLE', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPECTATION_FAILED', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPGRADE_REQUIRED', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_SERVER_ERROR', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_IMPLEMENTED', index=23, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BAD_GATEWAY', index=24, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_UNAVAILABLE', index=25, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GATEWAY_TIMEOUT', index=26, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROTOCOL_VERSION_NOT_SUPPORTED', index=27, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=148,
  serialized_end=724,
)
_sym_db.RegisterEnumDescriptor(_CODE)

Code = enum_type_wrapper.EnumTypeWrapper(_CODE)
OK = 0
CREATED = 1
ACCEPTED = 2
BAD_REQUEST = 3
UNAUTHORIZED = 4
PAYMENT_REQUIRED = 5
FORBIDDEN = 6
NOT_FOUND = 7
METHOD_NOT_ALLOWED = 8
NOT_ACCEPTABLE = 9
PROXY_AUTH_REQUIRED = 10
REQUEST_TIMEOUT = 11
CONFLICT = 12
GONE = 13
LENGTH_REQUIRED = 14
PRECONDITION_FAILED = 15
PAYLOAD_TOO_LARGE = 16
URI_TOO_LONG = 17
UNSUPPORTED_MIME_TYPE = 18
RANGE_NOT_SATISFIABLE = 19
EXPECTATION_FAILED = 20
UPGRADE_REQUIRED = 21
INTERNAL_SERVER_ERROR = 22
NOT_IMPLEMENTED = 23
BAD_GATEWAY = 24
SERVICE_UNAVAILABLE = 25
GATEWAY_TIMEOUT = 26
PROTOCOL_VERSION_NOT_SUPPORTED = 27



_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='dfa.rpc.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dfa.rpc.Status.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='dfa.rpc.Status.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='details', full_name='dfa.rpc.Status.details', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=52,
  serialized_end=145,
)

_STATUS.fields_by_name['code'].enum_type = _CODE
_STATUS.fields_by_name['details'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.enum_types_by_name['Code'] = _CODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'status_pb2'
  # @@protoc_insertion_point(class_scope:dfa.rpc.Status)
  })
_sym_db.RegisterMessage(Status)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
