from pydantic import BaseModel

class LeagueBase(BaseModel):
    league_id: str
    competition_name: str
    gender: str
    first_season: str