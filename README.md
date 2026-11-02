# ANIMEVERSE — Riftbound (Alpha 0.1)

A mobile-first anime multiverse card RPG prototype for Telegram + WebApp.

## Project layout
- `webapp/`: responsive browser game client
- `backend/`: FastAPI health/config scaffold
- `bot/`: aiogram Telegram launcher scaffold
- `requirements.txt`: Python dependencies

## Play the WebApp locally
```bash
cd webapp
python -m http.server 5173
```
Visit http://localhost:5173.

## Run the API scaffold
```bash
python -m venv .venv
# Activate the environment, then:
pip install -r requirements.txt
uvicorn backend.main:app --reload
```
Health endpoint: http://127.0.0.1:8000/health

## Run the Telegram bot scaffold
Set `BOT_TOKEN` and `WEBAPP_URL`, then run:
```bash
python bot/main.py
```
Configure the bot's Web App domain with BotFather and use the deployed HTTPS URL.

## Alpha features
- Responsive game dashboard and mobile navigation
- Original placeholder character codex with inspectable cards and stats
- Local demo summoning (single and tenfold)
- Five-character formation builder
- Turn-based arena combat with attack, skill, defend and ultimate actions
- Enemy encounters, rewards, XP and level-ups
- Dimension map preview and player profile
- Browser localStorage save, export and reset

## Important limitations
This is a playable front-end prototype, not a production multiplayer game. Player data is stored locally in the browser. Summoning, combat and rewards are client-side demo logic. The API is currently a health/config scaffold; MongoDB, Redis, Telegram init-data verification, server-authoritative combat, trading, matchmaking, guilds and anti-cheat must be implemented before public launch. Never use the client-side demo economy or combat for real-money purchases.

## Art and IP
Characters are original placeholder concepts. Use original or properly licensed character IP and artwork for a public release.
