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
- **Status**: To Do
- **Complexity**: Low
- **Blocked By**: Ticket #1
- **Acceptance Criteria**:
  - [ ] `frontend/` directory exists
  - [ ] `backend/` directory exists
  - [ ] Both contain a README explaining their purpose

---

### Ticket #3: Scaffold FastAPI backend with proper Python project structure
- **Status**: To Do
- **Complexity**: Medium
- **Blocked By**: Ticket #2
- **Acceptance Criteria**:
  - [ ] Python virtual environment created in `backend/`
  - [ ] FastAPI + uvicorn installed
  - [ ] `main.py` with a health check endpoint (`GET /health`)
  - [ ] Server runs with `uvicorn main:app --reload`
  - [ ] Swagger UI accessible at `/docs`
  - [ ] `requirements.txt` or `pyproject.toml` lists dependencies

---

### Ticket #4: Scaffold React Native Expo frontend with TypeScript
- **Status**: To Do
- **Complexity**: Medium
- **Blocked By**: Ticket #2
- **Acceptance Criteria**:
  - [ ] Expo app scaffolded inside `frontend/`
  - [ ] TypeScript configured
  - [ ] App runs on iOS simulator
  - [ ] Understand what each generated file does

---

### Ticket #5: Set up Supabase project and configure environment variables
- **Status**: To Do
- **Complexity**: Medium
- **Blocked By**: Ticket #3, Ticket #4
- **Acceptance Criteria**:
  - [ ] Supabase project created (cloud or local)
  - [ ] `.env` files created for both frontend and backend with Supabase URL + anon key
  - [ ] `.env.example` files created (without real values) for reference
  - [ ] Supabase client libraries installed in both projects
  - [ ] Connection verified (can ping Supabase from both frontend and backend)

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
#2 (folder structure)
 |
 +----------+
 |          |
 v          v
#3 FastAPI  #4 Expo
 |          |
 +----------+
      |
      v
#5 Supabase setup
      |
      v
#6 User profiles schema
```
