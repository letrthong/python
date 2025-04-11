#gRPC 

pip install grpcio grpcio-tools
example.proto:


syntax = "proto3";

service ExampleService {
  rpc SayHello (HelloRequest) returns (HelloResponse);
}

message HelloRequest {
  string name = 1;
}

message HelloResponse {
  string message = 1;
}


python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. example.proto

server.py

import grpc
from concurrent import futures
import example_pb2_grpc
import example_pb2

class ExampleServiceServicer(example_pb2_grpc.ExampleServiceServicer):
    def SayHello(self, request, context):
        return example_pb2.HelloResponse(message=f'Hello, {request.name}!')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

 client.py

import grpc
import example_pb2_grpc
import example_pb2

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = example_pb2_grpc.ExampleServiceStub(channel)
        response = stub.SayHello(example_pb2.HelloRequest(name='World'))
    print(f'Client received: {response.message}')

if __name__ == '__main__':
    run()
