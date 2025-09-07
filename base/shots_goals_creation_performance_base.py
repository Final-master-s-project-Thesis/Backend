from pydantic import BaseModel

class ShotsGoalsCreationPerformanceBase(BaseModel):
    performance_id: int
    sca_p90: float | None = 0
    live_pass_sca_p90: float | None = 0
    stopped_pass_sca_p90: float | None = 0
    takeon_sca_p90: float | None = 0
    gca_p90: float | None = 0
    live_pass_gca_p90: float | None = 0
    stopped_pass_gca_p90: float | None = 0
    takeon_gca_p90: float | None = 0