from fastapi import HTTPException,status,Depends
from sqlmodel import Session
from app import models_and_schemas
from app import database
from app import auth
import json

def create_user(db:Session,user:models_and_schemas.UserSchema):
    hashed_password=auth.create_password_hash(user.password)
    db_user=models_and_schemas.User(
        email=user.email,
        username=user.username,
        role=user.role,
        is_active=user.is_active,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db:Session):
    users=db.query(models_and_schemas.User).all()
    return users

def get_user_by_username(db: Session, username: str):
    user=db.query(models_and_schemas.User).filter(models_and_schemas.User.username==username).first()
    return user

"""Movies"""
def create_movies(db:Session,movie:models_and_schemas.UserSchema):
    genre=json.dumps(movie.genre)
    print(genre)
    db_movie=models_and_schemas.Movies(
        popularity=movie.popularity,
        director=movie.director,
        genre=genre,
        imdb_score=movie.imdb_score,
        name=movie.name
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_movies(db:Session,skip: int = 0, limit: int = 100):
    movies=db.query(models_and_schemas.Movies).offset(skip).limit(limit).all()
    return movies

def get_movie_by_id(db: Session, id: int):
    movie=db.query(models_and_schemas.Movies).filter(models_and_schemas.Movies.id==id).first()
    return movie

def get_movie_by_name(db: Session, name: str):
    movie=db.query(models_and_schemas.Movies).filter(models_and_schemas.Movies.name==name).first()
    return movie



def delete_movie(db: Session, id: int):
    movie=db.query(models_and_schemas.Movies).filter(models_and_schemas.Movies.id==id)
    movie.delete()
    db.commit()
    
    
def update_movie(db:Session,movie:models_and_schemas.MovieSchema,id: int):
    genre=json.dumps(movie.genre)
    db_movie=db.query(models_and_schemas.Movies).filter(models_and_schemas.Movies.id==id).update({'popularity':movie.popularity,
        'director':movie.director,
        'genre':genre,
        'imdb_score':movie.imdb_score,
        'name':movie.name})
    
    db.commit()
    return db_movie
   
"""function to insert json data into db"""
def create_movies_from_json(db:Session,movie):
    print(movie,"From crud program")
    genre=json.dumps(movie.get('genre'))
    print(genre)
    db_movie=models_and_schemas.Movies(
        popularity=movie.get('99popularity'),
        director=movie.get('director'),
        genre=genre,
        imdb_score=movie.get('imdb_score'),
        name=movie.get('name')
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie
  
    
