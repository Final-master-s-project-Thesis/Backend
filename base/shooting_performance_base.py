from pydantic import BaseModel

class ShootingPerformanceBase(BaseModel):
    performance_id: int
    goals_p90: float
    shots_p90: float
    shots_on_target_p90: float
    goals_per_shot: float
