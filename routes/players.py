from fastapi import APIRouter, status, HTTPException
from dependencies.dependencies import db_dependency
from models import Player_general

router = APIRouter(
    prefix="/players",
    tags=["Get data of Players"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/", 
    status_code=status.HTTP_200_OK,
    summary="Get all players and filter them",
    description="Retrieve all players with optional filters such as season, league, or club.",
)
def get_players(db: db_dependency):
    players = db.query(Player_general).all()
    return players

@router.get("/{player_id}", status_code=status.HTTP_200_OK)
def get_player(player_id: int, db: db_dependency):
    player = db.query(Player_general).filter(Player_general.id == player_id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    return player