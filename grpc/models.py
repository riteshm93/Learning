from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Unicode

Base = declarative_base()


class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    todo = Column(String(100))
    note = Column(Unicode(250))
    status = Column(String)
    time = Column(String)

    def __repr__(self):
        return "<Todos(id='%s', todo='%s', note='%s', status ='%s')>" % (
            self.id, self.todo, self.note, self.status)
