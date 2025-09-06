from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Defensive_performance(Base):
    __tablename__ = "defensive_performance"

    performance_id = Column(Integer, ForeignKey("player_performance.performance_id"), primary_key=True, index=True, nullable=False)
    tkl_p90 = Column(Float, nullable=True)
    tkl_ratio = Column(Float, nullable=True)
    drb_tkl_p90 = Column(Float, nullable=True)
    drb_tkl_ratio = Column(Float, nullable=True)
    blocks_p90 = Column(Float, nullable=True)
    sh_blocks_p90 = Column(Float, nullable=True)
    int_p90 = Column(Float, nullable=True)
    clr_p90 = Column(Float, nullable=True)

    player_performance = relationship("Player_performance", back_populates="defensive_performance")