from typing import List
from fastapi import APIRouter, status, HTTPException, Query
from dependencies.dependencies import db_dependency
from models import Player_general
from services.player_service import get_player_fm24_data, get_player_performance

router = APIRouter(
    prefix="/compare",
    tags=["Compare Players"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Compare players",
    description="""
        Retrieve comparison data for players <br><br>
        Example: ?player_id1=13ddc856&player_id2=8f2b4c6d (max 2 players) <br>
        player_id1 = 13ddc856 <br>
        player_id2 = 18d5f9e8 <br>
    """
)
def compare_players(
    player_id1: str = Query(..., description="Player IDs, máximo 2"),
    player_id2: str = Query(None, description="Player IDs, máximo 2"),
    db: db_dependency = db_dependency
):
    player1 = db.query(Player_general).filter(Player_general.player_id == player_id1).first()
    player2 = db.query(Player_general).filter(Player_general.player_id == player_id2).first()

    if not player1 or not player2:
        raise HTTPException(status_code=404, detail="Players not found")
    else:
        players = [player1, player2]

    result = []
    for player in players:
        player_id = player.player_id
        fm24_data = get_player_fm24_data(db, player_id)
        performance_data = get_player_performance(db, player_id)

        player_data = {
            "player": player,
            "fm24_data": fm24_data,
            "performance_data": performance_data,
        }

        result.append(player_data)

    return result