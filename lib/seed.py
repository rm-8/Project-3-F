from models import User,Movie, Base
from sqlalchemy import  create_engine
from sqlalchemy.orm  import sessionmaker
from faker import  Faker
import random

faker=Faker()

my_movies = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Schindler's List",
    "Pulp Fiction",
    "The Lord of the Rings: The Return of the King",
    "Forrest Gump",
    "The Matrix",
    "Fight Club",
    "Inception",
    "Star Wars: Episode V - The Empire Strikes Back",
    "Goodfellas",
    "The Silence of the Lambs",
    "The Lion King",
    "The Green Mile",
    "The Godfather: Part II",
    "The Lord of the Rings: The Fellowship of the Ring",
    "The Avengers",
    "Interstellar",
    "Saving Private Ryan",
    "The Departed",
    "Gladiator",
    "The Prestige",
    "The Usual Suspects",
    "The Terminator",
    "Alien",
    "The Wizard of Oz",
    "The Grand Budapest Hotel",
    "Inglourious Basterds",
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Schindler's List",
    "Pulp Fiction",
    "The Lord of the Rings: The Return of the King",
    "Forrest Gump"
]

movie_durations = [
    142,
    175,
    152,
    195,
    154,
    201,
    142,
    136,
    139,
    148,
    124,
    146,
    118,
    88,
    189,
    202,
    178,
    143,
    169,
    169,
    151,
    155,
    139,
    106,
    117,
    116,
    152,
    155,
    153,
    142,
    175,
    152,
    195,
    154,
    201,
    142,
    135,
    148,
    120,
    162
]



if __name__ == '__main__':
    # Create engine and session
    engine = create_engine("sqlite:///movie.db")
    Base.metadata.create_all(engine)

    mysession = sessionmaker(bind=engine)
    session = mysession()



    users=[
        User(
            user_name=faker.name(),
            passwd=faker.password(),
        )
    for i in range(35)]
    session.query(User).delete()
    session.commit()

    session.add_all(users)
    session.commit()
    my_users=session.query(User).all()
    # print(my_users)

    movies=[
        Movie(
            movie_title=random.choice(my_movies),
            movies_director=faker.name(),
            movie_durartion=random.choice(movie_durations),
            user_id=user.id
        )
    for user in my_users]

    session.query(Movie).delete()
    session.commit()

    session.add_all(movies)
    session.commit()
    





