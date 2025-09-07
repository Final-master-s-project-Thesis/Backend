from fastapi import APIRouter, status, HTTPException
from dependencies.dependencies import db_dependency
from models import League

router = APIRouter(
    prefix="/leagues",
    tags=["Get data of Leagues"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Get all leagues",
    description="Retrieve a list of all leagues available in the database.",
)
def get_leagues(db: db_dependency):
    leagues = db.query(League).distinct().all()
    return leagues
