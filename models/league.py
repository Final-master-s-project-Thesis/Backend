from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class League(Base):
    __tablename__ = "league"

    league_id = Column(String(10), primary_key=True, index=True, nullable=False)
    competition_name = Column(String(100), unique=True, index=True, nullable=False)
    gender = Column(String(1), nullable=True)
    first_season = Column(String(10), nullable=True)

    clubs = relationship("Club", back_populates="league")