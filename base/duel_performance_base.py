from pydantic import BaseModel

class DuelPerformanceBase(BaseModel):
    performance_id: int
    ball_recov_p90: float
    air_duel_total_p90: float
    air_duel_ratio: float