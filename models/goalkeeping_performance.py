from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Goalkeeping_performance(Base):
    __tablename__ = "goalkeeping_performance"

    performance_id = Column(Integer, ForeignKey("player_performance.performance_id"), primary_key=True, index=True, nullable=False)
    save_ratio = Column(Float, nullable=True)
    clean_sheets_ratio = Column(Float, nullable=True)

    player_performance = relationship("Player_performance", back_populates="goalkeeping_performance")