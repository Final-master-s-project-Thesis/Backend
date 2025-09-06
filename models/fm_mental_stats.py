from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class FM_mental_stats(Base):
    __tablename__ = "fm_mental_stats"

    player_id = Column(String(10), ForeignKey("player_general.player_id"), primary_key=True, index=True, nullable=False)
    serenity = Column(Integer, nullable=True)
    communication = Column(Integer, nullable=True)
    determination = Column(Integer, nullable=True)
    decisions = Column(Integer, nullable=True)
    concentration = Column(Integer, nullable=True)
    aggression = Column(Integer, nullable=True)
    vision = Column(Integer, nullable=True)
    leardership = Column(Integer, nullable=True)
    teamwork = Column(Integer, nullable=True)
    bravery = Column(Integer, nullable=True)
    sacrifice = Column(Integer, nullable=True)

    player_general = relationship("Player_general", back_populates="fm_mental_stats")