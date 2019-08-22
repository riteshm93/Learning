import grpc

import todo_pb2
import todo_pb2_grpc


def status_name(status):
    return todo_pb2.OperationResponse.Status.Name(status)

def print_response(response):
    print('Status: %s\nMessaage: %s\nDetails:\n%s' % (status_name(response.status), response.message, response.todo))

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = todo_pb2_grpc.TodosStub(channel)

    ip = 1
    while (ip!=0):
        ip = int(input("-----Select any option-----\n1. Add Todo\n2. List Todos\n3. Update Todo\n4. Delete Todo\n0. Exit\nEnter Choice: "))
        if ip==1:
            print('-----Add Todo-----')
            todo = input("Enter Todo: ")
            note = input("Enter Note: ")
            response = stub.AddTodo(todo_pb2.Todo(todo=todo, note=note, status=3))
            print('-----')
            print_response(response)
        elif ip==2:
            print('-----List Todos-----')
            response = stub.ListTodos(todo_pb2.ListTodosRequest(count=1))
            for todo in response.data:
                print(todo)
        elif ip==3:
            print('-----Update Todo-----')
            id = int(input("Enter todo id to update: "))
            print("Leave input fields blank to retain the orignal data")
            todo = input("Enter Updated Todo: ")
            note = input("Enter Updated Note: ")
            print("Status Codes:\n1 -> In Progress\n2 -> Completed\n3 -> Not Started")
            status = input("Enter Updated Status: ")
            if not status:
                status = 0
            else:
                status = int(status)
            response = stub.UpdateTodo(todo_pb2.Todo(id=id, todo=todo, note=note, status=status))
            print('-----')
            print_response(response)
        elif ip==4:
            print('-----Delete Todo-----')
            id = int(input("Enter todo id to delete: "))
            response = stub.DeleteTodo(todo_pb2.Todo(id=id))
            print('-----\nStatus: %s\nMessaage: %s' % (status_name(response.status), response.message))


if __name__ == '__main__':
    run()

