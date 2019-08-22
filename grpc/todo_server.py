from concurrent import futures
import time

import grpc

import todo_pb2
import todo_pb2_grpc

from main import get_all_todos, delete_todo, add_todo, update_todo

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Todo(todo_pb2_grpc.TodosServicer):

    def AddTodo(self, request, context):
        if request.todo == '':
            response=todo_pb2.OperationResponse(todo=request)
            response.status= 2
            response.message= 'Required fields missing'
        else:
            todo = add_todo(request)
            response=todo_pb2.OperationResponse(todo=todo_pb2.Todo(id=todo.id, todo=todo.todo, note=todo.note, status=todo.status))
            response.status= 1
            response.message='New Todo "%s" created!' % response.todo.todo
        return response

    def ListTodos(self, request, context):
        data = list()
        todos = get_all_todos()
        for todo in todos:
            data.append(todo_pb2.Todo(id=todo.id, todo=todo.todo, note=todo.note, status=todo.status))
        return todo_pb2.TodosList(data=data)

    def UpdateTodo(self, request, context):
        response=todo_pb2.OperationResponse(todo=request, status=2)
        message, todo = update_todo(request)
        if todo:
            response=todo_pb2.OperationResponse(todo=todo_pb2.Todo(id=todo.id, todo=todo.todo, note=todo.note, status=todo.status), status=1, message=message)
        else:
            response.message=message
        return response

    def DeleteTodo(self, request, context):
        status, message = delete_todo(request.id)
        return todo_pb2.OperationResponse(status=status, message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodosServicer_to_server(Todo(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

