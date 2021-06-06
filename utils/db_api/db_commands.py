import logging

from utils.db_api.database import db, session
from utils.db_api.models import Users



async def is_client(client_tg_id):
    conn = db.connect()
    user = session.query(Users).group_by(Users.tg_id == client_tg_id).one_or_none()
    if not user == None:
        logging.info('Нашли клиента!')
        return True
    else:
        logging.info('Не нашли клиента!')
        return False


def add_new_client(name, client_tg_id):
    client = Users(name=name, tg_id=client_tg_id)
    session.add(client)
    session.commit()
    logging.info(f'Добавили нового юpера {name}')