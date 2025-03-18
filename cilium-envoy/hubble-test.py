#! /usr/bin/env python3

import grpc
from observer_pb2 import GetFlowsRequest
from observer_pb2_grpc import ObserverStub
import flow.flow_pb2 as flow_pb2  # 패키지 유지
import relay.relay_pb2 as relay_pb2
import relay.relay_pb2_grpc as relay_pb2_grpc

# Hubble gRPC 서버 주소
HUBBLE_SERVER = "localhost:50051"

def get_flows():
    channel = grpc.insecure_channel(HUBBLE_SERVER)
    stub = ObserverStub(channel)

    request = GetFlowsRequest(number=5)
    response = stub.GetFlows(request)

    for flow in response.flows:
        print("Flow ID:", flow.flow_id)
        if flow.trace_context:
            trace_ctx = flow.trace_context
            print("Trace ID:", trace_ctx.trace_id)
            print("Span ID:", trace_ctx.span_id)

def get_relay_status():
    channel = grpc.insecure_channel(HUBBLE_SERVER)
    stub = relay_pb2_grpc.RelayStub(channel)  # Relay API Stub

    request = relay_pb2.GetStatusRequest()
    response = stub.GetStatus(request)

    print("Relay Status:", response)

if __name__ == "__main__":
    get_flows()
    get_relay_status()
