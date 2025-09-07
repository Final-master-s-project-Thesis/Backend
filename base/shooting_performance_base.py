from pydantic import BaseModel

class ShootingPerformanceBase(BaseModel):
    performance_id: int
    goals_p90: float | None = 0
    shots_p90: float | None = 0
    shots_on_target_p90: float | None = 0
    goals_per_shot: float | None = 0
