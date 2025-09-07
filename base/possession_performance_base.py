from pydantic import BaseModel

class PossessionPerformanceBase(BaseModel):
    performance_id: int
    takeon_att_p90: float | None = 0
    takeon_ratio: float | None = 0
    recv_p90: float | None = 0
    prog_recv_p90: float | None = 0
    carries_p90: float | None = 0
    prog_carries_p90: float | None = 0
    carry_dist_p90: float | None = 0
    prog_carry_dist_p90: float | None = 0
    carry_final_third_p90: float | None = 0
    carry_pen_area_p90: float | None = 0