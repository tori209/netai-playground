# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: flow/flow.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'flow/flow.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x66low/flow.proto\x12\x04\x66low\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x89\x0b\n\x04\x46low\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04uuid\x18\" \x01(\t\x12\x1e\n\x07verdict\x18\x02 \x01(\x0e\x32\r.flow.Verdict\x12\x17\n\x0b\x64rop_reason\x18\x03 \x01(\rB\x02\x18\x01\x12!\n\tauth_type\x18# \x01(\x0e\x32\x0e.flow.AuthType\x12 \n\x08\x65thernet\x18\x04 \x01(\x0b\x32\x0e.flow.Ethernet\x12\x14\n\x02IP\x18\x05 \x01(\x0b\x32\x08.flow.IP\x12\x18\n\x02l4\x18\x06 \x01(\x0b\x32\x0c.flow.Layer4\x12\x1e\n\x06source\x18\x08 \x01(\x0b\x32\x0e.flow.Endpoint\x12#\n\x0b\x64\x65stination\x18\t \x01(\x0b\x32\x0e.flow.Endpoint\x12\x1c\n\x04Type\x18\n \x01(\x0e\x32\x0e.flow.FlowType\x12\x11\n\tnode_name\x18\x0b \x01(\t\x12\x13\n\x0bnode_labels\x18% \x03(\t\x12\x14\n\x0csource_names\x18\r \x03(\t\x12\x19\n\x11\x64\x65stination_names\x18\x0e \x03(\t\x12\x18\n\x02l7\x18\x0f \x01(\x0b\x32\x0c.flow.Layer7\x12\x11\n\x05reply\x18\x10 \x01(\x08\x42\x02\x18\x01\x12)\n\nevent_type\x18\x13 \x01(\x0b\x32\x15.flow.CiliumEventType\x12%\n\x0esource_service\x18\x14 \x01(\x0b\x32\r.flow.Service\x12*\n\x13\x64\x65stination_service\x18\x15 \x01(\x0b\x32\r.flow.Service\x12\x31\n\x11traffic_direction\x18\x16 \x01(\x0e\x32\x16.flow.TrafficDirection\x12\x19\n\x11policy_match_type\x18\x17 \x01(\r\x12<\n\x17trace_observation_point\x18\x18 \x01(\x0e\x32\x1b.flow.TraceObservationPoint\x12\'\n\x0ctrace_reason\x18$ \x01(\x0e\x32\x11.flow.TraceReason\x12\x1c\n\x04\x66ile\x18& \x01(\x0b\x32\x0e.flow.FileInfo\x12*\n\x10\x64rop_reason_desc\x18\x19 \x01(\x0e\x32\x10.flow.DropReason\x12,\n\x08is_reply\x18\x1a \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x13\x64\x65\x62ug_capture_point\x18\x1b \x01(\x0e\x32\x17.flow.DebugCapturePoint\x12)\n\tinterface\x18\x1c \x01(\x0b\x32\x16.flow.NetworkInterface\x12\x12\n\nproxy_port\x18\x1d \x01(\r\x12)\n\rtrace_context\x18\x1e \x01(\x0b\x32\x12.flow.TraceContext\x12\x36\n\x10sock_xlate_point\x18\x1f \x01(\x0e\x32\x1c.flow.SocketTranslationPoint\x12\x15\n\rsocket_cookie\x18  \x01(\x04\x12\x11\n\tcgroup_id\x18! \x01(\x04\x12\x15\n\x07Summary\x18\xa0\x8d\x06 \x01(\tB\x02\x18\x01\x12*\n\nextensions\x18\xf0\x93\t \x01(\x0b\x32\x14.google.protobuf.Any\x12)\n\x11\x65gress_allowed_by\x18\x89\xa4\x01 \x03(\x0b\x32\x0c.flow.Policy\x12*\n\x12ingress_allowed_by\x18\x8a\xa4\x01 \x03(\x0b\x32\x0c.flow.Policy\x12(\n\x10\x65gress_denied_by\x18\x8c\xa4\x01 \x03(\x0b\x32\x0c.flow.Policy\x12)\n\x11ingress_denied_by\x18\x8d\xa4\x01 \x03(\x0b\x32\x0c.flow.PolicyJ\x04\x08\x07\x10\x08J\x04\x08\x0c\x10\rJ\x04\x08\x11\x10\x12J\x04\x08\x12\x10\x13\"&\n\x08\x46ileInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04line\x18\x02 \x01(\r\"\xa4\x01\n\x06Layer4\x12\x18\n\x03TCP\x18\x01 \x01(\x0b\x32\t.flow.TCPH\x00\x12\x18\n\x03UDP\x18\x02 \x01(\x0b\x32\t.flow.UDPH\x00\x12\x1e\n\x06ICMPv4\x18\x03 \x01(\x0b\x32\x0c.flow.ICMPv4H\x00\x12\x1e\n\x06ICMPv6\x18\x04 \x01(\x0b\x32\x0c.flow.ICMPv6H\x00\x12\x1a\n\x04SCTP\x18\x05 \x01(\x0b\x32\n.flow.SCTPH\x00\x42\n\n\x08protocol\"\x9a\x01\n\x06Layer7\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.flow.L7FlowType\x12\x12\n\nlatency_ns\x18\x02 \x01(\x04\x12\x18\n\x03\x64ns\x18\x64 \x01(\x0b\x32\t.flow.DNSH\x00\x12\x1a\n\x04http\x18\x65 \x01(\x0b\x32\n.flow.HTTPH\x00\x12\x1c\n\x05kafka\x18\x66 \x01(\x0b\x32\x0b.flow.KafkaH\x00\x42\x08\n\x06record\"1\n\x0cTraceContext\x12!\n\x06parent\x18\x01 \x01(\x0b\x32\x11.flow.TraceParent\"\x1f\n\x0bTraceParent\x12\x10\n\x08trace_id\x18\x01 \x01(\t\"\x96\x01\n\x08\x45ndpoint\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x10\n\x08identity\x18\x02 \x01(\r\x12\x14\n\x0c\x63luster_name\x18\x07 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\x0e\n\x06labels\x18\x04 \x03(\t\x12\x10\n\x08pod_name\x18\x05 \x01(\t\x12!\n\tworkloads\x18\x06 \x03(\x0b\x32\x0e.flow.Workload\"&\n\x08Workload\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\"S\n\x03TCP\x12\x13\n\x0bsource_port\x18\x01 \x01(\r\x12\x18\n\x10\x64\x65stination_port\x18\x02 \x01(\r\x12\x1d\n\x05\x66lags\x18\x03 \x01(\x0b\x32\x0e.flow.TCPFlags\"w\n\x02IP\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x15\n\rsource_xlated\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\"\n\tipVersion\x18\x03 \x01(\x0e\x32\x0f.flow.IPVersion\x12\x11\n\tencrypted\x18\x04 \x01(\x08\"/\n\x08\x45thernet\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\"~\n\x08TCPFlags\x12\x0b\n\x03\x46IN\x18\x01 \x01(\x08\x12\x0b\n\x03SYN\x18\x02 \x01(\x08\x12\x0b\n\x03RST\x18\x03 \x01(\x08\x12\x0b\n\x03PSH\x18\x04 \x01(\x08\x12\x0b\n\x03\x41\x43K\x18\x05 \x01(\x08\x12\x0b\n\x03URG\x18\x06 \x01(\x08\x12\x0b\n\x03\x45\x43\x45\x18\x07 \x01(\x08\x12\x0b\n\x03\x43WR\x18\x08 \x01(\x08\x12\n\n\x02NS\x18\t \x01(\x08\"4\n\x03UDP\x12\x13\n\x0bsource_port\x18\x01 \x01(\r\x12\x18\n\x10\x64\x65stination_port\x18\x02 \x01(\r\"5\n\x04SCTP\x12\x13\n\x0bsource_port\x18\x01 \x01(\r\x12\x18\n\x10\x64\x65stination_port\x18\x02 \x01(\r\"$\n\x06ICMPv4\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0c\n\x04\x63ode\x18\x02 \x01(\r\"$\n\x06ICMPv6\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0c\n\x04\x63ode\x18\x02 \x01(\r\"Y\n\x06Policy\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x0e\n\x06labels\x18\x03 \x03(\t\x12\x10\n\x08revision\x18\x04 \x01(\x04\x12\x0c\n\x04kind\x18\x05 \x01(\t\"I\n\x0f\x45ventTypeFilter\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x16\n\x0ematch_sub_type\x18\x02 \x01(\x08\x12\x10\n\x08sub_type\x18\x03 \x01(\x05\"1\n\x0f\x43iliumEventType\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x10\n\x08sub_type\x18\x02 \x01(\x05\"\x81\t\n\nFlowFilter\x12\x0c\n\x04uuid\x18\x1d \x03(\t\x12\x11\n\tsource_ip\x18\x01 \x03(\t\x12\x18\n\x10source_ip_xlated\x18\" \x03(\t\x12\x12\n\nsource_pod\x18\x02 \x03(\t\x12\x13\n\x0bsource_fqdn\x18\x07 \x03(\t\x12\x14\n\x0csource_label\x18\n \x03(\t\x12\x16\n\x0esource_service\x18\x10 \x03(\t\x12\'\n\x0fsource_workload\x18\x1a \x03(\x0b\x32\x0e.flow.Workload\x12\x1b\n\x13source_cluster_name\x18% \x03(\t\x12\x16\n\x0e\x64\x65stination_ip\x18\x03 \x03(\t\x12\x17\n\x0f\x64\x65stination_pod\x18\x04 \x03(\t\x12\x18\n\x10\x64\x65stination_fqdn\x18\x08 \x03(\t\x12\x19\n\x11\x64\x65stination_label\x18\x0b \x03(\t\x12\x1b\n\x13\x64\x65stination_service\x18\x11 \x03(\t\x12,\n\x14\x64\x65stination_workload\x18\x1b \x03(\x0b\x32\x0e.flow.Workload\x12 \n\x18\x64\x65stination_cluster_name\x18& \x03(\t\x12\x31\n\x11traffic_direction\x18\x1e \x03(\x0e\x32\x16.flow.TrafficDirection\x12\x1e\n\x07verdict\x18\x05 \x03(\x0e\x32\r.flow.Verdict\x12*\n\x10\x64rop_reason_desc\x18! \x03(\x0e\x32\x10.flow.DropReason\x12)\n\tinterface\x18# \x03(\x0b\x32\x16.flow.NetworkInterface\x12)\n\nevent_type\x18\x06 \x03(\x0b\x32\x15.flow.EventTypeFilter\x12\x18\n\x10http_status_code\x18\t \x03(\t\x12\x10\n\x08protocol\x18\x0c \x03(\t\x12\x13\n\x0bsource_port\x18\r \x03(\t\x12\x18\n\x10\x64\x65stination_port\x18\x0e \x03(\t\x12\r\n\x05reply\x18\x0f \x03(\x08\x12\x11\n\tdns_query\x18\x12 \x03(\t\x12\x17\n\x0fsource_identity\x18\x13 \x03(\r\x12\x1c\n\x14\x64\x65stination_identity\x18\x14 \x03(\r\x12\x13\n\x0bhttp_method\x18\x15 \x03(\t\x12\x11\n\thttp_path\x18\x16 \x03(\t\x12\x10\n\x08http_url\x18\x1f \x03(\t\x12%\n\x0bhttp_header\x18  \x03(\x0b\x32\x10.flow.HTTPHeader\x12!\n\ttcp_flags\x18\x17 \x03(\x0b\x32\x0e.flow.TCPFlags\x12\x11\n\tnode_name\x18\x18 \x03(\t\x12\x13\n\x0bnode_labels\x18$ \x03(\t\x12#\n\nip_version\x18\x19 \x03(\x0e\x32\x0f.flow.IPVersion\x12\x10\n\x08trace_id\x18\x1c \x03(\t\x12\x34\n\x0c\x65xperimental\x18\xe7\x07 \x01(\x0b\x32\x1d.flow.FlowFilter.Experimental\x1a&\n\x0c\x45xperimental\x12\x16\n\x0e\x63\x65l_expression\x18\x01 \x03(\t\"\x8a\x01\n\x03\x44NS\x12\r\n\x05query\x18\x01 \x01(\t\x12\x0b\n\x03ips\x18\x02 \x03(\t\x12\x0b\n\x03ttl\x18\x03 \x01(\r\x12\x0e\n\x06\x63names\x18\x04 \x03(\t\x12\x1a\n\x12observation_source\x18\x05 \x01(\t\x12\r\n\x05rcode\x18\x06 \x01(\r\x12\x0e\n\x06qtypes\x18\x07 \x03(\t\x12\x0f\n\x07rrtypes\x18\x08 \x03(\t\"(\n\nHTTPHeader\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"f\n\x04HTTP\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x10\n\x08protocol\x18\x04 \x01(\t\x12!\n\x07headers\x18\x05 \x03(\x0b\x32\x10.flow.HTTPHeader\"h\n\x05Kafka\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x13\n\x0b\x61pi_version\x18\x02 \x01(\x05\x12\x0f\n\x07\x61pi_key\x18\x03 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x04 \x01(\x05\x12\r\n\x05topic\x18\x05 \x01(\t\"*\n\x07Service\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\"u\n\tLostEvent\x12%\n\x06source\x18\x01 \x01(\x0e\x32\x15.flow.LostEventSource\x12\x17\n\x0fnum_events_lost\x18\x02 \x01(\x04\x12(\n\x03\x63pu\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\"\xfc\x03\n\nAgentEvent\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.flow.AgentEventType\x12*\n\x07unknown\x18\x64 \x01(\x0b\x32\x17.flow.AgentEventUnknownH\x00\x12-\n\x0b\x61gent_start\x18\x65 \x01(\x0b\x32\x16.flow.TimeNotificationH\x00\x12\x37\n\rpolicy_update\x18\x66 \x01(\x0b\x32\x1e.flow.PolicyUpdateNotificationH\x00\x12>\n\x13\x65ndpoint_regenerate\x18g \x01(\x0b\x32\x1f.flow.EndpointRegenNotificationH\x00\x12;\n\x0f\x65ndpoint_update\x18h \x01(\x0b\x32 .flow.EndpointUpdateNotificationH\x00\x12\x33\n\x0eipcache_update\x18i \x01(\x0b\x32\x19.flow.IPCacheNotificationH\x00\x12\x39\n\x0eservice_upsert\x18j \x01(\x0b\x32\x1f.flow.ServiceUpsertNotificationH\x00\x12\x39\n\x0eservice_delete\x18k \x01(\x0b\x32\x1f.flow.ServiceDeleteNotificationH\x00\x42\x0e\n\x0cnotification\"7\n\x11\x41gentEventUnknown\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x0cnotification\x18\x02 \x01(\t\"<\n\x10TimeNotification\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"P\n\x18PolicyUpdateNotification\x12\x0e\n\x06labels\x18\x01 \x03(\t\x12\x10\n\x08revision\x18\x02 \x01(\x04\x12\x12\n\nrule_count\x18\x03 \x01(\x03\"F\n\x19\x45ndpointRegenNotification\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06labels\x18\x02 \x03(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"l\n\x1a\x45ndpointUpdateNotification\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06labels\x18\x02 \x03(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x10\n\x08pod_name\x18\x04 \x01(\t\x12\x11\n\tnamespace\x18\x05 \x01(\t\"\xc9\x01\n\x13IPCacheNotification\x12\x0c\n\x04\x63idr\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\r\x12\x32\n\x0cold_identity\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x0f\n\x07host_ip\x18\x04 \x01(\t\x12\x13\n\x0bold_host_ip\x18\x05 \x01(\t\x12\x13\n\x0b\x65ncrypt_key\x18\x06 \x01(\r\x12\x11\n\tnamespace\x18\x07 \x01(\t\x12\x10\n\x08pod_name\x18\x08 \x01(\t\"9\n\x1dServiceUpsertNotificationAddr\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\"\xa9\x02\n\x19ServiceUpsertNotification\x12\n\n\x02id\x18\x01 \x01(\r\x12=\n\x10\x66rontend_address\x18\x02 \x01(\x0b\x32#.flow.ServiceUpsertNotificationAddr\x12>\n\x11\x62\x61\x63kend_addresses\x18\x03 \x03(\x0b\x32#.flow.ServiceUpsertNotificationAddr\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x1a\n\x0etraffic_policy\x18\x05 \x01(\tB\x02\x18\x01\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x11\n\tnamespace\x18\x07 \x01(\t\x12\x1a\n\x12\x65xt_traffic_policy\x18\x08 \x01(\t\x12\x1a\n\x12int_traffic_policy\x18\t \x01(\t\"\'\n\x19ServiceDeleteNotification\x12\n\n\x02id\x18\x01 \x01(\r\"/\n\x10NetworkInterface\x12\r\n\x05index\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xbb\x02\n\nDebugEvent\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.flow.DebugEventType\x12\x1e\n\x06source\x18\x02 \x01(\x0b\x32\x0e.flow.Endpoint\x12*\n\x04hash\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12*\n\x04\x61rg1\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12*\n\x04\x61rg2\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12*\n\x04\x61rg3\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x0f\n\x07message\x18\x07 \x01(\t\x12(\n\x03\x63pu\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int32Value*9\n\x08\x46lowType\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\t\n\x05L3_L4\x10\x01\x12\x06\n\x02L7\x10\x02\x12\x08\n\x04SOCK\x10\x03*9\n\x08\x41uthType\x12\x0c\n\x08\x44ISABLED\x10\x00\x12\t\n\x05SPIRE\x10\x01\x12\x14\n\x10TEST_ALWAYS_FAIL\x10\x02*\x8a\x02\n\x15TraceObservationPoint\x12\x11\n\rUNKNOWN_POINT\x10\x00\x12\x0c\n\x08TO_PROXY\x10\x01\x12\x0b\n\x07TO_HOST\x10\x02\x12\x0c\n\x08TO_STACK\x10\x03\x12\x0e\n\nTO_OVERLAY\x10\x04\x12\x0f\n\x0bTO_ENDPOINT\x10\x65\x12\x11\n\rFROM_ENDPOINT\x10\x05\x12\x0e\n\nFROM_PROXY\x10\x06\x12\r\n\tFROM_HOST\x10\x07\x12\x0e\n\nFROM_STACK\x10\x08\x12\x10\n\x0c\x46ROM_OVERLAY\x10\t\x12\x10\n\x0c\x46ROM_NETWORK\x10\n\x12\x0e\n\nTO_NETWORK\x10\x0b\x12\x0f\n\x0b\x46ROM_CRYPTO\x10\x0c\x12\r\n\tTO_CRYPTO\x10\r*\xa0\x01\n\x0bTraceReason\x12\x18\n\x14TRACE_REASON_UNKNOWN\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\x0f\n\x0b\x45STABLISHED\x10\x02\x12\t\n\x05REPLY\x10\x03\x12\x0b\n\x07RELATED\x10\x04\x12\x10\n\x08REOPENED\x10\x05\x1a\x02\x08\x01\x12\x0e\n\nSRV6_ENCAP\x10\x06\x12\x0e\n\nSRV6_DECAP\x10\x07\x12\x13\n\x0f\x45NCRYPT_OVERLAY\x10\x08*H\n\nL7FlowType\x12\x13\n\x0fUNKNOWN_L7_TYPE\x10\x00\x12\x0b\n\x07REQUEST\x10\x01\x12\x0c\n\x08RESPONSE\x10\x02\x12\n\n\x06SAMPLE\x10\x03*0\n\tIPVersion\x12\x0f\n\x0bIP_NOT_USED\x10\x00\x12\x08\n\x04IPv4\x10\x01\x12\x08\n\x04IPv6\x10\x02*|\n\x07Verdict\x12\x13\n\x0fVERDICT_UNKNOWN\x10\x00\x12\r\n\tFORWARDED\x10\x01\x12\x0b\n\x07\x44ROPPED\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\t\n\x05\x41UDIT\x10\x04\x12\x0e\n\nREDIRECTED\x10\x05\x12\n\n\x06TRACED\x10\x06\x12\x0e\n\nTRANSLATED\x10\x07*\xc5\x11\n\nDropReason\x12\x17\n\x13\x44ROP_REASON_UNKNOWN\x10\x00\x12\x1b\n\x12INVALID_SOURCE_MAC\x10\x82\x01\x1a\x02\x08\x01\x12 \n\x17INVALID_DESTINATION_MAC\x10\x83\x01\x1a\x02\x08\x01\x12\x16\n\x11INVALID_SOURCE_IP\x10\x84\x01\x12\x12\n\rPOLICY_DENIED\x10\x85\x01\x12\x1b\n\x16INVALID_PACKET_DROPPED\x10\x86\x01\x12#\n\x1e\x43T_TRUNCATED_OR_INVALID_HEADER\x10\x87\x01\x12\x1c\n\x17\x43T_MISSING_TCP_ACK_FLAG\x10\x88\x01\x12\x1b\n\x16\x43T_UNKNOWN_L4_PROTOCOL\x10\x89\x01\x12+\n\"CT_CANNOT_CREATE_ENTRY_FROM_PACKET\x10\x8a\x01\x1a\x02\x08\x01\x12\x1c\n\x17UNSUPPORTED_L3_PROTOCOL\x10\x8b\x01\x12\x15\n\x10MISSED_TAIL_CALL\x10\x8c\x01\x12\x1c\n\x17\x45RROR_WRITING_TO_PACKET\x10\x8d\x01\x12\x18\n\x13UNKNOWN_L4_PROTOCOL\x10\x8e\x01\x12\x18\n\x13UNKNOWN_ICMPV4_CODE\x10\x8f\x01\x12\x18\n\x13UNKNOWN_ICMPV4_TYPE\x10\x90\x01\x12\x18\n\x13UNKNOWN_ICMPV6_CODE\x10\x91\x01\x12\x18\n\x13UNKNOWN_ICMPV6_TYPE\x10\x92\x01\x12 \n\x1b\x45RROR_RETRIEVING_TUNNEL_KEY\x10\x93\x01\x12(\n\x1f\x45RROR_RETRIEVING_TUNNEL_OPTIONS\x10\x94\x01\x1a\x02\x08\x01\x12\x1e\n\x15INVALID_GENEVE_OPTION\x10\x95\x01\x1a\x02\x08\x01\x12\x1e\n\x19UNKNOWN_L3_TARGET_ADDRESS\x10\x96\x01\x12\x1b\n\x16STALE_OR_UNROUTABLE_IP\x10\x97\x01\x12*\n!NO_MATCHING_LOCAL_CONTAINER_FOUND\x10\x98\x01\x1a\x02\x08\x01\x12\'\n\"ERROR_WHILE_CORRECTING_L3_CHECKSUM\x10\x99\x01\x12\'\n\"ERROR_WHILE_CORRECTING_L4_CHECKSUM\x10\x9a\x01\x12\x1c\n\x17\x43T_MAP_INSERTION_FAILED\x10\x9b\x01\x12\"\n\x1dINVALID_IPV6_EXTENSION_HEADER\x10\x9c\x01\x12#\n\x1eIP_FRAGMENTATION_NOT_SUPPORTED\x10\x9d\x01\x12\x1e\n\x19SERVICE_BACKEND_NOT_FOUND\x10\x9e\x01\x12(\n#NO_TUNNEL_OR_ENCAPSULATION_ENDPOINT\x10\xa0\x01\x12#\n\x1e\x46\x41ILED_TO_INSERT_INTO_PROXYMAP\x10\xa1\x01\x12+\n&REACHED_EDT_RATE_LIMITING_DROP_HORIZON\x10\xa2\x01\x12&\n!UNKNOWN_CONNECTION_TRACKING_STATE\x10\xa3\x01\x12\x1e\n\x19LOCAL_HOST_IS_UNREACHABLE\x10\xa4\x01\x12:\n5NO_CONFIGURATION_AVAILABLE_TO_PERFORM_POLICY_DECISION\x10\xa5\x01\x12\x1c\n\x17UNSUPPORTED_L2_PROTOCOL\x10\xa6\x01\x12\"\n\x1dNO_MAPPING_FOR_NAT_MASQUERADE\x10\xa7\x01\x12,\n\'UNSUPPORTED_PROTOCOL_FOR_NAT_MASQUERADE\x10\xa8\x01\x12\x16\n\x11\x46IB_LOOKUP_FAILED\x10\xa9\x01\x12(\n#ENCAPSULATION_TRAFFIC_IS_PROHIBITED\x10\xaa\x01\x12\x15\n\x10INVALID_IDENTITY\x10\xab\x01\x12\x13\n\x0eUNKNOWN_SENDER\x10\xac\x01\x12\x13\n\x0eNAT_NOT_NEEDED\x10\xad\x01\x12\x13\n\x0eIS_A_CLUSTERIP\x10\xae\x01\x12.\n)FIRST_LOGICAL_DATAGRAM_FRAGMENT_NOT_FOUND\x10\xaf\x01\x12\x1d\n\x18\x46ORBIDDEN_ICMPV6_MESSAGE\x10\xb0\x01\x12!\n\x1c\x44\x45NIED_BY_LB_SRC_RANGE_CHECK\x10\xb1\x01\x12\x19\n\x14SOCKET_LOOKUP_FAILED\x10\xb2\x01\x12\x19\n\x14SOCKET_ASSIGN_FAILED\x10\xb3\x01\x12\x31\n,PROXY_REDIRECTION_NOT_SUPPORTED_FOR_PROTOCOL\x10\xb4\x01\x12\x10\n\x0bPOLICY_DENY\x10\xb5\x01\x12\x12\n\rVLAN_FILTERED\x10\xb6\x01\x12\x10\n\x0bINVALID_VNI\x10\xb7\x01\x12\x16\n\x11INVALID_TC_BUFFER\x10\xb8\x01\x12\x0b\n\x06NO_SID\x10\xb9\x01\x12\x1b\n\x12MISSING_SRV6_STATE\x10\xba\x01\x1a\x02\x08\x01\x12\n\n\x05NAT46\x10\xbb\x01\x12\n\n\x05NAT64\x10\xbc\x01\x12\x12\n\rAUTH_REQUIRED\x10\xbd\x01\x12\x14\n\x0f\x43T_NO_MAP_FOUND\x10\xbe\x01\x12\x16\n\x11SNAT_NO_MAP_FOUND\x10\xbf\x01\x12\x17\n\x12INVALID_CLUSTER_ID\x10\xc0\x01\x12\'\n\"UNSUPPORTED_PROTOCOL_FOR_DSR_ENCAP\x10\xc1\x01\x12\x16\n\x11NO_EGRESS_GATEWAY\x10\xc2\x01\x12\x18\n\x13UNENCRYPTED_TRAFFIC\x10\xc3\x01\x12\x11\n\x0cTTL_EXCEEDED\x10\xc4\x01\x12\x0f\n\nNO_NODE_ID\x10\xc5\x01\x12\x16\n\x11\x44ROP_RATE_LIMITED\x10\xc6\x01\x12\x11\n\x0cIGMP_HANDLED\x10\xc7\x01\x12\x14\n\x0fIGMP_SUBSCRIBED\x10\xc8\x01\x12\x16\n\x11MULTICAST_HANDLED\x10\xc9\x01\x12\x18\n\x13\x44ROP_HOST_NOT_READY\x10\xca\x01\x12\x16\n\x11\x44ROP_EP_NOT_READY\x10\xcb\x01\x12\x16\n\x11\x44ROP_NO_EGRESS_IP\x10\xcc\x01\x12\x14\n\x0f\x44ROP_PUNT_PROXY\x10\xcd\x01*J\n\x10TrafficDirection\x12\x1d\n\x19TRAFFIC_DIRECTION_UNKNOWN\x10\x00\x12\x0b\n\x07INGRESS\x10\x01\x12\n\n\x06\x45GRESS\x10\x02*\x8d\x02\n\x11\x44\x65\x62ugCapturePoint\x12\x1d\n\x19\x44\x42G_CAPTURE_POINT_UNKNOWN\x10\x00\x12\x18\n\x14\x44\x42G_CAPTURE_DELIVERY\x10\x04\x12\x17\n\x13\x44\x42G_CAPTURE_FROM_LB\x10\x05\x12\x19\n\x15\x44\x42G_CAPTURE_AFTER_V46\x10\x06\x12\x19\n\x15\x44\x42G_CAPTURE_AFTER_V64\x10\x07\x12\x19\n\x15\x44\x42G_CAPTURE_PROXY_PRE\x10\x08\x12\x1a\n\x16\x44\x42G_CAPTURE_PROXY_POST\x10\t\x12\x18\n\x14\x44\x42G_CAPTURE_SNAT_PRE\x10\n\x12\x19\n\x15\x44\x42G_CAPTURE_SNAT_POST\x10\x0b\"\x04\x08\x01\x10\x03*9\n\tEventType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0b\x45ventSample\x10\t\x12\x0e\n\nRecordLost\x10\x02*\x7f\n\x0fLostEventSource\x12\x1d\n\x19UNKNOWN_LOST_EVENT_SOURCE\x10\x00\x12\x1a\n\x16PERF_EVENT_RING_BUFFER\x10\x01\x12\x19\n\x15OBSERVER_EVENTS_QUEUE\x10\x02\x12\x16\n\x12HUBBLE_RING_BUFFER\x10\x03*\xae\x02\n\x0e\x41gentEventType\x12\x17\n\x13\x41GENT_EVENT_UNKNOWN\x10\x00\x12\x11\n\rAGENT_STARTED\x10\x02\x12\x12\n\x0ePOLICY_UPDATED\x10\x03\x12\x12\n\x0ePOLICY_DELETED\x10\x04\x12\x1f\n\x1b\x45NDPOINT_REGENERATE_SUCCESS\x10\x05\x12\x1f\n\x1b\x45NDPOINT_REGENERATE_FAILURE\x10\x06\x12\x14\n\x10\x45NDPOINT_CREATED\x10\x07\x12\x14\n\x10\x45NDPOINT_DELETED\x10\x08\x12\x14\n\x10IPCACHE_UPSERTED\x10\t\x12\x13\n\x0fIPCACHE_DELETED\x10\n\x12\x14\n\x10SERVICE_UPSERTED\x10\x0b\x12\x13\n\x0fSERVICE_DELETED\x10\x0c\"\x04\x08\x01\x10\x01*\xd8\x01\n\x16SocketTranslationPoint\x12\x1c\n\x18SOCK_XLATE_POINT_UNKNOWN\x10\x00\x12&\n\"SOCK_XLATE_POINT_PRE_DIRECTION_FWD\x10\x01\x12\'\n#SOCK_XLATE_POINT_POST_DIRECTION_FWD\x10\x02\x12&\n\"SOCK_XLATE_POINT_PRE_DIRECTION_REV\x10\x03\x12\'\n#SOCK_XLATE_POINT_POST_DIRECTION_REV\x10\x04*\x81\r\n\x0e\x44\x65\x62ugEventType\x12\x15\n\x11\x44\x42G_EVENT_UNKNOWN\x10\x00\x12\x0f\n\x0b\x44\x42G_GENERIC\x10\x01\x12\x16\n\x12\x44\x42G_LOCAL_DELIVERY\x10\x02\x12\r\n\tDBG_ENCAP\x10\x03\x12\x11\n\rDBG_LXC_FOUND\x10\x04\x12\x15\n\x11\x44\x42G_POLICY_DENIED\x10\x05\x12\x11\n\rDBG_CT_LOOKUP\x10\x06\x12\x15\n\x11\x44\x42G_CT_LOOKUP_REV\x10\x07\x12\x10\n\x0c\x44\x42G_CT_MATCH\x10\x08\x12\x12\n\x0e\x44\x42G_CT_CREATED\x10\t\x12\x13\n\x0f\x44\x42G_CT_CREATED2\x10\n\x12\x14\n\x10\x44\x42G_ICMP6_HANDLE\x10\x0b\x12\x15\n\x11\x44\x42G_ICMP6_REQUEST\x10\x0c\x12\x10\n\x0c\x44\x42G_ICMP6_NS\x10\r\x12\x1b\n\x17\x44\x42G_ICMP6_TIME_EXCEEDED\x10\x0e\x12\x12\n\x0e\x44\x42G_CT_VERDICT\x10\x0f\x12\r\n\tDBG_DECAP\x10\x10\x12\x10\n\x0c\x44\x42G_PORT_MAP\x10\x11\x12\x11\n\rDBG_ERROR_RET\x10\x12\x12\x0f\n\x0b\x44\x42G_TO_HOST\x10\x13\x12\x10\n\x0c\x44\x42G_TO_STACK\x10\x14\x12\x10\n\x0c\x44\x42G_PKT_HASH\x10\x15\x12\x1b\n\x17\x44\x42G_LB6_LOOKUP_FRONTEND\x10\x16\x12 \n\x1c\x44\x42G_LB6_LOOKUP_FRONTEND_FAIL\x10\x17\x12\x1f\n\x1b\x44\x42G_LB6_LOOKUP_BACKEND_SLOT\x10\x18\x12\'\n#DBG_LB6_LOOKUP_BACKEND_SLOT_SUCCESS\x10\x19\x12\'\n#DBG_LB6_LOOKUP_BACKEND_SLOT_V2_FAIL\x10\x1a\x12\x1f\n\x1b\x44\x42G_LB6_LOOKUP_BACKEND_FAIL\x10\x1b\x12\x1e\n\x1a\x44\x42G_LB6_REVERSE_NAT_LOOKUP\x10\x1c\x12\x17\n\x13\x44\x42G_LB6_REVERSE_NAT\x10\x1d\x12\x1b\n\x17\x44\x42G_LB4_LOOKUP_FRONTEND\x10\x1e\x12 \n\x1c\x44\x42G_LB4_LOOKUP_FRONTEND_FAIL\x10\x1f\x12\x1f\n\x1b\x44\x42G_LB4_LOOKUP_BACKEND_SLOT\x10 \x12\'\n#DBG_LB4_LOOKUP_BACKEND_SLOT_SUCCESS\x10!\x12\'\n#DBG_LB4_LOOKUP_BACKEND_SLOT_V2_FAIL\x10\"\x12\x1f\n\x1b\x44\x42G_LB4_LOOKUP_BACKEND_FAIL\x10#\x12\x1e\n\x1a\x44\x42G_LB4_REVERSE_NAT_LOOKUP\x10$\x12\x17\n\x13\x44\x42G_LB4_REVERSE_NAT\x10%\x12\x19\n\x15\x44\x42G_LB4_LOOPBACK_SNAT\x10&\x12\x1d\n\x19\x44\x42G_LB4_LOOPBACK_SNAT_REV\x10\'\x12\x12\n\x0e\x44\x42G_CT_LOOKUP4\x10(\x12\x1b\n\x17\x44\x42G_RR_BACKEND_SLOT_SEL\x10)\x12\x18\n\x14\x44\x42G_REV_PROXY_LOOKUP\x10*\x12\x17\n\x13\x44\x42G_REV_PROXY_FOUND\x10+\x12\x18\n\x14\x44\x42G_REV_PROXY_UPDATE\x10,\x12\x11\n\rDBG_L4_POLICY\x10-\x12\x19\n\x15\x44\x42G_NETDEV_IN_CLUSTER\x10.\x12\x15\n\x11\x44\x42G_NETDEV_ENCAP4\x10/\x12\x14\n\x10\x44\x42G_CT_LOOKUP4_1\x10\x30\x12\x14\n\x10\x44\x42G_CT_LOOKUP4_2\x10\x31\x12\x13\n\x0f\x44\x42G_CT_CREATED4\x10\x32\x12\x14\n\x10\x44\x42G_CT_LOOKUP6_1\x10\x33\x12\x14\n\x10\x44\x42G_CT_LOOKUP6_2\x10\x34\x12\x13\n\x0f\x44\x42G_CT_CREATED6\x10\x35\x12\x12\n\x0e\x44\x42G_SKIP_PROXY\x10\x36\x12\x11\n\rDBG_L4_CREATE\x10\x37\x12\x19\n\x15\x44\x42G_IP_ID_MAP_FAILED4\x10\x38\x12\x19\n\x15\x44\x42G_IP_ID_MAP_FAILED6\x10\x39\x12\x1a\n\x16\x44\x42G_IP_ID_MAP_SUCCEED4\x10:\x12\x1a\n\x16\x44\x42G_IP_ID_MAP_SUCCEED6\x10;\x12\x13\n\x0f\x44\x42G_LB_STALE_CT\x10<\x12\x18\n\x14\x44\x42G_INHERIT_IDENTITY\x10=\x12\x12\n\x0e\x44\x42G_SK_LOOKUP4\x10>\x12\x12\n\x0e\x44\x42G_SK_LOOKUP6\x10?\x12\x11\n\rDBG_SK_ASSIGN\x10@\x12\r\n\tDBG_L7_LB\x10\x41\x12\x13\n\x0f\x44\x42G_SKIP_POLICY\x10\x42\x42&Z$github.com/cilium/cilium/api/v1/flowb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flow.flow_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/cilium/cilium/api/v1/flow'
  _globals['_TRACEREASON'].values_by_name["REOPENED"]._loaded_options = None
  _globals['_TRACEREASON'].values_by_name["REOPENED"]._serialized_options = b'\010\001'
  _globals['_DROPREASON'].values_by_name["INVALID_SOURCE_MAC"]._loaded_options = None
  _globals['_DROPREASON'].values_by_name["INVALID_SOURCE_MAC"]._serialized_options = b'\010\001'
  _globals['_DROPREASON'].values_by_name["INVALID_DESTINATION_MAC"]._loaded_options = None
  _globals['_DROPREASON'].values_by_name["INVALID_DESTINATION_MAC"]._serialized_options = b'\010\001'
  _globals['_DROPREASON'].values_by_name["CT_CANNOT_CREATE_ENTRY_FROM_PACKET"]._loaded_options = None
  _globals['_DROPREASON'].values_by_name["CT_CANNOT_CREATE_ENTRY_FROM_PACKET"]._serialized_options = b'\010\001'
  _globals['_DROPREASON'].values_by_name["ERROR_RETRIEVING_TUNNEL_OPTIONS"]._loaded_options = None
  _globals['_DROPREASON'].values_by_name["ERROR_RETRIEVING_TUNNEL_OPTIONS"]._serialized_options = b'\010\001'
  _globals['_DROPREASON'].values_by_name["INVALID_GENEVE_OPTION"]._loaded_options = None
  _globals['_DROPREASON'].values_by_name["INVALID_GENEVE_OPTION"]._serialized_options = b'\010\001'
  _globals['_DROPREASON'].values_by_name["NO_MATCHING_LOCAL_CONTAINER_FOUND"]._loaded_options = None
  _globals['_DROPREASON'].values_by_name["NO_MATCHING_LOCAL_CONTAINER_FOUND"]._serialized_options = b'\010\001'
  _globals['_DROPREASON'].values_by_name["MISSING_SRV6_STATE"]._loaded_options = None
  _globals['_DROPREASON'].values_by_name["MISSING_SRV6_STATE"]._serialized_options = b'\010\001'
  _globals['_FLOW'].fields_by_name['drop_reason']._loaded_options = None
  _globals['_FLOW'].fields_by_name['drop_reason']._serialized_options = b'\030\001'
  _globals['_FLOW'].fields_by_name['reply']._loaded_options = None
  _globals['_FLOW'].fields_by_name['reply']._serialized_options = b'\030\001'
  _globals['_FLOW'].fields_by_name['Summary']._loaded_options = None
  _globals['_FLOW'].fields_by_name['Summary']._serialized_options = b'\030\001'
  _globals['_SERVICEUPSERTNOTIFICATION'].fields_by_name['traffic_policy']._loaded_options = None
  _globals['_SERVICEUPSERTNOTIFICATION'].fields_by_name['traffic_policy']._serialized_options = b'\030\001'
  _globals['_FLOWTYPE']._serialized_start=6540
  _globals['_FLOWTYPE']._serialized_end=6597
  _globals['_AUTHTYPE']._serialized_start=6599
  _globals['_AUTHTYPE']._serialized_end=6656
  _globals['_TRACEOBSERVATIONPOINT']._serialized_start=6659
  _globals['_TRACEOBSERVATIONPOINT']._serialized_end=6925
  _globals['_TRACEREASON']._serialized_start=6928
  _globals['_TRACEREASON']._serialized_end=7088
  _globals['_L7FLOWTYPE']._serialized_start=7090
  _globals['_L7FLOWTYPE']._serialized_end=7162
  _globals['_IPVERSION']._serialized_start=7164
  _globals['_IPVERSION']._serialized_end=7212
  _globals['_VERDICT']._serialized_start=7214
  _globals['_VERDICT']._serialized_end=7338
  _globals['_DROPREASON']._serialized_start=7341
  _globals['_DROPREASON']._serialized_end=9586
  _globals['_TRAFFICDIRECTION']._serialized_start=9588
  _globals['_TRAFFICDIRECTION']._serialized_end=9662
  _globals['_DEBUGCAPTUREPOINT']._serialized_start=9665
  _globals['_DEBUGCAPTUREPOINT']._serialized_end=9934
  _globals['_EVENTTYPE']._serialized_start=9936
  _globals['_EVENTTYPE']._serialized_end=9993
  _globals['_LOSTEVENTSOURCE']._serialized_start=9995
  _globals['_LOSTEVENTSOURCE']._serialized_end=10122
  _globals['_AGENTEVENTTYPE']._serialized_start=10125
  _globals['_AGENTEVENTTYPE']._serialized_end=10427
  _globals['_SOCKETTRANSLATIONPOINT']._serialized_start=10430
  _globals['_SOCKETTRANSLATIONPOINT']._serialized_end=10646
  _globals['_DEBUGEVENTTYPE']._serialized_start=10649
  _globals['_DEBUGEVENTTYPE']._serialized_end=12314
  _globals['_FLOW']._serialized_start=118
  _globals['_FLOW']._serialized_end=1535
  _globals['_FILEINFO']._serialized_start=1537
  _globals['_FILEINFO']._serialized_end=1575
  _globals['_LAYER4']._serialized_start=1578
  _globals['_LAYER4']._serialized_end=1742
  _globals['_LAYER7']._serialized_start=1745
  _globals['_LAYER7']._serialized_end=1899
  _globals['_TRACECONTEXT']._serialized_start=1901
  _globals['_TRACECONTEXT']._serialized_end=1950
  _globals['_TRACEPARENT']._serialized_start=1952
  _globals['_TRACEPARENT']._serialized_end=1983
  _globals['_ENDPOINT']._serialized_start=1986
  _globals['_ENDPOINT']._serialized_end=2136
  _globals['_WORKLOAD']._serialized_start=2138
  _globals['_WORKLOAD']._serialized_end=2176
  _globals['_TCP']._serialized_start=2178
  _globals['_TCP']._serialized_end=2261
  _globals['_IP']._serialized_start=2263
  _globals['_IP']._serialized_end=2382
  _globals['_ETHERNET']._serialized_start=2384
  _globals['_ETHERNET']._serialized_end=2431
  _globals['_TCPFLAGS']._serialized_start=2433
  _globals['_TCPFLAGS']._serialized_end=2559
  _globals['_UDP']._serialized_start=2561
  _globals['_UDP']._serialized_end=2613
  _globals['_SCTP']._serialized_start=2615
  _globals['_SCTP']._serialized_end=2668
  _globals['_ICMPV4']._serialized_start=2670
  _globals['_ICMPV4']._serialized_end=2706
  _globals['_ICMPV6']._serialized_start=2708
  _globals['_ICMPV6']._serialized_end=2744
  _globals['_POLICY']._serialized_start=2746
  _globals['_POLICY']._serialized_end=2835
  _globals['_EVENTTYPEFILTER']._serialized_start=2837
  _globals['_EVENTTYPEFILTER']._serialized_end=2910
  _globals['_CILIUMEVENTTYPE']._serialized_start=2912
  _globals['_CILIUMEVENTTYPE']._serialized_end=2961
  _globals['_FLOWFILTER']._serialized_start=2964
  _globals['_FLOWFILTER']._serialized_end=4117
  _globals['_FLOWFILTER_EXPERIMENTAL']._serialized_start=4079
  _globals['_FLOWFILTER_EXPERIMENTAL']._serialized_end=4117
  _globals['_DNS']._serialized_start=4120
  _globals['_DNS']._serialized_end=4258
  _globals['_HTTPHEADER']._serialized_start=4260
  _globals['_HTTPHEADER']._serialized_end=4300
  _globals['_HTTP']._serialized_start=4302
  _globals['_HTTP']._serialized_end=4404
  _globals['_KAFKA']._serialized_start=4406
  _globals['_KAFKA']._serialized_end=4510
  _globals['_SERVICE']._serialized_start=4512
  _globals['_SERVICE']._serialized_end=4554
  _globals['_LOSTEVENT']._serialized_start=4556
  _globals['_LOSTEVENT']._serialized_end=4673
  _globals['_AGENTEVENT']._serialized_start=4676
  _globals['_AGENTEVENT']._serialized_end=5184
  _globals['_AGENTEVENTUNKNOWN']._serialized_start=5186
  _globals['_AGENTEVENTUNKNOWN']._serialized_end=5241
  _globals['_TIMENOTIFICATION']._serialized_start=5243
  _globals['_TIMENOTIFICATION']._serialized_end=5303
  _globals['_POLICYUPDATENOTIFICATION']._serialized_start=5305
  _globals['_POLICYUPDATENOTIFICATION']._serialized_end=5385
  _globals['_ENDPOINTREGENNOTIFICATION']._serialized_start=5387
  _globals['_ENDPOINTREGENNOTIFICATION']._serialized_end=5457
  _globals['_ENDPOINTUPDATENOTIFICATION']._serialized_start=5459
  _globals['_ENDPOINTUPDATENOTIFICATION']._serialized_end=5567
  _globals['_IPCACHENOTIFICATION']._serialized_start=5570
  _globals['_IPCACHENOTIFICATION']._serialized_end=5771
  _globals['_SERVICEUPSERTNOTIFICATIONADDR']._serialized_start=5773
  _globals['_SERVICEUPSERTNOTIFICATIONADDR']._serialized_end=5830
  _globals['_SERVICEUPSERTNOTIFICATION']._serialized_start=5833
  _globals['_SERVICEUPSERTNOTIFICATION']._serialized_end=6130
  _globals['_SERVICEDELETENOTIFICATION']._serialized_start=6132
  _globals['_SERVICEDELETENOTIFICATION']._serialized_end=6171
  _globals['_NETWORKINTERFACE']._serialized_start=6173
  _globals['_NETWORKINTERFACE']._serialized_end=6220
  _globals['_DEBUGEVENT']._serialized_start=6223
  _globals['_DEBUGEVENT']._serialized_end=6538
# @@protoc_insertion_point(module_scope)
