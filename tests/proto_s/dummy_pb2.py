# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dummy.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='dummy.proto',
    package='dummy',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x0b\x64ummy.proto\x12\x05\x64ummy\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd5\x01\n\x08\x45nvelope\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x0f\n\x07part_id\x18\x03 \x01(\r\x12\x10\n\x08num_part\x18\x04 \x03(\r\x12\x0f\n\x07timeout\x18\x05 \x01(\r\x12%\n\x06routes\x18\x06 \x03(\x0b\x32\x15.dummy.Envelope.route\x1aG\n\x05route\x12\x0f\n\x07service\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\",\n\x07Message\x12!\n\x08\x65nvelope\x18\x01 \x01(\x0b\x32\x0f.dummy.Envelope2@\n\x10\x44ummyGRPCService\x12,\n\x08\x64ummyAPI\x12\x0e.dummy.Message\x1a\x0e.dummy.Message\"\x00\x62\x06proto3')
    ,
    dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR, ])

_ENVELOPE_ROUTE = _descriptor.Descriptor(
    name='route',
    full_name='dummy.Envelope.route',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='service', full_name='dummy.Envelope.route.service', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='timestamp', full_name='dummy.Envelope.route.timestamp', index=1,
            number=2, type=11, cpp_type=10, label=1,
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=198,
    serialized_end=269,
)

_ENVELOPE = _descriptor.Descriptor(
    name='Envelope',
    full_name='dummy.Envelope',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='client_id', full_name='dummy.Envelope.client_id', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='request_id', full_name='dummy.Envelope.request_id', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='part_id', full_name='dummy.Envelope.part_id', index=2,
            number=3, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='num_part', full_name='dummy.Envelope.num_part', index=3,
            number=4, type=13, cpp_type=3, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='timeout', full_name='dummy.Envelope.timeout', index=4,
            number=5, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='routes', full_name='dummy.Envelope.routes', index=5,
            number=6, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_ENVELOPE_ROUTE, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=56,
    serialized_end=269,
)

_MESSAGE = _descriptor.Descriptor(
    name='Message',
    full_name='dummy.Message',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='envelope', full_name='dummy.Message.envelope', index=0,
            number=1, type=11, cpp_type=10, label=1,
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=271,
    serialized_end=315,
)

_ENVELOPE_ROUTE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ENVELOPE_ROUTE.containing_type = _ENVELOPE
_ENVELOPE.fields_by_name['routes'].message_type = _ENVELOPE_ROUTE
_MESSAGE.fields_by_name['envelope'].message_type = _ENVELOPE
DESCRIPTOR.message_types_by_name['Envelope'] = _ENVELOPE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Envelope = _reflection.GeneratedProtocolMessageType('Envelope', (_message.Message,), dict(

    route=_reflection.GeneratedProtocolMessageType('route', (_message.Message,), dict(
        DESCRIPTOR=_ENVELOPE_ROUTE,
        __module__='dummy_pb2'
        # @@protoc_insertion_point(class_scope:dummy.Envelope.route)
    ))
    ,
    DESCRIPTOR=_ENVELOPE,
    __module__='dummy_pb2'
    # @@protoc_insertion_point(class_scope:dummy.Envelope)
))
_sym_db.RegisterMessage(Envelope)
_sym_db.RegisterMessage(Envelope.route)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
    DESCRIPTOR=_MESSAGE,
    __module__='dummy_pb2'
    # @@protoc_insertion_point(class_scope:dummy.Message)
))
_sym_db.RegisterMessage(Message)

_DUMMYGRPCSERVICE = _descriptor.ServiceDescriptor(
    name='DummyGRPCService',
    full_name='dummy.DummyGRPCService',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=317,
    serialized_end=381,
    methods=[
        _descriptor.MethodDescriptor(
            name='dummyAPI',
            full_name='dummy.DummyGRPCService.dummyAPI',
            index=0,
            containing_service=None,
            input_type=_MESSAGE,
            output_type=_MESSAGE,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_DUMMYGRPCSERVICE)

DESCRIPTOR.services_by_name['DummyGRPCService'] = _DUMMYGRPCSERVICE

# @@protoc_insertion_point(module_scope)
