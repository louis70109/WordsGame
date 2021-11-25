from sqlalchemy import Column, ForeignKey, Integer, String, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint

id_seq = Sequence('id_seq')
style_id_seq = Sequence('style_id_seq')
from .database import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(String(100), primary_key=True, unique=True, index=True)
    name = Column(String(100))
    picture = Column(String(255))
    games = relationship("Game", back_populates="owner")
    styles = relationship("Style", back_populates="owner")


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, id_seq, primary_key=True, unique=True, index=True,
        server_default=id_seq.next_value())
    score = Column(Integer)
    level = Column(Integer)
    owner_id = Column(String(100), ForeignKey("users.uid"))
    # __table_args__ = (
    #     UniqueConstraint('score', 'level', name='game_unique'),)

    owner = relationship("User", back_populates="games")


class Style(Base):
    __tablename__ = "styles"

    id = Column(Integer, style_id_seq,
        primary_key=True, 
        unique=True,
        index=True, 
        server_default=style_id_seq.next_value())
    size = Column(String(100))
    color = Column(String(100))
    duration = Column(Integer, default=10)
    level = Column(Integer)
    owner_id = Column(String(100), ForeignKey("users.uid"), unique=True)

    owner = relationship("User", back_populates="styles")
