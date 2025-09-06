from pydantic import BaseModel

class PlayerGeneralBase(BaseModel):
    club_id: str
    player_id: str
    name: str
    country_code: str
    age: int
    position: str
    height: int
    weight: int
    talent: int
    type_player: int
    market_value: float
    estimated_value: float
    salary_month: float