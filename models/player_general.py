from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Player_general(Base):
    __tablename__ = "player_general"

    club_id = Column(String(10), ForeignKey("club.club_id"), index=True, nullable=False)
    player_id = Column(String(10), primary_key=True, index=True, nullable=False)
    name = Column(String(100), index=True, nullable=False)
    country_code = Column(String(4), 
                          #ForeignKey("country.country_code"), 
                          nullable=True)
    age = Column(Integer, nullable=True)
    position = Column(String(100), nullable=True)
    height = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    talent = Column(Integer, nullable=True)
    type_player = Column(Integer, nullable=True)
    market_value = Column(Float, nullable=True)
    estimated_value = Column(Float, nullable=True)
    salary_month = Column(Float, nullable=True)

    club = relationship("Club", back_populates="player_general")
    #country = relationship("Country", back_populates="player_general")
    player_performance = relationship("Player_performance", back_populates="player_general")
    fm_goalkeeper_stats = relationship("FM_goalkeeper_stats", back_populates="player_general")
    fm_physical_stats = relationship("FM_physical_stats", back_populates="player_general")
    fm_mental_stats = relationship("FM_mental_stats", back_populates="player_general")
    fm_technical_stats = relationship("FM_technical_stats", back_populates="player_general")
    fm_dead_ball_stats = relationship("FM_dead_ball_stats", back_populates="player_general")