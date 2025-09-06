from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class FM_technical_stats(Base):
    __tablename__ = "fm_technical_stats"

    player_id = Column(String(10), ForeignKey("player_general.player_id"), primary_key=True, index=True, nullable=False)
    technique = Column(Integer, nullable=True)
    passing = Column(Integer, nullable=True)
    centering = Column(Integer, nullable=True)
    crossing = Column(Integer, nullable=True)
    dribbling = Column(Integer, nullable=True)
    off_the_ball = Column(Integer, nullable=True)
    finishing = Column(Integer, nullable=True)
    heading = Column(Integer, nullable=True)
    marking = Column(Integer, nullable=True)
    tackling = Column(Integer, nullable=True)
    long_shots = Column(Integer, nullable=True)
    anticipation = Column(Integer, nullable=True)
    positioning = Column(Integer, nullable=True)

    player_general = relationship("Player_general", back_populates="fm_technical_stats")