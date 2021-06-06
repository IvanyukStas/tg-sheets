from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Sequence

from .database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(28))
    tg_id = Column(Integer)
    create_date = Column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'User: {self.name}' \
               f'TG id: {self.tg_id}'