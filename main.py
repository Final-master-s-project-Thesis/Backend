from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
import routes

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Configuración de CORS
app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:4200"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(routes.country_router)
app.include_router(routes.league_router)
app.include_router(routes.club_router)
app.include_router(routes.players_router)
app.include_router(routes.compare_router)
