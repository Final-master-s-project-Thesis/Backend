from typing import Optional
from pydantic import BaseModel

class PlayerFilters(BaseModel): 
    # General Filters
    country_code: Optional[str] = None
    club_id: Optional[str] = None
    age_min: Optional[int] = None
    age_max: Optional[int] = None
    height_min: Optional[int] = None
    height_max: Optional[int] = None
    weight_min: Optional[int] = None
    weight_max: Optional[int] = None
    position: Optional[str] = None
    market_value_max: Optional[float] = None
    estimated_value_max: Optional[float] = None
    salary_month_max: Optional[float] = None
    talent_min: Optional[int] = None