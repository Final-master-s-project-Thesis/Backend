from pydantic import BaseModel

class ShotsGoalsCreationPerformanceBase(BaseModel):
    performance_id: int
    sca_p90: float
    live_pass_sca_p90: float
    stopped_pass_sca_p90: float
    takeon_sca_p90: float
    gca_p90: float
    live_pass_gca_p90: float
    stopped_pass_gca_p90: float
    takeon_gca_p90: float