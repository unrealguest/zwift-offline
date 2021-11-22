# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tcp-node-msgs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13tcp-node-msgs.proto\"A\n\rServerDetails\x12\n\n\x02\x66\x31\x18\x01 \x02(\x05\x12\n\n\x02\x66\x32\x18\x02 \x02(\x05\x12\n\n\x02ip\x18\x03 \x02(\t\x12\x0c\n\x04port\x18\x04 \x02(\x05\"S\n\x0cServersType1\x12\x1f\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32\x0e.ServerDetails\x12\n\n\x02\x66\x32\x18\x02 \x01(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05\x12\n\n\x02\x66\x34\x18\x04 \x01(\x05\"Y\n\x1eServerConnectionDetailsWrapper\x12\n\n\x02\x66\x31\x18\x01 \x02(\x05\x12\n\n\x02\x66\x32\x18\x02 \x02(\x05\x12\x1f\n\x07\x64\x65tails\x18\x03 \x03(\x0b\x32\x0e.ServerDetails\"V\n\x0cServersType2\x12\x38\n\x0f\x64\x65tails_wrapper\x18\x01 \x03(\x0b\x32\x1f.ServerConnectionDetailsWrapper\x12\x0c\n\x04port\x18\x02 \x02(\x05\"\x80\x01\n\rTCPServerInfo\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12\x11\n\tplayer_id\x18\x02 \x02(\x05\x12\n\n\x02\x66\x33\x18\x03 \x02(\x05\x12\x1e\n\x07servers\x18\x18 \x03(\x0b\x32\r.ServersType1\x12$\n\rother_servers\x18\x19 \x03(\x0b\x32\r.ServersType2\"E\n\x08TCPHello\x12\x11\n\tplayer_id\x18\x02 \x02(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05\x12\r\n\x05seqno\x18\x04 \x01(\x05\x12\x0b\n\x03\x66\x31\x33\x18\r \x01(\x05\"q\n\x13TCPCompanionConnect\x12\x11\n\tplayer_id\x18\x02 \x02(\x05\x12\r\n\x05\x64ummy\x18\x03 \x02(\x05\x12\x13\n\x0bzc_local_ip\x18\x0c \x02(\t\x12\x15\n\rzc_local_port\x18\x0f \x02(\x05\x12\x0c\n\x04kind\x18\x10 \x02(\x05\"N\n\x14RecurringTCPResponse\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12\x11\n\tplayer_id\x18\x02 \x01(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05\x12\x0b\n\x03\x66\x31\x31\x18\x0b \x01(\x05\"J\n\x12PhoneToGameCommand\x12\r\n\x05seqno\x18\x01 \x02(\x05\x12\x0f\n\x07\x63ommand\x18\x02 \x02(\x05\x12\x14\n\x0c\x63ommand_copy\x18\n \x02(\x05\"F\n\x0bPhoneToGame\x12\x11\n\tplayer_id\x18\x01 \x02(\x05\x12$\n\x07\x63ommand\x18\x02 \x03(\x0b\x32\x13.PhoneToGameCommand')



_SERVERDETAILS = DESCRIPTOR.message_types_by_name['ServerDetails']
_SERVERSTYPE1 = DESCRIPTOR.message_types_by_name['ServersType1']
_SERVERCONNECTIONDETAILSWRAPPER = DESCRIPTOR.message_types_by_name['ServerConnectionDetailsWrapper']
_SERVERSTYPE2 = DESCRIPTOR.message_types_by_name['ServersType2']
_TCPSERVERINFO = DESCRIPTOR.message_types_by_name['TCPServerInfo']
_TCPHELLO = DESCRIPTOR.message_types_by_name['TCPHello']
_TCPCOMPANIONCONNECT = DESCRIPTOR.message_types_by_name['TCPCompanionConnect']
_RECURRINGTCPRESPONSE = DESCRIPTOR.message_types_by_name['RecurringTCPResponse']
_PHONETOGAMECOMMAND = DESCRIPTOR.message_types_by_name['PhoneToGameCommand']
_PHONETOGAME = DESCRIPTOR.message_types_by_name['PhoneToGame']
ServerDetails = _reflection.GeneratedProtocolMessageType('ServerDetails', (_message.Message,), {
  'DESCRIPTOR' : _SERVERDETAILS,
  '__module__' : 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ServerDetails)
  })
_sym_db.RegisterMessage(ServerDetails)

ServersType1 = _reflection.GeneratedProtocolMessageType('ServersType1', (_message.Message,), {
  'DESCRIPTOR' : _SERVERSTYPE1,
  '__module__' : 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ServersType1)
  })
_sym_db.RegisterMessage(ServersType1)

ServerConnectionDetailsWrapper = _reflection.GeneratedProtocolMessageType('ServerConnectionDetailsWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SERVERCONNECTIONDETAILSWRAPPER,
  '__module__' : 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ServerConnectionDetailsWrapper)
  })
_sym_db.RegisterMessage(ServerConnectionDetailsWrapper)

ServersType2 = _reflection.GeneratedProtocolMessageType('ServersType2', (_message.Message,), {
  'DESCRIPTOR' : _SERVERSTYPE2,
  '__module__' : 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ServersType2)
  })
_sym_db.RegisterMessage(ServersType2)

TCPServerInfo = _reflection.GeneratedProtocolMessageType('TCPServerInfo', (_message.Message,), {
  'DESCRIPTOR' : _TCPSERVERINFO,
  '__module__' : 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:TCPServerInfo)
  })
_sym_db.RegisterMessage(TCPServerInfo)

TCPHello = _reflection.GeneratedProtocolMessageType('TCPHello', (_message.Message,), {
  'DESCRIPTOR' : _TCPHELLO,
  '__module__' : 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:TCPHello)
  })
_sym_db.RegisterMessage(TCPHello)

TCPCompanionConnect = _reflection.GeneratedProtocolMessageType('TCPCompanionConnect', (_message.Message,), {
  'DESCRIPTOR' : _TCPCOMPANIONCONNECT,
  '__module__' : 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:TCPCompanionConnect)
  })
_sym_db.RegisterMessage(TCPCompanionConnect)

RecurringTCPResponse = _reflection.GeneratedProtocolMessageType('RecurringTCPResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECURRINGTCPRESPONSE,
  '__module__' : 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:RecurringTCPResponse)
  })
_sym_db.RegisterMessage(RecurringTCPResponse)

PhoneToGameCommand = _reflection.GeneratedProtocolMessageType('PhoneToGameCommand', (_message.Message,), {
  'DESCRIPTOR' : _PHONETOGAMECOMMAND,
  '__module__' : 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PhoneToGameCommand)
  })
_sym_db.RegisterMessage(PhoneToGameCommand)

PhoneToGame = _reflection.GeneratedProtocolMessageType('PhoneToGame', (_message.Message,), {
  'DESCRIPTOR' : _PHONETOGAME,
  '__module__' : 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PhoneToGame)
  })
_sym_db.RegisterMessage(PhoneToGame)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SERVERDETAILS._serialized_start=23
  _SERVERDETAILS._serialized_end=88
  _SERVERSTYPE1._serialized_start=90
  _SERVERSTYPE1._serialized_end=173
  _SERVERCONNECTIONDETAILSWRAPPER._serialized_start=175
  _SERVERCONNECTIONDETAILSWRAPPER._serialized_end=264
  _SERVERSTYPE2._serialized_start=266
  _SERVERSTYPE2._serialized_end=352
  _TCPSERVERINFO._serialized_start=355
  _TCPSERVERINFO._serialized_end=483
  _TCPHELLO._serialized_start=485
  _TCPHELLO._serialized_end=554
  _TCPCOMPANIONCONNECT._serialized_start=556
  _TCPCOMPANIONCONNECT._serialized_end=669
  _RECURRINGTCPRESPONSE._serialized_start=671
  _RECURRINGTCPRESPONSE._serialized_end=749
  _PHONETOGAMECOMMAND._serialized_start=751
  _PHONETOGAMECOMMAND._serialized_end=825
  _PHONETOGAME._serialized_start=827
  _PHONETOGAME._serialized_end=897
# @@protoc_insertion_point(module_scope)
