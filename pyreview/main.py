import sys

import grpc
from datetime import datetime
from concurrent import futures
from generated import review_pb2_grpc

from generated.review_pb2 import MyResponse, MyReview, Rating


class MyReviewServicer(review_pb2_grpc.ReviewServicer):
    def ProcessReview(self, request: MyReview, context) -> MyResponse:
        print('Review received:')
        print(
            f'{request.userid=}\n{request.timestamp=}\n{request.message=}\n{request.rating=}\n'
        )
        print('Sending response: saved="False"')
        return MyResponse(saved=False)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    review_pb2_grpc.add_ReviewServicer_to_server(MyReviewServicer(), server)
    server.add_insecure_port('localhost:50051')
    print('Starting server...')
    server.start()
    server.wait_for_termination()


def send():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = review_pb2_grpc.ReviewStub(channel)
        my_review = MyReview(
            userid=1234,
            timestamp=int(datetime.now().timestamp()),
            message='Juan Wuz Here',
            rating=Rating.BOGUS,
        )
        response: 'MyResponse' = stub.ProcessReview(my_review)
        print(f'Review processed: {response.saved=}')


if __name__ == '__main__':
    args = sys.argv[1:]
    if args[0] == 'recv':
        serve()
    elif args[0] == 'send':
        send()
    else:
        print('Usage: pyreview.py recv|send')
