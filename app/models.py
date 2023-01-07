from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base
from sqlalchemy.orm import relationship

# define the model
class Post(Base):
    __tablename__ = "posts"

    # specifying the columns
    id = Column(Integer, primary_key=True, nullable = False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published=Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    # set up the foreign key constraint
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable = False)
    owner = relationship("User") 


class User(Base):
    __tablename__ = "users"

    email = Column(String, nullable=False, unique=True)
    password=Column(String, nullable=False)
    id = Column(Integer, primary_key=True, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_number = Column(String)


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key = True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key = True)

