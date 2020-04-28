# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: variograms.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import intrepid.commontaskmodel_pb2 as commontaskmodel__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='variograms.proto',
  package='vario',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10variograms.proto\x12\x05vario\x1a\x15\x63ommontaskmodel.proto\"\xff\x02\n\x15Variogram_Lags_Master\x12\x13\n\x0bnumber_bins\x18\x01 \x01(\x05\x12\x14\n\tbin_width\x18\x03 \x01(\x01:\x01\x31\x12\x12\n\x07\x61zimuth\x18\x04 \x01(\x01:\x01\x30\x12\x1b\n\x13GeophysicalDatabase\x18\x05 \x01(\t\x12\x18\n\x0bSignalField\x18\x06 \x01(\t:\x03mag\x12\x1b\n\x10signal_subsample\x18\x07 \x01(\x05:\x01\x31\x12\x1e\n\x0e\x45levationField\x18\x08 \x01(\t:\x06gps_ht\x12/\n\nFlightType\x18\t \x01(\x0e\x32\x10.ctm.FlightTypes:\tLT_FLIGHT\x12\x32\n\x04type\x18\n \x01(\x0e\x32\x19.ctm.GeophysicsSignalType:\tMagnetism\x12)\n\nProjection\x18\x0b \x01(\x0b\x32\x15.ctm.CoordinateSystem\x12#\n\x04lags\x18\x0c \x03(\x0b\x32\x15.vario.Variogram_Lags\"\xaa\x01\n\x0eVariogram_Lags\x12\x13\n\x0bline_number\x18\x01 \x01(\x05\x12\t\n\x01X\x18\x02 \x01(\x01\x12\t\n\x01Y\x18\x03 \x01(\x01\x12\x0f\n\x04nges\x18\x04 \x01(\x01:\x01\x30\x12\"\n\televation\x18\x05 \x01(\x0b\x32\x0f.ctm.BasicStats\x12\r\n\x05struc\x18\x06 \x03(\x01\x12\x19\n\x04tens\x18\x07 \x03(\x0b\x32\x0b.ctm.Tensor\x12\x0e\n\x06nstruc\x18\x08 \x03(\x01\"\xb4\x02\n\x0f\x43ovarianceModel\x12\x1a\n\x0cTheIsotropic\x18\x02 \x01(\x08:\x04true\x12\x16\n\x08TheRange\x18\x03 \x01(\x01:\x04\x31\x30\x30\x30\x12\x1a\n\x0bTheVariance\x18\x04 \x01(\x01:\x05\x32\x33\x38\x30\x39\x12\x19\n\x0eTheVarGradient\x18\x05 \x01(\x01:\x01\x31\x12\x1d\n\x12TheTangentVariance\x18\x06 \x01(\x01:\x01\x31\x12\x1b\n\x0cThePotNugget\x18\x07 \x01(\x01:\x05\x31\x65-06\x12\x1f\n\x11TheGradientNugget\x18\x08 \x01(\x01:\x04\x30.01\x12\x1e\n\x10TheTangentNugget\x18\t \x01(\x01:\x04\x30.01\x12\x1a\n\x0fTheDeriveDegree\x18\n \x01(\x05:\x01\x31\x12\r\n\x05\x43oefs\x18\x0b \x03(\x01\x12\x0e\n\x06\x41ngles\x18\x0c \x03(\x01\"\xb2\x01\n\x13GeostatisticsMaster\x12;\n\x15Variogram_Lags_Master\x18\x01 \x01(\x0b\x32\x1c.vario.Variogram_Lags_Master\x12-\n\x0eVariogram_Lags\x18\x02 \x01(\x0b\x32\x15.vario.Variogram_Lags\x12/\n\x0f\x43ovarianceModel\x18\x03 \x01(\x0b\x32\x16.vario.CovarianceModel*y\n\x0e\x43ovarianceType\x12\x13\n\x0fPotential_Gauss\x10\x00\x12\x15\n\x11Potential_Cubique\x10\x01\x12\x14\n\x10Potential_h4logh\x10\x02\x12\x10\n\x0cPotential_h3\x10\x03\x12\x13\n\x0fPotential_Penta\x10\x04')
  ,
  dependencies=[commontaskmodel__pb2.DESCRIPTOR,])

_COVARIANCETYPE = _descriptor.EnumDescriptor(
  name='CovarianceType',
  full_name='vario.CovarianceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Potential_Gauss', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Potential_Cubique', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Potential_h4logh', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Potential_h3', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Potential_Penta', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1101,
  serialized_end=1222,
)
_sym_db.RegisterEnumDescriptor(_COVARIANCETYPE)

CovarianceType = enum_type_wrapper.EnumTypeWrapper(_COVARIANCETYPE)
Potential_Gauss = 0
Potential_Cubique = 1
Potential_h4logh = 2
Potential_h3 = 3
Potential_Penta = 4



_VARIOGRAM_LAGS_MASTER = _descriptor.Descriptor(
  name='Variogram_Lags_Master',
  full_name='vario.Variogram_Lags_Master',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number_bins', full_name='vario.Variogram_Lags_Master.number_bins', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bin_width', full_name='vario.Variogram_Lags_Master.bin_width', index=1,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='azimuth', full_name='vario.Variogram_Lags_Master.azimuth', index=2,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='GeophysicalDatabase', full_name='vario.Variogram_Lags_Master.GeophysicalDatabase', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SignalField', full_name='vario.Variogram_Lags_Master.SignalField', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("mag").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signal_subsample', full_name='vario.Variogram_Lags_Master.signal_subsample', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ElevationField', full_name='vario.Variogram_Lags_Master.ElevationField', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("gps_ht").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FlightType', full_name='vario.Variogram_Lags_Master.FlightType', index=7,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='vario.Variogram_Lags_Master.type', index=8,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=15,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Projection', full_name='vario.Variogram_Lags_Master.Projection', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lags', full_name='vario.Variogram_Lags_Master.lags', index=10,
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
  serialized_start=51,
  serialized_end=434,
)


_VARIOGRAM_LAGS = _descriptor.Descriptor(
  name='Variogram_Lags',
  full_name='vario.Variogram_Lags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line_number', full_name='vario.Variogram_Lags.line_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='X', full_name='vario.Variogram_Lags.X', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Y', full_name='vario.Variogram_Lags.Y', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nges', full_name='vario.Variogram_Lags.nges', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elevation', full_name='vario.Variogram_Lags.elevation', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='struc', full_name='vario.Variogram_Lags.struc', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tens', full_name='vario.Variogram_Lags.tens', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nstruc', full_name='vario.Variogram_Lags.nstruc', index=7,
      number=8, type=1, cpp_type=5, label=3,
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
  serialized_start=437,
  serialized_end=607,
)


_COVARIANCEMODEL = _descriptor.Descriptor(
  name='CovarianceModel',
  full_name='vario.CovarianceModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TheIsotropic', full_name='vario.CovarianceModel.TheIsotropic', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TheRange', full_name='vario.CovarianceModel.TheRange', index=1,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1000),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TheVariance', full_name='vario.CovarianceModel.TheVariance', index=2,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(23809),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TheVarGradient', full_name='vario.CovarianceModel.TheVarGradient', index=3,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TheTangentVariance', full_name='vario.CovarianceModel.TheTangentVariance', index=4,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ThePotNugget', full_name='vario.CovarianceModel.ThePotNugget', index=5,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1e-06),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TheGradientNugget', full_name='vario.CovarianceModel.TheGradientNugget', index=6,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.01),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TheTangentNugget', full_name='vario.CovarianceModel.TheTangentNugget', index=7,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.01),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TheDeriveDegree', full_name='vario.CovarianceModel.TheDeriveDegree', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Coefs', full_name='vario.CovarianceModel.Coefs', index=9,
      number=11, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Angles', full_name='vario.CovarianceModel.Angles', index=10,
      number=12, type=1, cpp_type=5, label=3,
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
  serialized_start=610,
  serialized_end=918,
)


_GEOSTATISTICSMASTER = _descriptor.Descriptor(
  name='GeostatisticsMaster',
  full_name='vario.GeostatisticsMaster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Variogram_Lags_Master', full_name='vario.GeostatisticsMaster.Variogram_Lags_Master', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Variogram_Lags', full_name='vario.GeostatisticsMaster.Variogram_Lags', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CovarianceModel', full_name='vario.GeostatisticsMaster.CovarianceModel', index=2,
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
  serialized_start=921,
  serialized_end=1099,
)

_VARIOGRAM_LAGS_MASTER.fields_by_name['FlightType'].enum_type = commontaskmodel__pb2._FLIGHTTYPES
_VARIOGRAM_LAGS_MASTER.fields_by_name['type'].enum_type = commontaskmodel__pb2._GEOPHYSICSSIGNALTYPE
_VARIOGRAM_LAGS_MASTER.fields_by_name['Projection'].message_type = commontaskmodel__pb2._COORDINATESYSTEM
_VARIOGRAM_LAGS_MASTER.fields_by_name['lags'].message_type = _VARIOGRAM_LAGS
_VARIOGRAM_LAGS.fields_by_name['elevation'].message_type = commontaskmodel__pb2._BASICSTATS
_VARIOGRAM_LAGS.fields_by_name['tens'].message_type = commontaskmodel__pb2._TENSOR
_GEOSTATISTICSMASTER.fields_by_name['Variogram_Lags_Master'].message_type = _VARIOGRAM_LAGS_MASTER
_GEOSTATISTICSMASTER.fields_by_name['Variogram_Lags'].message_type = _VARIOGRAM_LAGS
_GEOSTATISTICSMASTER.fields_by_name['CovarianceModel'].message_type = _COVARIANCEMODEL
DESCRIPTOR.message_types_by_name['Variogram_Lags_Master'] = _VARIOGRAM_LAGS_MASTER
DESCRIPTOR.message_types_by_name['Variogram_Lags'] = _VARIOGRAM_LAGS
DESCRIPTOR.message_types_by_name['CovarianceModel'] = _COVARIANCEMODEL
DESCRIPTOR.message_types_by_name['GeostatisticsMaster'] = _GEOSTATISTICSMASTER
DESCRIPTOR.enum_types_by_name['CovarianceType'] = _COVARIANCETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Variogram_Lags_Master = _reflection.GeneratedProtocolMessageType('Variogram_Lags_Master', (_message.Message,), {
  'DESCRIPTOR' : _VARIOGRAM_LAGS_MASTER,
  '__module__' : 'variograms_pb2'
  # @@protoc_insertion_point(class_scope:vario.Variogram_Lags_Master)
  })
_sym_db.RegisterMessage(Variogram_Lags_Master)

Variogram_Lags = _reflection.GeneratedProtocolMessageType('Variogram_Lags', (_message.Message,), {
  'DESCRIPTOR' : _VARIOGRAM_LAGS,
  '__module__' : 'variograms_pb2'
  # @@protoc_insertion_point(class_scope:vario.Variogram_Lags)
  })
_sym_db.RegisterMessage(Variogram_Lags)

CovarianceModel = _reflection.GeneratedProtocolMessageType('CovarianceModel', (_message.Message,), {
  'DESCRIPTOR' : _COVARIANCEMODEL,
  '__module__' : 'variograms_pb2'
  # @@protoc_insertion_point(class_scope:vario.CovarianceModel)
  })
_sym_db.RegisterMessage(CovarianceModel)

GeostatisticsMaster = _reflection.GeneratedProtocolMessageType('GeostatisticsMaster', (_message.Message,), {
  'DESCRIPTOR' : _GEOSTATISTICSMASTER,
  '__module__' : 'variograms_pb2'
  # @@protoc_insertion_point(class_scope:vario.GeostatisticsMaster)
  })
_sym_db.RegisterMessage(GeostatisticsMaster)


# @@protoc_insertion_point(module_scope)
