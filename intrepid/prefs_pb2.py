# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prefs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import intrepid.jobs_pb2 as jobs__pb2
import intrepid.ssh_access_profile_pb2 as ssh__access__profile__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='prefs.proto',
  package='protocols',
  syntax='proto2',
  serialized_options=b'\n\035com.geomodeller.protocols.appB\013Preferences',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bprefs.proto\x12\tprotocols\x1a\njobs.proto\x1a\x18ssh_access_profile.proto\"\xba\x01\n\tUserScope\x12\x1d\n\x04misc\x18\x01 \x01(\x0b\x32\x0f.protocols.Misc\x12%\n\x08\x61utosave\x18\x02 \x01(\x0b\x32\x13.protocols.AutoSave\x12\'\n\tworkspace\x18\x03 \x01(\x0b\x32\x14.protocols.Workspace\x12>\n\x15\x64istributed_computing\x18\x04 \x01(\x0b\x32\x1f.protocols.DistributedComputing\"\xa8\x01\n\x04Misc\x12$\n\x15research_menu_visible\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\"\n\x13shutdown_gracefully\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x15\n\rlook_and_feel\x18\x03 \x01(\t\x12#\n\x14\x65nable_BRGM_features\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0c\x65nable_pulse\x18\x05 \x01(\x08:\x04true\"\x8b\x01\n\x08\x41utoSave\x12\x16\n\x07\x65nabled\x18\x01 \x01(\x08:\x05\x66\x61lse\x12+\n\x1fnumber_of_autosaves_per_project\x18\x02 \x01(\x05:\x02\x31\x30\x12 \n\x10minimum_interval\x18\x03 \x01(\x03:\x06\x33\x30\x30\x30\x30\x30\x12\x18\n\nduty_cycle\x18\x04 \x01(\x02:\x04\x30.05\"\xd7\x01\n\tWorkspace\x12\x1a\n\x12latest_project_uri\x18\x01 \x01(\t\x12\x1c\n\x14latest_workspace_uri\x18\x02 \x01(\t\x12#\n\x1blatest_filechooser_location\x18\x03 \x01(\t\x12\x1d\n\x15latest_project_closed\x18\x04 \x01(\x08\x12-\n\x0e\x63urrent_action\x18\x05 \x01(\x0e\x32\x15.protocols.ActionEnum\x12\x1d\n\x15\x63urrent_action_object\x18\x06 \x01(\t\"w\n\x14\x44istributedComputing\x12@\n\x1b\x64\x65\x66\x61ult_ssh_access_profiles\x18\x01 \x03(\x0b\x32\x1b.protocols.SSHAccessProfile\x12\x1d\n\x04jobs\x18\x02 \x01(\x0b\x32\x0f.protocols.Jobs\"d\n\x04Jobs\x12/\n\x0einversion_jobs\x18\x01 \x03(\x0b\x32\x17.protocols.InversionJob\x12+\n\x0c\x66orward_jobs\x18\x02 \x03(\x0b\x32\x15.protocols.ForwardJob*6\n\nActionEnum\x12\x08\n\x04NOOP\x10\x00\x12\x08\n\x04LOAD\x10\x01\x12\x08\n\x04SAVE\x10\x02\x12\n\n\x06\x45XPORT\x10\x03\x42,\n\x1d\x63om.geomodeller.protocols.appB\x0bPreferences'
  ,
  dependencies=[jobs__pb2.DESCRIPTOR,ssh__access__profile__pb2.DESCRIPTOR,])

_ACTIONENUM = _descriptor.EnumDescriptor(
  name='ActionEnum',
  full_name='protocols.ActionEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOOP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOAD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SAVE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPORT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1007,
  serialized_end=1061,
)
_sym_db.RegisterEnumDescriptor(_ACTIONENUM)

ActionEnum = enum_type_wrapper.EnumTypeWrapper(_ACTIONENUM)
NOOP = 0
LOAD = 1
SAVE = 2
EXPORT = 3



_USERSCOPE = _descriptor.Descriptor(
  name='UserScope',
  full_name='protocols.UserScope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='misc', full_name='protocols.UserScope.misc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autosave', full_name='protocols.UserScope.autosave', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workspace', full_name='protocols.UserScope.workspace', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distributed_computing', full_name='protocols.UserScope.distributed_computing', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=65,
  serialized_end=251,
)


_MISC = _descriptor.Descriptor(
  name='Misc',
  full_name='protocols.Misc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='research_menu_visible', full_name='protocols.Misc.research_menu_visible', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shutdown_gracefully', full_name='protocols.Misc.shutdown_gracefully', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='look_and_feel', full_name='protocols.Misc.look_and_feel', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_BRGM_features', full_name='protocols.Misc.enable_BRGM_features', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_pulse', full_name='protocols.Misc.enable_pulse', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  serialized_start=254,
  serialized_end=422,
)


_AUTOSAVE = _descriptor.Descriptor(
  name='AutoSave',
  full_name='protocols.AutoSave',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='protocols.AutoSave.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number_of_autosaves_per_project', full_name='protocols.AutoSave.number_of_autosaves_per_project', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minimum_interval', full_name='protocols.AutoSave.minimum_interval', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=300000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duty_cycle', full_name='protocols.AutoSave.duty_cycle', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.05),
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
  serialized_start=425,
  serialized_end=564,
)


_WORKSPACE = _descriptor.Descriptor(
  name='Workspace',
  full_name='protocols.Workspace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='latest_project_uri', full_name='protocols.Workspace.latest_project_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latest_workspace_uri', full_name='protocols.Workspace.latest_workspace_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latest_filechooser_location', full_name='protocols.Workspace.latest_filechooser_location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latest_project_closed', full_name='protocols.Workspace.latest_project_closed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_action', full_name='protocols.Workspace.current_action', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_action_object', full_name='protocols.Workspace.current_action_object', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=567,
  serialized_end=782,
)


_DISTRIBUTEDCOMPUTING = _descriptor.Descriptor(
  name='DistributedComputing',
  full_name='protocols.DistributedComputing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='default_ssh_access_profiles', full_name='protocols.DistributedComputing.default_ssh_access_profiles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jobs', full_name='protocols.DistributedComputing.jobs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=784,
  serialized_end=903,
)


_JOBS = _descriptor.Descriptor(
  name='Jobs',
  full_name='protocols.Jobs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inversion_jobs', full_name='protocols.Jobs.inversion_jobs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='forward_jobs', full_name='protocols.Jobs.forward_jobs', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=905,
  serialized_end=1005,
)

_USERSCOPE.fields_by_name['misc'].message_type = _MISC
_USERSCOPE.fields_by_name['autosave'].message_type = _AUTOSAVE
_USERSCOPE.fields_by_name['workspace'].message_type = _WORKSPACE
_USERSCOPE.fields_by_name['distributed_computing'].message_type = _DISTRIBUTEDCOMPUTING
_WORKSPACE.fields_by_name['current_action'].enum_type = _ACTIONENUM
_DISTRIBUTEDCOMPUTING.fields_by_name['default_ssh_access_profiles'].message_type = ssh__access__profile__pb2._SSHACCESSPROFILE
_DISTRIBUTEDCOMPUTING.fields_by_name['jobs'].message_type = _JOBS
_JOBS.fields_by_name['inversion_jobs'].message_type = jobs__pb2._INVERSIONJOB
_JOBS.fields_by_name['forward_jobs'].message_type = jobs__pb2._FORWARDJOB
DESCRIPTOR.message_types_by_name['UserScope'] = _USERSCOPE
DESCRIPTOR.message_types_by_name['Misc'] = _MISC
DESCRIPTOR.message_types_by_name['AutoSave'] = _AUTOSAVE
DESCRIPTOR.message_types_by_name['Workspace'] = _WORKSPACE
DESCRIPTOR.message_types_by_name['DistributedComputing'] = _DISTRIBUTEDCOMPUTING
DESCRIPTOR.message_types_by_name['Jobs'] = _JOBS
DESCRIPTOR.enum_types_by_name['ActionEnum'] = _ACTIONENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserScope = _reflection.GeneratedProtocolMessageType('UserScope', (_message.Message,), {
  'DESCRIPTOR' : _USERSCOPE,
  '__module__' : 'prefs_pb2'
  # @@protoc_insertion_point(class_scope:protocols.UserScope)
  })
_sym_db.RegisterMessage(UserScope)

Misc = _reflection.GeneratedProtocolMessageType('Misc', (_message.Message,), {
  'DESCRIPTOR' : _MISC,
  '__module__' : 'prefs_pb2'
  # @@protoc_insertion_point(class_scope:protocols.Misc)
  })
_sym_db.RegisterMessage(Misc)

AutoSave = _reflection.GeneratedProtocolMessageType('AutoSave', (_message.Message,), {
  'DESCRIPTOR' : _AUTOSAVE,
  '__module__' : 'prefs_pb2'
  # @@protoc_insertion_point(class_scope:protocols.AutoSave)
  })
_sym_db.RegisterMessage(AutoSave)

Workspace = _reflection.GeneratedProtocolMessageType('Workspace', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACE,
  '__module__' : 'prefs_pb2'
  # @@protoc_insertion_point(class_scope:protocols.Workspace)
  })
_sym_db.RegisterMessage(Workspace)

DistributedComputing = _reflection.GeneratedProtocolMessageType('DistributedComputing', (_message.Message,), {
  'DESCRIPTOR' : _DISTRIBUTEDCOMPUTING,
  '__module__' : 'prefs_pb2'
  # @@protoc_insertion_point(class_scope:protocols.DistributedComputing)
  })
_sym_db.RegisterMessage(DistributedComputing)

Jobs = _reflection.GeneratedProtocolMessageType('Jobs', (_message.Message,), {
  'DESCRIPTOR' : _JOBS,
  '__module__' : 'prefs_pb2'
  # @@protoc_insertion_point(class_scope:protocols.Jobs)
  })
_sym_db.RegisterMessage(Jobs)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
