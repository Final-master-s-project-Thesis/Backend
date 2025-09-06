from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Shots_goals_creation_performance(Base):
    __tablename__ = "shots_goals_creation_performance"

    performance_id = Column(Integer, ForeignKey("player_performance.performance_id"), primary_key=True, index=True, nullable=False)
    sca_p90 = Column(Float, nullable=True)
    live_pass_sca_p90 = Column(Float, nullable=True)
    stopped_pass_sca_p90 = Column(Float, nullable=True)
    takeon_sca_p90 = Column(Float, nullable=True)
    gca_p90 = Column(Float, nullable=True)
    live_pass_gca_p90 = Column(Float, nullable=True)
    stopped_pass_gca_p90 = Column(Float, nullable=True)
    takeon_gca_p90 = Column(Float, nullable=True)

    player_performance = relationship("Player_performance", back_populates="shots_goals_creation_performance")