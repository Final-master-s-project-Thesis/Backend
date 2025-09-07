from fastapi import APIRouter, status, HTTPException
from dependencies.dependencies import db_dependency
from models import Club

router = APIRouter(
    prefix="/clubs",
    tags=["Get data of Clubs"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Get all clubs",
    description="Retrieve a list of all clubs available in the database.",
)
def get_clubs(db: db_dependency):
    clubs = db.query(Club).distinct().all()
    return clubs
