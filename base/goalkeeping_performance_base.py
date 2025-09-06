from pydantic import BaseModel

class GoalkeepingPerformanceBase(BaseModel):
    player_id: int
    save_ratio: float
    clean_sheets_ratio: float
