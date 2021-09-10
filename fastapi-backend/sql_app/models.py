from sqlalchemy import Column, ForeignKey, Integer, String, Sequence
from sqlalchemy.orm import relationship

id_seq = Sequence('id_seq')
from .database import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(String(100), primary_key=True, unique=True, index=True)
    name = Column(String(100))
    picture = Column(String(255))
    projects = relationship("Project", back_populates="owner")


class Game(Base):
    __tablename__ = "games"
    score = Column(Integer(100))
    level = Column(Integer(100))
    owner_id = Column(String(100), ForeignKey("users.uid"))

    owner = relationship("User", back_populates="games")


class Style(Base):
    __tablename__ = "styles"
    size = Column(String(100))
    color = Column(String(100))
    owner_id = Column(String(100), ForeignKey("users.uid"))

    owner = relationship("User", back_populates="styles")
