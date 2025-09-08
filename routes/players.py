from fastapi import APIRouter, Depends, status, HTTPException, Query
from dependencies.dependencies import db_dependency
from typing import Optional
from models import Player_general
from services.auxiliar import apply_filters
from services.filters import PlayerFilters
from services.player_service import get_player_fm24_data, get_player_performance

router = APIRouter(
    prefix="/players",
    tags=["Get data of Players"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/", 
    status_code=status.HTTP_200_OK,
    summary="Get all players general data and filter them",
    description="Retrieve all players with optional filters such as season, league, or club.",
)
def get_players(
    db: db_dependency, 
    filters: PlayerFilters = Depends(), 
    all_data: Optional[bool] = Query(False, description="If true, add fm24_data and performance_data to each player")
):
    query = db.query(Player_general)
    query = apply_filters(query, filters)
    players = query.all()
    
    if all_data:
        full_data_players = []
        
        for player in players:
            fm24_data = get_player_fm24_data(db, player.player_id)
            performance_data = get_player_performance(db, player.player_id)

            full_data = {
                "player": player,
                "fm24_data": fm24_data,
                "performance_data": performance_data
            }

            full_data_players.append(full_data)
        
        return full_data_players

    return players

@router.get(
    "/{player_id}", 
    status_code=status.HTTP_200_OK,
    summary="Get players general data by ID",
    description="Retrieve players",
)
def get_player(player_id: str, db: db_dependency):
    player = db.query(Player_general).filter(Player_general.player_id == player_id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    return player

@router.get(
    "/{player_id}/full_data", 
    status_code=status.HTTP_200_OK,
    summary="Get full player data by ID",
    description="Retrieve full player data including general info, FM24 data, and performance data.",
)
def get_player_full_data(player_id: str, db: db_dependency):
    player = db.query(Player_general).filter(Player_general.player_id == player_id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")

    fm24_data = get_player_fm24_data(db, player_id)
    performance_data = get_player_performance(db, player_id)

    full_data = {
        "player": player,
        "fm24_data": fm24_data,
        "performance_data": performance_data
    }

    return full_data

@router.get(
    "/{player_id}/fm24_data", 
    status_code=status.HTTP_200_OK,
    summary="Get FM24 data by player ID",
    description="Retrieve FM24 data for a specific player.",
)
def get_fm24_data(player_id: str, db: db_dependency):
    player = db.query(Player_general).filter(Player_general.player_id == player_id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")

    fm24_data = get_player_fm24_data(db, player_id)
    return fm24_data

@router.get(
    "/{player_id}/performance",
    status_code=status.HTTP_200_OK,
    summary="Get performance data by player ID",
    description="Retrieve performance data for a specific player.",
)
def get_performance(player_id: str, db: db_dependency):
    player = db.query(Player_general).filter(Player_general.player_id == player_id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")

    performance_data = get_player_performance(db, player_id)
    if not performance_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Performance data not found for this player")

    return performance_data

@router.get(
    "/{player_id}/similar",
    status_code=status.HTTP_200_OK,
    summary="Get similar players to a given player ID",
    description="Retrieve a list of players similar to the specified player.",
)
def get_similar_players(player_id: str, db: db_dependency, filters: PlayerFilters = Depends()):
    player = db.query(Player_general).filter(Player_general.player_id == player_id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")

    query = db.query(Player_general).filter(
        Player_general.type_player == player.type_player,
    )
    query = apply_filters(query, filters)
    
    similar_players = query.all()
    return similar_players