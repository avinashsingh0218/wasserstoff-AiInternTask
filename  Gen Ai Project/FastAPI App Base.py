from fastapi import FastAPI
from backend.api.routes import router as game_router

app = FastAPI(title="What Beats Rock Game")

app.include_router(game_router, prefix="/game")

@app.get("/")
async def root():
    return {"message": "Welcome to the Gen-AI Game!"}
