from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class FM_physical_stats(Base):
    __tablename__ = "fm_physical_stats"

    player_id = Column(String(10), ForeignKey("player_general.player_id"), primary_key=True, index=True, nullable=False)
    physical = Column(Integer, nullable=True)
    stamina = Column(Integer, nullable=True)
    pace = Column(Integer, nullable=True)
    acceleration = Column(Integer, nullable=True)
    agility = Column(Integer, nullable=True)
    aerial_reach = Column(Integer, nullable=True)
    jumping_reach = Column(Integer, nullable=True)
    strength = Column(Integer, nullable=True)
    balance = Column(Integer, nullable=True)

    player_general = relationship("Player_general", back_populates="fm_physical_stats")