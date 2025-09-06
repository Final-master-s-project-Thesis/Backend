from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Passing_performance(Base):
    __tablename__ = "passing_performance"

    performance_id = Column(Integer, ForeignKey("player_performance.performance_id"), primary_key=True, index=True, nullable=False)
    pass_att_p90 = Column(Float, nullable=True)
    pass_acc = Column(Float, nullable=True)
    short_att_p90 = Column(Float, nullable=True)
    short_acc = Column(Float, nullable=True)
    medium_att_p90 = Column(Float, nullable=True)
    medium_acc = Column(Float, nullable=True)
    long_att_p90 = Column(Float, nullable=True)
    long_acc = Column(Float, nullable=True)

    player_performance = relationship("Player_performance", back_populates="passing_performance")