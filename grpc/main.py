from models import Todos

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import secrets

engine = create_engine(secrets.db)
Session = sessionmaker(bind=engine)


def get_all_todos():
    session = Session()
    todos = session.query(Todos).all()
    return todos

def delete_todo(id):
    session = Session()
    todo = session.query(Todos).filter(Todos.id==id).first()
    if todo:
        session.delete(todo)
        session.commit()
        return 1, 'Todo removed!'
    else:
        return 2, 'No Todo with id %s exists' % str(id)

def add_todo(request):
    session = Session()
    todo = Todos(todo=request.todo, note=request.note, status=request.status)
    session.add(todo)
    session.commit()
    return todo

def update_todo(request):
    session = Session()
    todo = session.query(Todos).filter(Todos.id==request.id).first()
    if not request.todo and not request.status and not request.note:
        return 'Required fields missing', None
    elif todo:
        if request.todo:
            todo.todo = request.todo
        if request.note:
            todo.note = request.note
        if request.status:
            todo.status = request.status
        session.commit()
        return 'Todo updated', todo
    else:
        return 'No Todo with id %s exists' % request.id, None


