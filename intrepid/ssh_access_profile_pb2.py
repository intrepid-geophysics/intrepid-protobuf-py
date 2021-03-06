# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssh_access_profile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ssh_access_profile.proto',
  package='protocols',
  syntax='proto2',
  serialized_options=b'\n\034com.geomodeller.protocols.dc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18ssh_access_profile.proto\x12\tprotocols\"\xf8\x01\n\x10SSHAccessProfile\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05login\x18\x02 \x02(\t\x12n\n\x07scripts\x18\x03 \x01(\t:]#!/bin/tcsh\nsource .login\nsource /short/v90/_intrepiddev\nManageLithoInversion -batch $JOBFILE\x12 \n\nremote_zip\x18\x04 \x01(\t:\x0c/usr/bin/zip\x12$\n\x0cremote_unzip\x18\x05 \x01(\t:\x0e/usr/bin/unzip\x12\x0f\n\x05\x65mail\x18\x06 \x01(\t:\x00\x42\x1e\n\x1c\x63om.geomodeller.protocols.dc'
)




_SSHACCESSPROFILE = _descriptor.Descriptor(
  name='SSHAccessProfile',
  full_name='protocols.SSHAccessProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protocols.SSHAccessProfile.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='login', full_name='protocols.SSHAccessProfile.login', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scripts', full_name='protocols.SSHAccessProfile.scripts', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"#!/bin/tcsh\nsource .login\nsource /short/v90/_intrepiddev\nManageLithoInversion -batch $JOBFILE".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remote_zip', full_name='protocols.SSHAccessProfile.remote_zip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"/usr/bin/zip".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remote_unzip', full_name='protocols.SSHAccessProfile.remote_unzip', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"/usr/bin/unzip".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='protocols.SSHAccessProfile.email', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"".decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=288,
)

DESCRIPTOR.message_types_by_name['SSHAccessProfile'] = _SSHACCESSPROFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SSHAccessProfile = _reflection.GeneratedProtocolMessageType('SSHAccessProfile', (_message.Message,), {
  'DESCRIPTOR' : _SSHACCESSPROFILE,
  '__module__' : 'ssh_access_profile_pb2'
  # @@protoc_insertion_point(class_scope:protocols.SSHAccessProfile)
  })
_sym_db.RegisterMessage(SSHAccessProfile)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
