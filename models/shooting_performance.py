from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Shooting_performance(Base):
    __tablename__ = "shooting_performance"

    performance_id = Column(Integer, ForeignKey("player_performance.performance_id"), primary_key=True, index=True, nullable=False)
    goals_p90 = Column(Float, nullable=True)
    shots_p90 = Column(Float, nullable=True)
    shots_on_target_p90 = Column(Float, nullable=True)
    goals_per_shot = Column(Float, nullable=True)

    player_performance = relationship("Player_performance", back_populates="shooting_performance")