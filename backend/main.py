"""Animeverse API starter. Local demo gameplay currently runs in webapp/app.js."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Animeverse API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/health")
async def health():
    return {"ok": True, "service": "animeverse-api", "version": "0.1.0"}

@app.get("/api/v1/game-config")
async def game_config():
    return {"name": "ANIMEVERSE", "season": 1, "status": "prototype", "features": ["collection", "summoning", "deck-building", "turn-based-combat"]}
