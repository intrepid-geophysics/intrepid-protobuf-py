# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jobs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='jobs.proto',
  package='protocols',
  syntax='proto2',
  serialized_options=_b('\n!com.geomodeller.protocols.dc.jobs'),
  serialized_pb=_b('\n\njobs.proto\x12\tprotocols\"k\n\nForwardJob\x12\x0e\n\x06job_id\x18\x01 \x02(\x05\x12\x13\n\x0bproject_url\x18\x02 \x02(\t\x12\x1d\n\x15status_descriptor_url\x18\x03 \x02(\t\x12\x0c\n\x04\x63\x61se\x18\x04 \x02(\t\x12\x0b\n\x03run\x18\x05 \x02(\t\"m\n\x0cInversionJob\x12\x0e\n\x06job_id\x18\x01 \x02(\x05\x12\x13\n\x0bproject_url\x18\x02 \x02(\t\x12\x1d\n\x15status_descriptor_url\x18\x03 \x02(\t\x12\x0c\n\x04\x63\x61se\x18\x04 \x02(\t\x12\x0b\n\x03run\x18\x05 \x02(\tB#\n!com.geomodeller.protocols.dc.jobs')
)




_FORWARDJOB = _descriptor.Descriptor(
  name='ForwardJob',
  full_name='protocols.ForwardJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='protocols.ForwardJob.job_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project_url', full_name='protocols.ForwardJob.project_url', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_descriptor_url', full_name='protocols.ForwardJob.status_descriptor_url', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='case', full_name='protocols.ForwardJob.case', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run', full_name='protocols.ForwardJob.run', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=132,
)


_INVERSIONJOB = _descriptor.Descriptor(
  name='InversionJob',
  full_name='protocols.InversionJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='protocols.InversionJob.job_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project_url', full_name='protocols.InversionJob.project_url', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_descriptor_url', full_name='protocols.InversionJob.status_descriptor_url', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='case', full_name='protocols.InversionJob.case', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run', full_name='protocols.InversionJob.run', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=243,
)

DESCRIPTOR.message_types_by_name['ForwardJob'] = _FORWARDJOB
DESCRIPTOR.message_types_by_name['InversionJob'] = _INVERSIONJOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ForwardJob = _reflection.GeneratedProtocolMessageType('ForwardJob', (_message.Message,), {
  'DESCRIPTOR' : _FORWARDJOB,
  '__module__' : 'jobs_pb2'
  # @@protoc_insertion_point(class_scope:protocols.ForwardJob)
  })
_sym_db.RegisterMessage(ForwardJob)

InversionJob = _reflection.GeneratedProtocolMessageType('InversionJob', (_message.Message,), {
  'DESCRIPTOR' : _INVERSIONJOB,
  '__module__' : 'jobs_pb2'
  # @@protoc_insertion_point(class_scope:protocols.InversionJob)
  })
_sym_db.RegisterMessage(InversionJob)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)