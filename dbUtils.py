
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

# function for returning engine
def getEngine(dbUrl):
    engine = create_engine(db_url)
    return engine

# function for getting session
def getSession(engine):
    Session = sessionmaker(bind=engine)
    return Session()

# fun for creating user
def createUser(session, firstName, lastName, username, password):
    user = User(first_name=firstName, last_name=lastName)
    # set user name
    user.set_username(username)
    # set user password
    user.set_password(password)
    try:
        session.add(user)
        session.commit()
        print('user created successfully...')
    except Exception as e:
        print ("Got exception while creating user")
        print(e)
        session.rollback()
        traceback.print_exc()

def getProductDetails(productsList):
    productsInfo = {}
    if productsList.__len__():
        for products in productsList:
            # get products details
            if products:
                productCount = 0
                manufacturers = []
                for product in products:
                    productCount += product.quantity
                    manufacturers.append(product.manufacturer)
                    product_name = product.__class__.__name__

                productsDetails = {'name': product_name, 'quantity': productCount, 'manufacturers': manufacturers}
                productsInfo[product_name] = productsDetails

    return productsInfo

if __name__ == '__main__':
    engine = getEngine(db_url)
    session = getSession(engine)
    createUser(session, 'John', 'drew', 'john123', '12345678')