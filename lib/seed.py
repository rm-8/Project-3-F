from models import User,Movie, Base
from sqlalchemy import  create_engine
from sqlalchemy.orm  import sessionmaker
if __name__ == '__main__':
    # Create engine and session
    engine = create_engine("sqlite:///movie.db")
    Base.metadata.create_all(engine)

    mysession = sessionmaker(bind=engine)
    session = mysession()