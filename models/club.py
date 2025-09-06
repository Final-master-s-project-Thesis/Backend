from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Club(Base):
    __tablename__ = "club"

    league_id = Column(String(10), ForeignKey("league.league_id"), index=True, nullable=False)
    club_id = Column(String(10), primary_key=True, index=True, nullable=False)
    club_name = Column(String(100), unique=True, index=True, nullable=False)
    season = Column(String(10), nullable=True)
    total_matches = Column(Integer, default=0)

    league = relationship("League", back_populates="clubs")