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
