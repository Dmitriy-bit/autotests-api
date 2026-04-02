import grpc

import user_service_pb2
import user_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = user_service_pb2_grpc.UserServiceStub(channel)

response = stub.GetUser(user_service_pb2.GetUserRequest(username="Alice"))
response_age = stub.GetAge(user_service_pb2.GetUserAgeRequest(age="17"))

print(response)
print(response_age)