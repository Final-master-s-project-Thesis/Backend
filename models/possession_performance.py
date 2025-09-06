from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Possession_performance(Base):
    __tablename__ = "possession_performance"

    performance_id = Column(Integer, ForeignKey("player_performance.performance_id"), primary_key=True, index=True, nullable=False)
    takeon_att_p90 = Column(Float, nullable=True)
    takeon_ratio = Column(Float, nullable=True)
    recv_p90 = Column(Float, nullable=True)
    prog_recv_p90 = Column(Float, nullable=True)
    carries_p90 = Column(Float, nullable=True)
    prog_carries_p90 = Column(Float, nullable=True)
    carry_dist_p90 = Column(Float, nullable=True)
    prog_carry_dist_p90 = Column(Float, nullable=True)
    carry_final_final3rd_p90 = Column(Float, nullable=True)
    carry_pen_area_p90 = Column(Float, nullable=True)

    player_performance = relationship("Player_performance", back_populates="possession_performance")