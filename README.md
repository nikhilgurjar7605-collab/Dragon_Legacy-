# ANIMEVERSE — Riftbound

A mobile-first anime multiverse card RPG prototype for Telegram WebApp.

## Project archive

The complete source bundle is provided in `animeverse-alpha.zip`. Extract it to obtain the `animeverse/` project directory.

## Stack
- WebApp: HTML, CSS and JavaScript
- Backend scaffold: Python + FastAPI
- Telegram bot scaffold: Python + aiogram

## Current status
This is an alpha prototype. Summoning, collection, deck building and local battle gameplay are demo features. Production Telegram authentication, MongoDB persistence, multiplayer services and deployment configuration still need implementation.

## Local WebApp preview
Extract the archive, then run:

```bash
cd animeverse/webapp
python -m http.server 5173
```

Open `http://localhost:5173`.
