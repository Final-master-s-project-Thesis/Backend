from pydantic import BaseModel

class DefensePerformanceBase(BaseModel):
    performance_id: int
    tkl_p90: float | None = 0
    tkl_ratio: float | None = 0
    drb_tkl_p90: float | None = 0
    drb_tkl_ratio: float | None = 0
    blocks_p90: float | None = 0
    sh_blocks_p90: float | None = 0
    int_p90: float | None = 0
    clr_p90: float | None = 0