from pydantic import BaseModel

class FMGoalkeeperStatsBase(BaseModel):
    player_id: str
    rushing_out: int
    command_of_area: int
    punching: int
    eccentricity: int
    goal_kicks: int
    hand_throws: int
    long_throws: int
    one_on_ones: int
    blocking: int
    reflexes: int
