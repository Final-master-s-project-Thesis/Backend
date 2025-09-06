from pydantic import BaseModel

class FMMentalStatsBase(BaseModel):
    player_id: str
    serenity: int
    communication: int
    determination: int
    decisions: int
    concentration: int
    aggression: int
    vision: int
    leadership: int
    teamwork: int
    bravery: int
    sacrifice: int