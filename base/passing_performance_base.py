from pydantic import BaseModel

class PassingPerformanceBase(BaseModel):
    performance_id: int
    pass_att_p90: float
    pass_acc: float
    short_att_p90: float
    short_acc: float
    medium_att_p90: float
    medium_acc: float
    long_att_p90: float
    long_acc: float