from pydantic import BaseModel

class DefensePerformanceBase(BaseModel):
    performance_id: int
    tkl_p90: float
    tkl_ratio: float
    drb_tkl_p90: float
    drb_tkl_ratio: float
    blocks_p90: float
    sh_blocks_p90: float
    int_p90: float
    clr_p90: float