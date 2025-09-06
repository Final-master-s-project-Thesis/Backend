from pydantic import BaseModel

class PlayerPerformanceBase(BaseModel):
    player_id: str
    season: str
    performance_id: int