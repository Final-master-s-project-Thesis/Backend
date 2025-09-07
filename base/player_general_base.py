from pydantic import BaseModel

class PlayerGeneralBase(BaseModel):
    club_id: str
    player_id: str
    name: str
    country_code: str
    age: int | None = None
    position: str | None = None
    height: int | None = None
    weight: int | None = None
    talent: int | None = None
    type_player: int | None = None
    market_value: float | None = None
    estimated_value: float | None = None
    salary_month: float | None = None