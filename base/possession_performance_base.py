from pydantic import BaseModel

class PossessionPerformanceBase(BaseModel):
    performance_id: int
    takeon_att_p90: float
    takeon_ratio: float
    recv_p90: float
    prog_recv_p90: float
    carries_p90: float
    prog_carries_p90: float
    carry_dist_p90: float
    prog_carry_dist_p90: float
    carry_final_third_p90: float
    carry_pen_area_p90: float