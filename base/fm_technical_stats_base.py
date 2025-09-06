from pydantic import BaseModel

class FMTechnicalStatsBase(BaseModel):
    player_id: str
    technique: int
    passing: int
    centering: int
    crossing: int
    dribbling: int
    off_the_ball: int
    finishing: int
    heading: int
    marking: int
    tackling: int
    long_shots: int
    anticipation: int
    positioning: int