from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class FM_goalkeeper_stats(Base):
    __tablename__ = "fm_goalkeeper_stats"

    player_id = Column(String(10), ForeignKey("player_general.player_id"), primary_key=True, index=True, nullable=False)
    rushing_out = Column(Integer, nullable=True)
    command_of_area = Column(Integer, nullable=True)
    punching = Column(Integer, nullable=True)
    eccentricity = Column(Integer, nullable=True)
    goal_kicks = Column(Integer, nullable=True)
    hand_throws = Column(Integer, nullable=True)
    long_throws = Column(Integer, nullable=True)
    one_on_ones = Column(Integer, nullable=True)
    blocking = Column(Integer, nullable=True)
    reflexes = Column(Integer, nullable=True)

    player_general = relationship("Player_general", back_populates="fm_goalkeeper_stats")