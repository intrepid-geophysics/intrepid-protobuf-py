# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshgrid_model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import commontaskmodel_pb2 as commontaskmodel__pb2
import data_description_format_pb2 as data__description__format__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='meshgrid_model.proto',
  package='meshgrid_model',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x14meshgrid_model.proto\x12\x0emeshgrid_model\x1a\x15\x63ommontaskmodel.proto\x1a\x1d\x64\x61ta_description_format.proto\"\xd1\x01\n\x10\x46ieldRenderState\x12\x14\n\x0csection_name\x18\x01 \x01(\t\x12\x0c\n\x04in3d\x18\x02 \x01(\x08\x12@\n\x08iso_mode\x18\x03 \x01(\x0e\x32..meshgrid_model.FieldRenderState.IsoRenderMode\x12\x1b\n\x13projection_distance\x18\x04 \x01(\x01\":\n\rIsoRenderMode\x12\x0b\n\x07ISONONE\x10\x00\x12\x0c\n\x08ISOCURVE\x10\x01\x12\x0e\n\nISOSURFACE\x10\x02\"H\n\rLithologyDesc\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04rank\x18\x02 \x01(\x05\x12\x1b\n\x06\x63olour\x18\x03 \x01(\x0b\x32\x0b.ctm.Colour\"\x89\x01\n\x07NoValue\x12\x13\n\x0b\x64ouble_null\x18\x01 \x01(\x01\x12\x12\n\nint32_null\x18\x02 \x01(\x05\x12\x12\n\nint64_null\x18\x03 \x01(\x03\x12\x12\n\nfloat_null\x18\x04 \x01(\x02\x12\x18\n\x0clogical_null\x18\x05 \x01(\x05:\x02-1\x12\x13\n\x0bstring_null\x18\x06 \x01(\t\"\xf2\x03\n\rMeshGridField\x12&\n\nfield_desc\x18\x01 \x01(\x0b\x32\x12.ddf.FieldInfo_DDF\x12\x38\n\x08\x63\x65lltype\x18\x02 \x01(\x0e\x32&.meshgrid_model.MeshGridField.CellType\x12\x13\n\x0b\x64\x65scription\x18\x03 \x03(\t\x12\x19\n\x0b\x66ield_alias\x18\x04 \x01(\t:\x04none\x12\x36\n\x0crender_state\x18\x05 \x03(\x0b\x32 .meshgrid_model.FieldRenderState\x12\x30\n\tlithology\x18\x08 \x03(\x0b\x32\x1d.meshgrid_model.LithologyDesc\x12\x16\n\x0evariogram_file\x18\x0c \x01(\t\x12\x32\n\x0fgeophysics_type\x18\r \x01(\x0e\x32\x19.ctm.GeophysicsSignalType\x12\x10\n\x08resource\x18\x0e \x01(\t\x12\x17\n\x0b\x66ield_index\x18\x0f \x01(\x05:\x02-1\x12)\n\x08no_value\x18\x10 \x01(\x0b\x32\x17.meshgrid_model.NoValue\"C\n\x08\x43\x65llType\x12\t\n\x05VOXET\x10\x00\x12\x08\n\x04QUAD\x10\x01\x12\x0c\n\x08TRIANGLE\x10\x02\x12\t\n\x05POINT\x10\x03\x12\t\n\x05TETRA\x10\x04\"0\n\x0fRunLengthDouble\x12\x0e\n\x06length\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01\"\x8c\x02\n\x08GridDesc\x12\n\n\x02nx\x18\x01 \x01(\x05\x12\n\n\x02ny\x18\x02 \x01(\x05\x12\n\n\x02nz\x18\x03 \x01(\x05\x12\x18\n\x02\x64x\x18\x04 \x01(\x0b\x32\x0c.ctm.Point3d\x12\x18\n\x02\x64y\x18\x05 \x01(\x0b\x32\x0c.ctm.Point3d\x12\x18\n\x02\x64z\x18\x06 \x01(\x0b\x32\x0c.ctm.Point3d\x12.\n\x05sizex\x18\n \x03(\x0b\x32\x1f.meshgrid_model.RunLengthDouble\x12.\n\x05sizey\x18\x0b \x03(\x0b\x32\x1f.meshgrid_model.RunLengthDouble\x12.\n\x05sizez\x18\x0c \x03(\x0b\x32\x1f.meshgrid_model.RunLengthDouble\"\xfd\x03\n\x08MeshGrid\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.meshgrid_model.MeshGrid.MeshGridType\x12,\n\x05\x66ield\x18\x02 \x03(\x0b\x32\x1d.meshgrid_model.MeshGridField\x12+\n\tgrid_desc\x18\x03 \x01(\x0b\x32\x18.meshgrid_model.GridDesc\x12\x1c\n\x06origin\x18\x04 \x01(\x0b\x32\x0c.ctm.Point3d\x12\x0c\n\x04name\x18\x05 \x01(\t\x12(\n\x0b\x64\x65scription\x18\x06 \x01(\x0b\x32\x13.ctm.RepeatedString\x12\x11\n\tdimension\x18\x07 \x01(\x05\x12+\n\x0c\x63oord_system\x18\x08 \x01(\x0b\x32\x15.ctm.CoordinateSystem\x12\x38\n\x10\x63oord_ref_system\x18\t \x01(\x0e\x32\x1e.ctm.CoordinateReferenceSystem\x12\x16\n\x07use_ijk\x18\n \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07use_xyz\x18\x0b \x01(\x08:\x05\x66\x61lse\x12!\n\x13predefined_meshgrid\x18\x0c \x01(\x08:\x04true\">\n\x0cMeshGridType\x12\x0b\n\x07REGULAR\x10\x00\x12\x0f\n\x0bSEMIREGULAR\x10\x01\x12\x10\n\x0cUNSTRUCTURED\x10\x02\"l\n\x0f\x43olumnAliasList\x12\x0f\n\x07x_alias\x18\x01 \x03(\t\x12\x0f\n\x07y_alias\x18\x02 \x03(\t\x12\x0f\n\x07z_alias\x18\x03 \x03(\t\x12\x12\n\ntime_alias\x18\x04 \x03(\t\x12\x12\n\ndate_alias\x18\x05 \x03(\t\"\xb5\x01\n\x10MeshGridFileDesc\x12:\n\x11\x63olumn_alias_list\x18\x01 \x01(\x0b\x32\x1f.meshgrid_model.ColumnAliasList\x12+\n\tmesh_grid\x18\x02 \x01(\x0b\x32\x18.meshgrid_model.MeshGrid\x12\x1c\n\x11\x63omment_character\x18\x03 \x01(\t:\x01#\x12\x1a\n\rfile_no_value\x18\x04 \x01(\t:\x03NaN')
  ,
  dependencies=[commontaskmodel__pb2.DESCRIPTOR,data__description__format__pb2.DESCRIPTOR,])



_FIELDRENDERSTATE_ISORENDERMODE = _descriptor.EnumDescriptor(
  name='IsoRenderMode',
  full_name='meshgrid_model.FieldRenderState.IsoRenderMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ISONONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISOCURVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISOSURFACE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=246,
  serialized_end=304,
)
_sym_db.RegisterEnumDescriptor(_FIELDRENDERSTATE_ISORENDERMODE)

_MESHGRIDFIELD_CELLTYPE = _descriptor.EnumDescriptor(
  name='CellType',
  full_name='meshgrid_model.MeshGridField.CellType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VOXET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUAD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRIANGLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POINT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TETRA', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=952,
  serialized_end=1019,
)
_sym_db.RegisterEnumDescriptor(_MESHGRIDFIELD_CELLTYPE)

_MESHGRID_MESHGRIDTYPE = _descriptor.EnumDescriptor(
  name='MeshGridType',
  full_name='meshgrid_model.MeshGrid.MeshGridType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REGULAR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEMIREGULAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSTRUCTURED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1790,
  serialized_end=1852,
)
_sym_db.RegisterEnumDescriptor(_MESHGRID_MESHGRIDTYPE)


_FIELDRENDERSTATE = _descriptor.Descriptor(
  name='FieldRenderState',
  full_name='meshgrid_model.FieldRenderState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='section_name', full_name='meshgrid_model.FieldRenderState.section_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in3d', full_name='meshgrid_model.FieldRenderState.in3d', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iso_mode', full_name='meshgrid_model.FieldRenderState.iso_mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='projection_distance', full_name='meshgrid_model.FieldRenderState.projection_distance', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FIELDRENDERSTATE_ISORENDERMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=304,
)


_LITHOLOGYDESC = _descriptor.Descriptor(
  name='LithologyDesc',
  full_name='meshgrid_model.LithologyDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='meshgrid_model.LithologyDesc.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank', full_name='meshgrid_model.LithologyDesc.rank', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='colour', full_name='meshgrid_model.LithologyDesc.colour', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=306,
  serialized_end=378,
)


_NOVALUE = _descriptor.Descriptor(
  name='NoValue',
  full_name='meshgrid_model.NoValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='double_null', full_name='meshgrid_model.NoValue.double_null', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int32_null', full_name='meshgrid_model.NoValue.int32_null', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_null', full_name='meshgrid_model.NoValue.int64_null', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_null', full_name='meshgrid_model.NoValue.float_null', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logical_null', full_name='meshgrid_model.NoValue.logical_null', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_null', full_name='meshgrid_model.NoValue.string_null', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=381,
  serialized_end=518,
)


_MESHGRIDFIELD = _descriptor.Descriptor(
  name='MeshGridField',
  full_name='meshgrid_model.MeshGridField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_desc', full_name='meshgrid_model.MeshGridField.field_desc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='celltype', full_name='meshgrid_model.MeshGridField.celltype', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='meshgrid_model.MeshGridField.description', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_alias', full_name='meshgrid_model.MeshGridField.field_alias', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("none").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='render_state', full_name='meshgrid_model.MeshGridField.render_state', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lithology', full_name='meshgrid_model.MeshGridField.lithology', index=5,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variogram_file', full_name='meshgrid_model.MeshGridField.variogram_file', index=6,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='geophysics_type', full_name='meshgrid_model.MeshGridField.geophysics_type', index=7,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource', full_name='meshgrid_model.MeshGridField.resource', index=8,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_index', full_name='meshgrid_model.MeshGridField.field_index', index=9,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_value', full_name='meshgrid_model.MeshGridField.no_value', index=10,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESHGRIDFIELD_CELLTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=521,
  serialized_end=1019,
)


_RUNLENGTHDOUBLE = _descriptor.Descriptor(
  name='RunLengthDouble',
  full_name='meshgrid_model.RunLengthDouble',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='length', full_name='meshgrid_model.RunLengthDouble.length', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='meshgrid_model.RunLengthDouble.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=1021,
  serialized_end=1069,
)


_GRIDDESC = _descriptor.Descriptor(
  name='GridDesc',
  full_name='meshgrid_model.GridDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nx', full_name='meshgrid_model.GridDesc.nx', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ny', full_name='meshgrid_model.GridDesc.ny', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nz', full_name='meshgrid_model.GridDesc.nz', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dx', full_name='meshgrid_model.GridDesc.dx', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dy', full_name='meshgrid_model.GridDesc.dy', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dz', full_name='meshgrid_model.GridDesc.dz', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sizex', full_name='meshgrid_model.GridDesc.sizex', index=6,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sizey', full_name='meshgrid_model.GridDesc.sizey', index=7,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sizez', full_name='meshgrid_model.GridDesc.sizez', index=8,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1072,
  serialized_end=1340,
)


_MESHGRID = _descriptor.Descriptor(
  name='MeshGrid',
  full_name='meshgrid_model.MeshGrid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='meshgrid_model.MeshGrid.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field', full_name='meshgrid_model.MeshGrid.field', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grid_desc', full_name='meshgrid_model.MeshGrid.grid_desc', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin', full_name='meshgrid_model.MeshGrid.origin', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='meshgrid_model.MeshGrid.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='meshgrid_model.MeshGrid.description', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimension', full_name='meshgrid_model.MeshGrid.dimension', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coord_system', full_name='meshgrid_model.MeshGrid.coord_system', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coord_ref_system', full_name='meshgrid_model.MeshGrid.coord_ref_system', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_ijk', full_name='meshgrid_model.MeshGrid.use_ijk', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_xyz', full_name='meshgrid_model.MeshGrid.use_xyz', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='predefined_meshgrid', full_name='meshgrid_model.MeshGrid.predefined_meshgrid', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESHGRID_MESHGRIDTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1343,
  serialized_end=1852,
)


_COLUMNALIASLIST = _descriptor.Descriptor(
  name='ColumnAliasList',
  full_name='meshgrid_model.ColumnAliasList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_alias', full_name='meshgrid_model.ColumnAliasList.x_alias', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y_alias', full_name='meshgrid_model.ColumnAliasList.y_alias', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z_alias', full_name='meshgrid_model.ColumnAliasList.z_alias', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_alias', full_name='meshgrid_model.ColumnAliasList.time_alias', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_alias', full_name='meshgrid_model.ColumnAliasList.date_alias', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1854,
  serialized_end=1962,
)


_MESHGRIDFILEDESC = _descriptor.Descriptor(
  name='MeshGridFileDesc',
  full_name='meshgrid_model.MeshGridFileDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='column_alias_list', full_name='meshgrid_model.MeshGridFileDesc.column_alias_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mesh_grid', full_name='meshgrid_model.MeshGridFileDesc.mesh_grid', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment_character', full_name='meshgrid_model.MeshGridFileDesc.comment_character', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("#").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_no_value', full_name='meshgrid_model.MeshGridFileDesc.file_no_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("NaN").decode('utf-8'),
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
  serialized_start=1965,
  serialized_end=2146,
)

_FIELDRENDERSTATE.fields_by_name['iso_mode'].enum_type = _FIELDRENDERSTATE_ISORENDERMODE
_FIELDRENDERSTATE_ISORENDERMODE.containing_type = _FIELDRENDERSTATE
_LITHOLOGYDESC.fields_by_name['colour'].message_type = commontaskmodel__pb2._COLOUR
_MESHGRIDFIELD.fields_by_name['field_desc'].message_type = data__description__format__pb2._FIELDINFO_DDF
_MESHGRIDFIELD.fields_by_name['celltype'].enum_type = _MESHGRIDFIELD_CELLTYPE
_MESHGRIDFIELD.fields_by_name['render_state'].message_type = _FIELDRENDERSTATE
_MESHGRIDFIELD.fields_by_name['lithology'].message_type = _LITHOLOGYDESC
_MESHGRIDFIELD.fields_by_name['geophysics_type'].enum_type = commontaskmodel__pb2._GEOPHYSICSSIGNALTYPE
_MESHGRIDFIELD.fields_by_name['no_value'].message_type = _NOVALUE
_MESHGRIDFIELD_CELLTYPE.containing_type = _MESHGRIDFIELD
_GRIDDESC.fields_by_name['dx'].message_type = commontaskmodel__pb2._POINT3D
_GRIDDESC.fields_by_name['dy'].message_type = commontaskmodel__pb2._POINT3D
_GRIDDESC.fields_by_name['dz'].message_type = commontaskmodel__pb2._POINT3D
_GRIDDESC.fields_by_name['sizex'].message_type = _RUNLENGTHDOUBLE
_GRIDDESC.fields_by_name['sizey'].message_type = _RUNLENGTHDOUBLE
_GRIDDESC.fields_by_name['sizez'].message_type = _RUNLENGTHDOUBLE
_MESHGRID.fields_by_name['type'].enum_type = _MESHGRID_MESHGRIDTYPE
_MESHGRID.fields_by_name['field'].message_type = _MESHGRIDFIELD
_MESHGRID.fields_by_name['grid_desc'].message_type = _GRIDDESC
_MESHGRID.fields_by_name['origin'].message_type = commontaskmodel__pb2._POINT3D
_MESHGRID.fields_by_name['description'].message_type = commontaskmodel__pb2._REPEATEDSTRING
_MESHGRID.fields_by_name['coord_system'].message_type = commontaskmodel__pb2._COORDINATESYSTEM
_MESHGRID.fields_by_name['coord_ref_system'].enum_type = commontaskmodel__pb2._COORDINATEREFERENCESYSTEM
_MESHGRID_MESHGRIDTYPE.containing_type = _MESHGRID
_MESHGRIDFILEDESC.fields_by_name['column_alias_list'].message_type = _COLUMNALIASLIST
_MESHGRIDFILEDESC.fields_by_name['mesh_grid'].message_type = _MESHGRID
DESCRIPTOR.message_types_by_name['FieldRenderState'] = _FIELDRENDERSTATE
DESCRIPTOR.message_types_by_name['LithologyDesc'] = _LITHOLOGYDESC
DESCRIPTOR.message_types_by_name['NoValue'] = _NOVALUE
DESCRIPTOR.message_types_by_name['MeshGridField'] = _MESHGRIDFIELD
DESCRIPTOR.message_types_by_name['RunLengthDouble'] = _RUNLENGTHDOUBLE
DESCRIPTOR.message_types_by_name['GridDesc'] = _GRIDDESC
DESCRIPTOR.message_types_by_name['MeshGrid'] = _MESHGRID
DESCRIPTOR.message_types_by_name['ColumnAliasList'] = _COLUMNALIASLIST
DESCRIPTOR.message_types_by_name['MeshGridFileDesc'] = _MESHGRIDFILEDESC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FieldRenderState = _reflection.GeneratedProtocolMessageType('FieldRenderState', (_message.Message,), {
  'DESCRIPTOR' : _FIELDRENDERSTATE,
  '__module__' : 'meshgrid_model_pb2'
  # @@protoc_insertion_point(class_scope:meshgrid_model.FieldRenderState)
  })
_sym_db.RegisterMessage(FieldRenderState)

LithologyDesc = _reflection.GeneratedProtocolMessageType('LithologyDesc', (_message.Message,), {
  'DESCRIPTOR' : _LITHOLOGYDESC,
  '__module__' : 'meshgrid_model_pb2'
  # @@protoc_insertion_point(class_scope:meshgrid_model.LithologyDesc)
  })
_sym_db.RegisterMessage(LithologyDesc)

NoValue = _reflection.GeneratedProtocolMessageType('NoValue', (_message.Message,), {
  'DESCRIPTOR' : _NOVALUE,
  '__module__' : 'meshgrid_model_pb2'
  # @@protoc_insertion_point(class_scope:meshgrid_model.NoValue)
  })
_sym_db.RegisterMessage(NoValue)

MeshGridField = _reflection.GeneratedProtocolMessageType('MeshGridField', (_message.Message,), {
  'DESCRIPTOR' : _MESHGRIDFIELD,
  '__module__' : 'meshgrid_model_pb2'
  # @@protoc_insertion_point(class_scope:meshgrid_model.MeshGridField)
  })
_sym_db.RegisterMessage(MeshGridField)

RunLengthDouble = _reflection.GeneratedProtocolMessageType('RunLengthDouble', (_message.Message,), {
  'DESCRIPTOR' : _RUNLENGTHDOUBLE,
  '__module__' : 'meshgrid_model_pb2'
  # @@protoc_insertion_point(class_scope:meshgrid_model.RunLengthDouble)
  })
_sym_db.RegisterMessage(RunLengthDouble)

GridDesc = _reflection.GeneratedProtocolMessageType('GridDesc', (_message.Message,), {
  'DESCRIPTOR' : _GRIDDESC,
  '__module__' : 'meshgrid_model_pb2'
  # @@protoc_insertion_point(class_scope:meshgrid_model.GridDesc)
  })
_sym_db.RegisterMessage(GridDesc)

MeshGrid = _reflection.GeneratedProtocolMessageType('MeshGrid', (_message.Message,), {
  'DESCRIPTOR' : _MESHGRID,
  '__module__' : 'meshgrid_model_pb2'
  # @@protoc_insertion_point(class_scope:meshgrid_model.MeshGrid)
  })
_sym_db.RegisterMessage(MeshGrid)

ColumnAliasList = _reflection.GeneratedProtocolMessageType('ColumnAliasList', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNALIASLIST,
  '__module__' : 'meshgrid_model_pb2'
  # @@protoc_insertion_point(class_scope:meshgrid_model.ColumnAliasList)
  })
_sym_db.RegisterMessage(ColumnAliasList)

MeshGridFileDesc = _reflection.GeneratedProtocolMessageType('MeshGridFileDesc', (_message.Message,), {
  'DESCRIPTOR' : _MESHGRIDFILEDESC,
  '__module__' : 'meshgrid_model_pb2'
  # @@protoc_insertion_point(class_scope:meshgrid_model.MeshGridFileDesc)
  })
_sym_db.RegisterMessage(MeshGridFileDesc)


# @@protoc_insertion_point(module_scope)
