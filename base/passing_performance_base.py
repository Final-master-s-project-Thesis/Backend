from pydantic import BaseModel

class PassingPerformanceBase(BaseModel):
    performance_id: int
    pass_att_p90: float | None = 0
    pass_acc: float | None = 0
    short_att_p90: float | None = 0
    short_acc: float | None = 0
    medium_att_p90: float | None = 0
    medium_acc: float | None = 0
    long_att_p90: float | None = 0
    long_acc: float | None = 0