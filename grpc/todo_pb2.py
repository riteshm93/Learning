# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo.proto',
  package='todo',
  syntax='proto3',
  serialized_pb=_b('\n\ntodo.proto\x12\x04todo\"\xa0\x01\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04todo\x18\x02 \x01(\t\x12\x0c\n\x04note\x18\x03 \x01(\t\x12!\n\x06status\x18\x04 \x01(\x0e\x32\x11.todo.Todo.Status\"M\n\x06Status\x12\x12\n\x0eUNKNOWN_STATUS\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\r\n\tCOMPLETED\x10\x02\x12\x0f\n\x0bNOT_STARTED\x10\x03\"\xa4\x01\n\x11OperationResponse\x12.\n\x06status\x18\x01 \x01(\x0e\x32\x1e.todo.OperationResponse.Status\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x18\n\x04todo\x18\x03 \x01(\x0b\x32\n.todo.Todo\"4\n\x06Status\x12\x12\n\x0eUNKNOWN_STATUS\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"!\n\x10ListTodosRequest\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"%\n\tTodosList\x12\x18\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\n.todo.Todo2\xdb\x01\n\x05Todos\x12\x30\n\x07\x41\x64\x64Todo\x12\n.todo.Todo\x1a\x17.todo.OperationResponse\"\x00\x12\x36\n\tListTodos\x12\x16.todo.ListTodosRequest\x1a\x0f.todo.TodosList\"\x00\x12\x33\n\nDeleteTodo\x12\n.todo.Todo\x1a\x17.todo.OperationResponse\"\x00\x12\x33\n\nUpdateTodo\x12\n.todo.Todo\x1a\x17.todo.OperationResponse\"\x00\x62\x06proto3')
)



_TODO_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='todo.Todo.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_STATUS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_STARTED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=104,
  serialized_end=181,
)
_sym_db.RegisterEnumDescriptor(_TODO_STATUS)

_OPERATIONRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='todo.OperationResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_STATUS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=296,
  serialized_end=348,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONRESPONSE_STATUS)


_TODO = _descriptor.Descriptor(
  name='Todo',
  full_name='todo.Todo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.Todo.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='todo', full_name='todo.Todo.todo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='note', full_name='todo.Todo.note', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='todo.Todo.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TODO_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=181,
)


_OPERATIONRESPONSE = _descriptor.Descriptor(
  name='OperationResponse',
  full_name='todo.OperationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='todo.OperationResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='todo.OperationResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='todo', full_name='todo.OperationResponse.todo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPERATIONRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=348,
)


_LISTTODOSREQUEST = _descriptor.Descriptor(
  name='ListTodosRequest',
  full_name='todo.ListTodosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='todo.ListTodosRequest.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=383,
)


_TODOSLIST = _descriptor.Descriptor(
  name='TodosList',
  full_name='todo.TodosList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='todo.TodosList.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=422,
)

_TODO.fields_by_name['status'].enum_type = _TODO_STATUS
_TODO_STATUS.containing_type = _TODO
_OPERATIONRESPONSE.fields_by_name['status'].enum_type = _OPERATIONRESPONSE_STATUS
_OPERATIONRESPONSE.fields_by_name['todo'].message_type = _TODO
_OPERATIONRESPONSE_STATUS.containing_type = _OPERATIONRESPONSE
_TODOSLIST.fields_by_name['data'].message_type = _TODO
DESCRIPTOR.message_types_by_name['Todo'] = _TODO
DESCRIPTOR.message_types_by_name['OperationResponse'] = _OPERATIONRESPONSE
DESCRIPTOR.message_types_by_name['ListTodosRequest'] = _LISTTODOSREQUEST
DESCRIPTOR.message_types_by_name['TodosList'] = _TODOSLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Todo = _reflection.GeneratedProtocolMessageType('Todo', (_message.Message,), dict(
  DESCRIPTOR = _TODO,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.Todo)
  ))
_sym_db.RegisterMessage(Todo)

OperationResponse = _reflection.GeneratedProtocolMessageType('OperationResponse', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONRESPONSE,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.OperationResponse)
  ))
_sym_db.RegisterMessage(OperationResponse)

ListTodosRequest = _reflection.GeneratedProtocolMessageType('ListTodosRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTTODOSREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.ListTodosRequest)
  ))
_sym_db.RegisterMessage(ListTodosRequest)

TodosList = _reflection.GeneratedProtocolMessageType('TodosList', (_message.Message,), dict(
  DESCRIPTOR = _TODOSLIST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.TodosList)
  ))
_sym_db.RegisterMessage(TodosList)



_TODOS = _descriptor.ServiceDescriptor(
  name='Todos',
  full_name='todo.Todos',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=425,
  serialized_end=644,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddTodo',
    full_name='todo.Todos.AddTodo',
    index=0,
    containing_service=None,
    input_type=_TODO,
    output_type=_OPERATIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListTodos',
    full_name='todo.Todos.ListTodos',
    index=1,
    containing_service=None,
    input_type=_LISTTODOSREQUEST,
    output_type=_TODOSLIST,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTodo',
    full_name='todo.Todos.DeleteTodo',
    index=2,
    containing_service=None,
    input_type=_TODO,
    output_type=_OPERATIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTodo',
    full_name='todo.Todos.UpdateTodo',
    index=3,
    containing_service=None,
    input_type=_TODO,
    output_type=_OPERATIONRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODOS)

DESCRIPTOR.services_by_name['Todos'] = _TODOS

# @@protoc_insertion_point(module_scope)
