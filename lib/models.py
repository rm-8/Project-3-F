from sqlalchemy import Column, Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base

Base=declarative_base()

class User(Base):

    __tablename__="users"

    id =Column(Integer,primary_key=True)
    user_name=Column(String())
    passwd=Column(String())

    def __repr__(self):
        return f"<User(id={self.id}, name={self.user_name}, password={self.passwd})>"


class Movie(Base):

    __tablename__="movies"

    id=Column(Integer, primary_key=True)
    movie_title=Column(String())
    movies_director=Column(String())
    movie_durartion=Column(Integer())
    user_id=Column(Integer(),ForeignKey("users.id"))


    def __repr__(self):
        return f"<Movie(id={self.id}, title={self.movie_title}, director={self.movies_director}, duration={self.movie_durartion}, user_id={self.user_id})>"


    


    


    