from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Player_performance(Base):
    __tablename__ = "player_performance"

    player_id = Column(String(10), ForeignKey("player_general.player_id"), primary_key=True, index=True, nullable=False)
    season = Column(String(10), nullable=False)
    performance_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    player_general = relationship("Player_general", back_populates="player_performance")
    passing_performance = relationship("Passing_performance", back_populates="player_performance")
    shooting_performance = relationship("Shooting_performance", back_populates="player_performance")
    defensive_performance = relationship("Defensive_performance", back_populates="player_performance")
    possession_performance = relationship("Possession_performance", back_populates="player_performance")
    duel_performance = relationship("Duel_performance", back_populates="player_performance")
    goalkeeping_performance = relationship("Goalkeeping_performance", back_populates="player_performance")
    shots_goals_creation_performance = relationship("Shots_goals_creation_performance", back_populates="player_performance")