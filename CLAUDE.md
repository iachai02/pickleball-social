# Rally - Pickleball Social App

## Teaching Mode
Always use the `socratic-mentor` agent when helping with this project. The user wants to learn by doing -- guide with questions and hints, don't write code unless explicitly asked. Use the "fix these N things" format for reviews.

## Project Overview
Rally is a social-first pickleball app for finding people to play with. See `prd.md` for the full PRD (v1.0) and `tickets.md` for tracked progress.

## Current State
- **Phase**: Initialization COMPLETE (6/6 tickets done)
- **Next**: MVP feature development -- create tickets for auth flow, profiles API, court discovery, game creation
- **Database**: `profiles` table created in Supabase with `skill_level` and `play_style` ENUMs
- **Migration**: `backend/migrations/001_create_profiles.sql`

## Tech Stack
- **Frontend**: React Native (Expo) + TypeScript (`frontend/`)
- **Backend**: FastAPI (Python) (`backend/`)
- **Database**: Supabase (PostgreSQL) -- cloud project created and connected
- **Auth**: Supabase Auth (Apple + Google + Email)
- **API Contract**: OpenAPI auto-generated from FastAPI → `openapi-typescript` for frontend types
- **Design**: Dark mode only, green (court-inspired) brand color, modern & clean

## Project Structure
```
pickleball-social/
├── .gitignore          (Python + Node + Expo rules)
├── prd.md              (Rally PRD v1.0 -- all decisions made)
├── tickets.md          (ticket tracking)
├── CLAUDE.md           (this file)
├── backend/
│   ├── .venv/          (Python 3.13 virtual environment)
│   ├── .env            (SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY)
│   ├── .env.example
│   ├── main.py         (FastAPI app with GET /health endpoint)
│   ├── requirements.txt (fastapi, uvicorn, supabase, etc.)
│   └── migrations/
│       └── 001_create_profiles.sql
└── frontend/
    ├── .env            (SUPABASE_URL, SUPABASE_ANON_KEY)
    ├── .env.example
    ├── App.tsx         (root component -- blank template)
    ├── app.json        (Expo config)
    ├── index.ts        (entry point, registers root component)
    ├── package.json    (expo, react-native, @supabase/supabase-js)
    └── tsconfig.json   (extends expo base, strict mode)
```

## Commands
- **Backend**: `cd backend && source .venv/bin/activate && uvicorn main:app --reload`
- **Frontend**: `cd frontend && npx expo start` (press `i` for iOS simulator)
- **Swagger UI**: http://localhost:8000/docs (when backend is running)

## Database Schema (Supabase)
- `profiles` table: id (UUID FK→auth.users), first_name, last_name, skill_level (ENUM), play_style (ENUM), reliability_score (FLOAT DEFAULT 100.0), avatar_url (TEXT), home_courts (TEXT[]), bio (TEXT), created_at (TIMESTAMPTZ), updated_at (TIMESTAMPTZ)

## User's Learning Context
- Built a RAG chatbot end-to-end (Cloud SQL, LangGraph, FastAPI, frontend)
- Knows high-level architecture, wants to deeply understand the details and syntax
- Wants to learn: code organization, clean architecture, WHY one approach is better, scalability
- Common issues: editor import errors (fix with Python: Select Interpreter or TS: Restart TS Server), Postgres syntax (single quotes, TIMESTAMPTZ, no trailing commas), file placement (never put code inside .venv/)

## Key PRD Decisions Made
- MVP: "Find people to play with" (matchmaking/discovery)
- Navigation: Bottom tab bar (Home, Map, Create, Chat, Profile)
- Game creation: Quick post (minimal fields, <30 seconds)
- Skill levels: Self-reported (Beginner/Intermediate/Advanced)
- Court data: Google Places API seed + user corrections
- No-show handling: Soft reputation (reliability score)
- Chat: Game-specific group chat only (no DMs in MVP)
- Notifications: Essential only
- Monetization: Free for now
- Launch scope: Single city (TBD)
