import grpc
from concurrent import futures
import time
import logging

# proto 파일을 컴파일하여 생성된 모듈을 임포트합니다.
import external_auth_pb2
import external_auth_pb2_grpc

from google.protobuf import struct_pb2

# 로그 설정: INFO 레벨로 출력
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Authorization 서비스의 Servicer 구현 (모든 요청을 승인하며, 요청 로그를 출력합니다)
class AuthorizationServicer(external_auth_pb2_grpc.AuthorizationServicer):
    def Check(self, request, context):
        # 요청에서 전달된 데이터를 로그에 출력합니다.
        logging.info("Received CheckRequest with attributes: %s", request.attributes)
        
        # 모든 요청을 승인하는 응답 생성 (빈 헤더 포함)
        ok_response = external_auth_pb2.OkResponse(headers=struct_pb2.Struct())
        return external_auth_pb2.CheckResponse(ok_response=ok_response)

def serve():
    # 최대 10개의 쓰레드를 사용하는 gRPC 서버 생성
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    external_auth_pb2_grpc.add_AuthorizationServicer_to_server(AuthorizationServicer(), server)
    
    # 서버가 50051 포트에서 수신하도록 설정
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("gRPC 서버가 포트 50051에서 시작되었습니다.")
    
    try:
        while True:
            time.sleep(86400)  # 서버를 지속적으로 실행 (하루 단위)
    except KeyboardInterrupt:
        server.stop(0)
        logging.info("서버가 종료되었습니다.")

if __name__ == '__main__':
    serve()

