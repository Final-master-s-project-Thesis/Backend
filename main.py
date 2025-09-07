from fastapi import FastAPI
from database import engine, Base
import models
import routes

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(routes.country_router)
app.include_router(routes.league_router)
app.include_router(routes.club_router)
app.include_router(routes.players_router)
app.include_router(routes.compare_router)
