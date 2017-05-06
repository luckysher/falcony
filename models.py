from sqlalchemy import Column
from sqlalchemy import String, Integer, BigInteger, Boolean
from sqlalchemy.ext.declarative import declarative_base
from utils import strToToken

Base = declarative_base()


# model for users
class User(Base):
    __tablename__ = 'User'

    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, nullable=False, unique=True)
    password = Column(String)

    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def set_password(self, password):
        self.password = strToToken(password)

    def get_password(self):
        return self.password

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def __repr__(self):
        return 'User(name=%s, is_admin=%s)' % (self.full_name(), self.is_admin)


# model for harddisk
class Harddisks(Base):
    __tablename__ = 'harddisks'

    hid = Column(BigInteger, primary_key=True)
    name = Column(String)
    available = Column(Boolean, default=False)
    cost = Column(Integer)
    manufacturer = Column(String)
    quantity = Column(Integer)
    warranty = Column(Integer, nullable=True)
    img_url = Column(String)

    def code(self):
        return 'HDD'

    def __repr__(self):
        return 'Harddisk(name=%s, available=%s, cost=%s, warranty=%s, image-url=%s)' % (self.name, self.available,
                                                                                       self.cost, self.warranty, self.img_url)

# model for handphone
class Headphone(Base):
    __tablename__ = 'headphone'

    hpid = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=True)
    available = Column(Boolean, default=False)
    cost = Column(Integer)
    manufacturer = Column(String)
    quantity = Column(Integer)
    warranty = Column(Integer, nullable=True)
    img_url = Column(String)

    def code(self):
        return 'HDF'

    def __repr__(self):
        return 'HeadPhone(name=%s, available=%s, cost=%s, warranty=%s, image-url=%s)' % (self.name, self.available,
                                                               self.cost, self.warranty, self.img_url)

