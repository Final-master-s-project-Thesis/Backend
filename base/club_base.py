from pydantic import BaseModel

class ClubBase(BaseModel):
    league_id: str
    club_id: str
    club_name: str
    season: str | None = None
    total_matches: int | None = 0
