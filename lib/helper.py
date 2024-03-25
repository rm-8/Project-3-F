from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User, Movie



engine = create_engine("sqlite:///movie.db")
mysession = sessionmaker(bind=engine)
session = mysession()

def list_users():
    print ("Listing all users:")
    users = session.query(User).all()
    for user in users:
        print(user)

def find_user_by_name():
    name = input("Enter your user's name : ")
    user = session.query(User).filter_by(user_name=name).first()
    print(
        "NAME: ", user.user_name,
        "PASSWORD: ", user.passwd
        
        )  

def find_user_by_id():
    id_num = input("Enter your User's ID number: ")
    user = session.query(User).filter_by(id=id_num).first()
    print(
        "ID: ", user.id,
        "NAME: ", user.user_name,
        "PASSWORD: ", user.passwd
        
    )

def  add_new_user():
    user_id = input("Enter the User's unique ID number: ")
    user_name = input("Enter  the Users's Name: ")
    password =  input("Enter the Password: ")

    new_user = User(id=user_id, user_name=user_name, passwd=password)

    session.add(new_user)
    session.commit()
    print(f"The New user {user_name} has been added succesfully.")



def list_movies():
    print ("Listing all movies:")
    movies = session.query(Movie).all()
    for movie in movies:
        print(movie)

def find_movie_by_title():
    name = input("Enter your Movie's title:")
    movie = session.query(Movie).filter_by(movie_title=name).first()
    print(
        "NAME: ", movie.movie_title,
        "DIRECTOR: ", movie.movies_director,
        "DURATION: ", movie.movie_durartion,
        "USER ID: ", movie.user_id

         
    )  



def add_new_movie():
    movie_id = input("Enter the new movie's ID number: ")
    movies_title = input("Enter the new movie's title : ")
    movies_director = input("Enter the new director's name : ")
    movies_duration = input("Enter the duration of your new movie: ")
    user_id = input("Enter the User's ID: ")

    new_movie = Movie(id=user_id, movie_title=movies_title, movies_director=movies_director, movie_durartion=movies_duration, user_id=user_id)

    session.add(new_movie)
    session.commit()
    print(f"The new movie {movies_title} has been  added to the system!")


def exit_program():
    print("GOODBYE!!!! THANK YOU!!!")
    exit()          