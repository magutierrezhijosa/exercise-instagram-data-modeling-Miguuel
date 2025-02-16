import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    user_name = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    relation_favorite = relationship('Followers' , backref='user')
    relation_comment = relationship('Comment' , backref='user')
    relation_post = relationship('Post' , backref='user')
    
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer,primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer,primary_key=True)
    comment_text = Column(String(250))
    author_id =  Column(Integer, ForeignKey('user.id'))
    post_id =  Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer,primary_key=True)
    user_id =  Column(Integer, ForeignKey('user.id'))
    relation_post = relationship('Comment' , backref='post')
    relation_media = relationship('Media' , backref='post')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer,primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e