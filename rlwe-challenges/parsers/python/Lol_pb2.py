# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Lol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Lol.proto',
  package='',
  serialized_pb=_b('\n\tLol.proto\"<\n\x08LinearRq\x12\t\n\x01\x65\x18\x01 \x02(\r\x12\t\n\x01r\x18\x02 \x02(\r\x12\x1a\n\x06\x63oeffs\x18\x03 \x03(\x0b\x32\n.RqProduct\"\x1a\n\x01R\x12\t\n\x01m\x18\x01 \x02(\r\x12\n\n\x02xs\x18\x02 \x03(\x12\"\'\n\x03Rq1\x12\t\n\x01m\x18\x01 \x02(\r\x12\t\n\x01q\x18\x02 \x02(\x04\x12\n\n\x02xs\x18\x03 \x03(\x12\"\'\n\x03Kq1\x12\t\n\x01m\x18\x01 \x02(\r\x12\t\n\x01q\x18\x02 \x02(\x04\x12\n\n\x02xs\x18\x03 \x03(\x01\"!\n\tRqProduct\x12\x14\n\x06rqlist\x18\x01 \x03(\x0b\x32\x04.Rq1\"!\n\tKqProduct\x12\x14\n\x06kqlist\x18\x01 \x03(\x0b\x32\x04.Kq1\"\x1f\n\x07TypeRep\x12\t\n\x01\x61\x18\x01 \x02(\x04\x12\t\n\x01\x62\x18\x02 \x02(\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LINEARRQ = _descriptor.Descriptor(
  name='LinearRq',
  full_name='LinearRq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='e', full_name='LinearRq.e', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r', full_name='LinearRq.r', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coeffs', full_name='LinearRq.coeffs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=73,
)


_R = _descriptor.Descriptor(
  name='R',
  full_name='R',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m', full_name='R.m', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xs', full_name='R.xs', index=1,
      number=2, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=101,
)


_RQ1 = _descriptor.Descriptor(
  name='Rq1',
  full_name='Rq1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m', full_name='Rq1.m', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q', full_name='Rq1.q', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xs', full_name='Rq1.xs', index=2,
      number=3, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=142,
)


_KQ1 = _descriptor.Descriptor(
  name='Kq1',
  full_name='Kq1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m', full_name='Kq1.m', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='q', full_name='Kq1.q', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xs', full_name='Kq1.xs', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=183,
)


_RQPRODUCT = _descriptor.Descriptor(
  name='RqProduct',
  full_name='RqProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rqlist', full_name='RqProduct.rqlist', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=218,
)


_KQPRODUCT = _descriptor.Descriptor(
  name='KqProduct',
  full_name='KqProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kqlist', full_name='KqProduct.kqlist', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=253,
)


_TYPEREP = _descriptor.Descriptor(
  name='TypeRep',
  full_name='TypeRep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='TypeRep.a', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='TypeRep.b', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=286,
)

_LINEARRQ.fields_by_name['coeffs'].message_type = _RQPRODUCT
_RQPRODUCT.fields_by_name['rqlist'].message_type = _RQ1
_KQPRODUCT.fields_by_name['kqlist'].message_type = _KQ1
DESCRIPTOR.message_types_by_name['LinearRq'] = _LINEARRQ
DESCRIPTOR.message_types_by_name['R'] = _R
DESCRIPTOR.message_types_by_name['Rq1'] = _RQ1
DESCRIPTOR.message_types_by_name['Kq1'] = _KQ1
DESCRIPTOR.message_types_by_name['RqProduct'] = _RQPRODUCT
DESCRIPTOR.message_types_by_name['KqProduct'] = _KQPRODUCT
DESCRIPTOR.message_types_by_name['TypeRep'] = _TYPEREP

LinearRq = _reflection.GeneratedProtocolMessageType('LinearRq', (_message.Message,), dict(
  DESCRIPTOR = _LINEARRQ,
  __module__ = 'Lol_pb2'
  # @@protoc_insertion_point(class_scope:LinearRq)
  ))
_sym_db.RegisterMessage(LinearRq)

R = _reflection.GeneratedProtocolMessageType('R', (_message.Message,), dict(
  DESCRIPTOR = _R,
  __module__ = 'Lol_pb2'
  # @@protoc_insertion_point(class_scope:R)
  ))
_sym_db.RegisterMessage(R)

Rq1 = _reflection.GeneratedProtocolMessageType('Rq1', (_message.Message,), dict(
  DESCRIPTOR = _RQ1,
  __module__ = 'Lol_pb2'
  # @@protoc_insertion_point(class_scope:Rq1)
  ))
_sym_db.RegisterMessage(Rq1)

Kq1 = _reflection.GeneratedProtocolMessageType('Kq1', (_message.Message,), dict(
  DESCRIPTOR = _KQ1,
  __module__ = 'Lol_pb2'
  # @@protoc_insertion_point(class_scope:Kq1)
  ))
_sym_db.RegisterMessage(Kq1)

RqProduct = _reflection.GeneratedProtocolMessageType('RqProduct', (_message.Message,), dict(
  DESCRIPTOR = _RQPRODUCT,
  __module__ = 'Lol_pb2'
  # @@protoc_insertion_point(class_scope:RqProduct)
  ))
_sym_db.RegisterMessage(RqProduct)

KqProduct = _reflection.GeneratedProtocolMessageType('KqProduct', (_message.Message,), dict(
  DESCRIPTOR = _KQPRODUCT,
  __module__ = 'Lol_pb2'
  # @@protoc_insertion_point(class_scope:KqProduct)
  ))
_sym_db.RegisterMessage(KqProduct)

TypeRep = _reflection.GeneratedProtocolMessageType('TypeRep', (_message.Message,), dict(
  DESCRIPTOR = _TYPEREP,
  __module__ = 'Lol_pb2'
  # @@protoc_insertion_point(class_scope:TypeRep)
  ))
_sym_db.RegisterMessage(TypeRep)


# @@protoc_insertion_point(module_scope)