from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Country(Base):
    __tablename__ = "country"

    country_code = Column(String(3), primary_key=True, nullable=False)
    country = Column(String(100), unique=True, index=True, nullable=False)

    player_general = relationship("Player_general", back_populates="country")