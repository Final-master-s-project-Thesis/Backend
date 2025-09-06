from pydantic import BaseModel

class FMDeadBallStatsBase(BaseModel):
    player_id: str
    corners: int
    penalty_taking: int
    free_kicks: int