from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Duel_performance(Base):
    __tablename__ = "duel_performance"

    performance_id = Column(Integer, ForeignKey("player_performance.performance_id"), primary_key=True, index=True, nullable=False)
    ball_recov_p90 = Column(Float, nullable=True)
    air_duel_total_p90 = Column(Float, nullable=True)
    air_duel_ratio = Column(Float, nullable=True)

    player_performance = relationship("Player_performance", back_populates="duel_performance")