from sqlalchemy import Column
from sqlalchemy import String, Integer, BigInteger, Boolean
from sqlalchemy.ext.declarative import declarative_base
from utils import strToToken

Base = declarative_base()


# model for users
class Users(Base):
    __tablename__ = 'Users'

    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)

    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def set_password(self, password):
        self.password = strToToken(password)

    def __repr__(self):
        return 'User(name=%s, is_admin=%s)' % (self.full_name(), self.is_admin)


