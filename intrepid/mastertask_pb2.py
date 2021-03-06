# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mastertask.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import intrepid.intrepid_tasks_pb2 as intrepid__tasks__pb2
import intrepid.intrepid_3dexplore_pb2 as intrepid__3dexplore__pb2
import intrepid.gmtaskmodel_pb2 as gmtaskmodel__pb2
import intrepid.invtaskmodel_pb2 as invtaskmodel__pb2
import intrepid.Petrel_data_interchange_pb2 as Petrel__data__interchange__pb2
import intrepid.magnetic_methods_pb2 as magnetic__methods__pb2
import intrepid.jetstream_pb2 as jetstream__pb2
import intrepid.AEMINV_pb2 as AEMINV__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mastertask.proto',
  package='mastertask',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10mastertask.proto\x12\nmastertask\x1a\x14intrepid_tasks.proto\x1a\x18intrepid_3dexplore.proto\x1a\x11gmtaskmodel.proto\x1a\x12invtaskmodel.proto\x1a\x1dPetrel_data_interchange.proto\x1a\x16magnetic_methods.proto\x1a\x0fjetstream.proto\x1a\x0c\x41\x45MINV.proto\"\xc5\x03\n\x08\x42\x61tchJob\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\tauditfile\x18\x03 \x01(\t\x12,\n\x0cIntrepidTask\x18\x04 \x03(\x0b\x32\x16.intrepid.IntrepidTask\x12\x35\n\x0fGeomodellerTask\x18\x05 \x03(\x0b\x32\x1c.gmtaskmodel.GeomodellerTask\x12\x32\n\rInversionTask\x18\x06 \x03(\x0b\x32\x1b.invtaskmodel.InversionTask\x12\'\n\nPetrelTask\x18\x07 \x03(\x0b\x32\x13.eclipse.PetrelTask\x12,\n\x0cMagneticTask\x18\x08 \x03(\x0b\x32\x16.magnetic.MagneticTask\x12)\n\rJetstreamTask\x18\t \x03(\x0b\x32\x12.jet.JetstreamTask\x12&\n\x07\x41\x45MTask\x18\n \x03(\x0b\x32\x15.AEMInversion.AEMTask\x12@\n\x11Intrepid3DExplore\x18\x0b \x03(\x0b\x32%.intrepid_3dexplore.Intrepid3DExplore'
  ,
  dependencies=[intrepid__tasks__pb2.DESCRIPTOR,intrepid__3dexplore__pb2.DESCRIPTOR,gmtaskmodel__pb2.DESCRIPTOR,invtaskmodel__pb2.DESCRIPTOR,Petrel__data__interchange__pb2.DESCRIPTOR,magnetic__methods__pb2.DESCRIPTOR,jetstream__pb2.DESCRIPTOR,AEMINV__pb2.DESCRIPTOR,])




_BATCHJOB = _descriptor.Descriptor(
  name='BatchJob',
  full_name='mastertask.BatchJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mastertask.BatchJob.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='mastertask.BatchJob.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auditfile', full_name='mastertask.BatchJob.auditfile', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='IntrepidTask', full_name='mastertask.BatchJob.IntrepidTask', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='GeomodellerTask', full_name='mastertask.BatchJob.GeomodellerTask', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='InversionTask', full_name='mastertask.BatchJob.InversionTask', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PetrelTask', full_name='mastertask.BatchJob.PetrelTask', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MagneticTask', full_name='mastertask.BatchJob.MagneticTask', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='JetstreamTask', full_name='mastertask.BatchJob.JetstreamTask', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AEMTask', full_name='mastertask.BatchJob.AEMTask', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Intrepid3DExplore', full_name='mastertask.BatchJob.Intrepid3DExplore', index=10,
      number=11, type=11, cpp_type=10, label=3,
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
  serialized_start=206,
  serialized_end=659,
)

_BATCHJOB.fields_by_name['IntrepidTask'].message_type = intrepid__tasks__pb2._INTREPIDTASK
_BATCHJOB.fields_by_name['GeomodellerTask'].message_type = gmtaskmodel__pb2._GEOMODELLERTASK
_BATCHJOB.fields_by_name['InversionTask'].message_type = invtaskmodel__pb2._INVERSIONTASK
_BATCHJOB.fields_by_name['PetrelTask'].message_type = Petrel__data__interchange__pb2._PETRELTASK
_BATCHJOB.fields_by_name['MagneticTask'].message_type = magnetic__methods__pb2._MAGNETICTASK
_BATCHJOB.fields_by_name['JetstreamTask'].message_type = jetstream__pb2._JETSTREAMTASK
_BATCHJOB.fields_by_name['AEMTask'].message_type = AEMINV__pb2._AEMTASK
_BATCHJOB.fields_by_name['Intrepid3DExplore'].message_type = intrepid__3dexplore__pb2._INTREPID3DEXPLORE
DESCRIPTOR.message_types_by_name['BatchJob'] = _BATCHJOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchJob = _reflection.GeneratedProtocolMessageType('BatchJob', (_message.Message,), {
  'DESCRIPTOR' : _BATCHJOB,
  '__module__' : 'mastertask_pb2'
  # @@protoc_insertion_point(class_scope:mastertask.BatchJob)
  })
_sym_db.RegisterMessage(BatchJob)


# @@protoc_insertion_point(module_scope)
