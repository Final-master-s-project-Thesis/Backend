from fastapi import APIRouter, status, HTTPException
from dependencies.dependencies import db_dependency
from models import Country

router = APIRouter(
    prefix="/countries",
    tags=["Get data of Countries"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Get all countries",
    description="Retrieve a list of all countries available in the database.",
)
def get_countries(db: db_dependency):
    countries = db.query(Country).distinct().all()
    return countries