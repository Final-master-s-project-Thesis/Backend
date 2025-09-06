from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class FM_dead_ball_stats(Base):
    __tablename__ = "fm_dead_ball_stats"

    player_id = Column(String(10), ForeignKey("player_general.player_id"), primary_key=True, index=True, nullable=False)
    corner_taking = Column(Integer, nullable=True)
    free_kick_taking = Column(Integer, nullable=True)
    penalty_taking = Column(Integer, nullable=True)

    player_general = relationship("Player_general", back_populates="fm_dead_ball_stats")