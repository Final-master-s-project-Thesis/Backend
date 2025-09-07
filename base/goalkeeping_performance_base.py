from pydantic import BaseModel

class GoalkeepingPerformanceBase(BaseModel):
    player_id: int
    save_ratio: float | None = 0
    clean_sheets_ratio: float | None = 0
