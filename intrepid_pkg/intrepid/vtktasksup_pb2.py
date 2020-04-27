# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vtktasksup.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='vtktasksup.proto',
  package='vtktasksup',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10vtktasksup.proto\x12\nvtktasksup\"\xed\x03\n\x11QuadricDecimation\x12\x1d\n\x10target_reduction\x18\x01 \x01(\x01:\x03\x30.9\x12)\n\x1ause_attribute_error_metric\x18\x02 \x01(\x08:\x05\x66\x61lse\x12&\n\x17use_volume_preservation\x18\x03 \x01(\x08:\x05\x66\x61lse\x12#\n\x15use_scalars_attribute\x18\x04 \x01(\x08:\x04true\x12#\n\x15use_vectors_attribute\x18\x05 \x01(\x08:\x04true\x12#\n\x15use_normals_attribute\x18\x06 \x01(\x08:\x04true\x12#\n\x15use_tcoords_attribute\x18\x07 \x01(\x08:\x04true\x12#\n\x15use_tensors_attribute\x18\x08 \x01(\x08:\x04true\x12\x19\n\x0escalars_weight\x18\t \x01(\x01:\x01\x31\x12\x19\n\x0evectors_weight\x18\n \x01(\x01:\x01\x30\x12\x19\n\x0enormals_weight\x18\x0b \x01(\x01:\x01\x30\x12\x19\n\x0etcoords_weight\x18\x0c \x01(\x01:\x01\x30\x12\x19\n\x0etensors_weight\x18\r \x01(\x01:\x01\x30\x12&\n\x18use_boundary_constraints\x18\x0e \x01(\x08:\x04true\"\xea\x02\n\x0b\x44\x65\x63imatePro\x12\x1d\n\x10target_reduction\x18\x01 \x01(\x01:\x03\x30.9\x12\x19\n\rfeature_angle\x18\x02 \x01(\x01:\x02\x36\x30\x12\x1f\n\x11preserve_topology\x18\x03 \x01(\x08:\x04true\x12\x18\n\tsplitting\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x18\n\x0bsplit_angle\x18\x05 \x01(\x01:\x03\x31\x32\x30\x12\x1d\n\x0epre_split_mesh\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x11\n\tmax_error\x18\x07 \x01(\x01\x12\x1e\n\x10\x61\x63\x63umulate_error\x18\x08 \x01(\x08:\x04true\x12!\n\x12use_absolute_error\x18\t \x01(\x08:\x05\x66\x61lse\x12\'\n\x18\x62oundary_vertex_deletion\x18\n \x01(\x08:\x05\x66\x61lse\x12\x0e\n\x06\x64\x65gree\x18\x0b \x01(\x05\x12\x1e\n\x16inflection_point_ratio\x18\x0c \x01(\x01\"\xdc\x01\n\rCleanPolyData\x12$\n\x15tolerance_is_absolute\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x14\n\ttolerance\x18\x02 \x01(\x01:\x01\x30\x12%\n\x17\x63onvert_lines_to_points\x18\x03 \x01(\x08:\x04true\x12$\n\x16\x63onvert_polys_to_lines\x18\x04 \x01(\x08:\x04true\x12%\n\x17\x63onvert_strips_to_polys\x18\x05 \x01(\x08:\x04true\x12\x1b\n\rpoint_merging\x18\x06 \x01(\x08:\x04true')
)




_QUADRICDECIMATION = _descriptor.Descriptor(
  name='QuadricDecimation',
  full_name='vtktasksup.QuadricDecimation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_reduction', full_name='vtktasksup.QuadricDecimation.target_reduction', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.9),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_attribute_error_metric', full_name='vtktasksup.QuadricDecimation.use_attribute_error_metric', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_volume_preservation', full_name='vtktasksup.QuadricDecimation.use_volume_preservation', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_scalars_attribute', full_name='vtktasksup.QuadricDecimation.use_scalars_attribute', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_vectors_attribute', full_name='vtktasksup.QuadricDecimation.use_vectors_attribute', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_normals_attribute', full_name='vtktasksup.QuadricDecimation.use_normals_attribute', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_tcoords_attribute', full_name='vtktasksup.QuadricDecimation.use_tcoords_attribute', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_tensors_attribute', full_name='vtktasksup.QuadricDecimation.use_tensors_attribute', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scalars_weight', full_name='vtktasksup.QuadricDecimation.scalars_weight', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vectors_weight', full_name='vtktasksup.QuadricDecimation.vectors_weight', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normals_weight', full_name='vtktasksup.QuadricDecimation.normals_weight', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcoords_weight', full_name='vtktasksup.QuadricDecimation.tcoords_weight', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensors_weight', full_name='vtktasksup.QuadricDecimation.tensors_weight', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_boundary_constraints', full_name='vtktasksup.QuadricDecimation.use_boundary_constraints', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  serialized_start=33,
  serialized_end=526,
)


_DECIMATEPRO = _descriptor.Descriptor(
  name='DecimatePro',
  full_name='vtktasksup.DecimatePro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_reduction', full_name='vtktasksup.DecimatePro.target_reduction', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.9),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_angle', full_name='vtktasksup.DecimatePro.feature_angle', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(60),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preserve_topology', full_name='vtktasksup.DecimatePro.preserve_topology', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='splitting', full_name='vtktasksup.DecimatePro.splitting', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='split_angle', full_name='vtktasksup.DecimatePro.split_angle', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(120),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pre_split_mesh', full_name='vtktasksup.DecimatePro.pre_split_mesh', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_error', full_name='vtktasksup.DecimatePro.max_error', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accumulate_error', full_name='vtktasksup.DecimatePro.accumulate_error', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_absolute_error', full_name='vtktasksup.DecimatePro.use_absolute_error', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boundary_vertex_deletion', full_name='vtktasksup.DecimatePro.boundary_vertex_deletion', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='degree', full_name='vtktasksup.DecimatePro.degree', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inflection_point_ratio', full_name='vtktasksup.DecimatePro.inflection_point_ratio', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=529,
  serialized_end=891,
)


_CLEANPOLYDATA = _descriptor.Descriptor(
  name='CleanPolyData',
  full_name='vtktasksup.CleanPolyData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tolerance_is_absolute', full_name='vtktasksup.CleanPolyData.tolerance_is_absolute', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tolerance', full_name='vtktasksup.CleanPolyData.tolerance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='convert_lines_to_points', full_name='vtktasksup.CleanPolyData.convert_lines_to_points', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='convert_polys_to_lines', full_name='vtktasksup.CleanPolyData.convert_polys_to_lines', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='convert_strips_to_polys', full_name='vtktasksup.CleanPolyData.convert_strips_to_polys', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point_merging', full_name='vtktasksup.CleanPolyData.point_merging', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  serialized_start=894,
  serialized_end=1114,
)

DESCRIPTOR.message_types_by_name['QuadricDecimation'] = _QUADRICDECIMATION
DESCRIPTOR.message_types_by_name['DecimatePro'] = _DECIMATEPRO
DESCRIPTOR.message_types_by_name['CleanPolyData'] = _CLEANPOLYDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuadricDecimation = _reflection.GeneratedProtocolMessageType('QuadricDecimation', (_message.Message,), {
  'DESCRIPTOR' : _QUADRICDECIMATION,
  '__module__' : 'vtktasksup_pb2'
  # @@protoc_insertion_point(class_scope:vtktasksup.QuadricDecimation)
  })
_sym_db.RegisterMessage(QuadricDecimation)

DecimatePro = _reflection.GeneratedProtocolMessageType('DecimatePro', (_message.Message,), {
  'DESCRIPTOR' : _DECIMATEPRO,
  '__module__' : 'vtktasksup_pb2'
  # @@protoc_insertion_point(class_scope:vtktasksup.DecimatePro)
  })
_sym_db.RegisterMessage(DecimatePro)

CleanPolyData = _reflection.GeneratedProtocolMessageType('CleanPolyData', (_message.Message,), {
  'DESCRIPTOR' : _CLEANPOLYDATA,
  '__module__' : 'vtktasksup_pb2'
  # @@protoc_insertion_point(class_scope:vtktasksup.CleanPolyData)
  })
_sym_db.RegisterMessage(CleanPolyData)


# @@protoc_insertion_point(module_scope)
