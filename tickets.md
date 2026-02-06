# Rally - Project Tickets

## Project Initialization

### Ticket #1: Initialize Git repo and create comprehensive .gitignore
- **Status**: Done
- **Complexity**: Low
- **Blocked By**: --
- **Acceptance Criteria**:
  - [x] .gitignore exists at repo root
  - [x] Covers Python rules (__pycache__/, .venv, *.pyc, .env)
  - [x] Covers Node rules (node_modules/, .env, dist/, build/)
  - [x] Covers Expo rules (.expo/)
  - [x] Covers macOS rules (.DS_Store)

---

### Ticket #2: Create monorepo folder structure (frontend/ and backend/)
- **Status**: Done
- **Complexity**: Low
- **Blocked By**: Ticket #1
- **Acceptance Criteria**:
  - [x] `frontend/` directory exists
  - [x] `backend/` directory exists

---

### Ticket #3: Scaffold FastAPI backend with proper Python project structure
- **Status**: Done
- **Complexity**: Medium
- **Blocked By**: Ticket #2
- **Acceptance Criteria**:
  - [x] Python virtual environment created in `backend/`
  - [x] FastAPI + uvicorn installed
  - [x] `main.py` with a health check endpoint (`GET /health`)
  - [x] Server runs with `uvicorn main:app --reload`
  - [x] Swagger UI accessible at `/docs`
  - [x] `requirements.txt` lists dependencies

---

### Ticket #4: Scaffold React Native Expo frontend with TypeScript
- **Status**: Done
- **Complexity**: Medium
- **Blocked By**: Ticket #2
- **Acceptance Criteria**:
  - [x] Expo app scaffolded inside `frontend/`
  - [x] TypeScript configured
  - [x] App runs on iOS simulator
  - [x] Understand what each generated file does

---

### Ticket #5: Set up Supabase project and configure environment variables
- **Status**: Done
- **Complexity**: Medium
- **Blocked By**: Ticket #3, Ticket #4
- **Acceptance Criteria**:
  - [x] Supabase project created (cloud)
  - [x] `.env` files created for both frontend and backend with Supabase URL + anon key
  - [x] `.env.example` files created (without real values) for reference
  - [x] Supabase client libraries installed in both projects
  - [x] Backend: `supabase==2.27.3`
  - [x] Frontend: `@supabase/supabase-js: ^2.95.2`

---

### Ticket #6: Create initial database schema for user profiles
- **Status**: To Do
- **Complexity**: Medium
- **Blocked By**: Ticket #5
- **Acceptance Criteria**:
  - [ ] `profiles` table created in Supabase with fields: id, email, display_name, avatar_url, skill_level (enum: beginner/intermediate/advanced), play_style (enum: casual/competitive), home_courts, bio, reliability_score, created_at, updated_at
  - [ ] SQL migration written and saved in repo
  - [ ] Can insert and query a test profile

---

## Dependency Flow

```
#1 (.gitignore)  <-- DONE
 |
 v
#2 (folder structure)  <-- DONE
 |
 +----------+
 |          |
 v          v
#3 FastAPI  #4 Expo
 (DONE)     (DONE)
 |          |
 +----------+
      |
      v
#5 Supabase setup  <-- DONE
      |
      v
#6 User profiles schema  <-- UP NEXT
```
