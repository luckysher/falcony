
from models import User
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
import traceback
from utils import strToToken
from settings import db_url


def isUserAuthenticated(session, username, password):
    token = None
    try:
        user = session.query(User).filter(User.username==username).first()
        password = strToToken(password)
        if password == user.password:
            token = user.password
            return token
    except Exception as e:
        print('Got exception while getting user..')
        print(e)
    return token
