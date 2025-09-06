from pydantic import BaseModel

class FMPhysicalStatsBase(BaseModel):
    player_id: str
    physical: int
    stamina: int
    pace: int
    acceleration: int
    agility: int
    aerial_reach: int
    jumping_reach: int
    strength: int
    balance: int