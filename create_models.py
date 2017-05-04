from models import Base
from sqlalchemy import create_engine
from settings import db_url


def create_models():
    engine = create_engine(db_url)
    print("creating models...")
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_models()
