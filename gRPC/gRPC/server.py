import grpc
from concurrent import futures
import example_pb2_grpc
import example_pb2

import time



class ExampleServiceServicer(example_pb2_grpc.ExampleServiceServicer):
    def SayHello(self, request, context):
        epoch_time = int(time.time())
        return example_pb2.HelloResponse(message=f'Hello, {request.name}! at {epoch_time}')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
