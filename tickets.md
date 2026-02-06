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
- **Status**: Done
- **Complexity**: Medium
- **Blocked By**: Ticket #5
- **Acceptance Criteria**:
  - [x] `profiles` table created in Supabase with ENUM types for skill_level and play_style
  - [x] SQL migration written and saved in `backend/migrations/001_create_profiles.sql`
  - [x] Can insert and query a test profile

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
#6 User profiles schema  <-- DONE
```

## ALL INITIALIZATION TICKETS COMPLETE

---
---

## MVP Foundation

### Ticket #7: Structure the FastAPI Backend with Clean Architecture
- **Status**: Done
- **Complexity**: Medium
- **Blocked By**: Ticket #6
- **System Design Lesson**: **Layered Architecture & Separation of Concerns** -- Why we separate code into layers (API, schemas, services, core). What happens if you put database queries directly in route handlers? What if you need that same query logic in two different endpoints?
- **Acceptance Criteria**:
  - [ ] Create a `backend/app/` directory as the main application package
  - [ ] Move the FastAPI app initialization to `backend/app/main.py`
  - [ ] Create the following subdirectories (empty `__init__.py` files for now):
    - `app/api/` -- will contain route handlers (endpoints)
    - `app/api/v1/` -- versioned API routes
    - `app/schemas/` -- Pydantic models for request/response validation
    - `app/services/` -- business logic layer
    - `app/core/` -- configuration, dependencies, shared utilities
  - [ ] Create `app/core/config.py` that loads environment variables using Pydantic Settings
  - [ ] Health check endpoint still works at `GET /health`
  - [ ] Update the run command to work with the new structure
- **Think about**: Why might we want a separate `schemas/` directory instead of putting Pydantic models in the route file? Look at how FastAPI's documentation structures larger applications ("Bigger Applications - Multiple Files").

---

### Ticket #8: Create Pydantic Schemas for the Profile Resource
- **Status**: Done
- **Complexity**: Medium
- **Blocked By**: Ticket #7
- **System Design Lesson**: **Data Transfer Objects (DTOs) & API Contract Design** -- Your API response shape should NOT match your database schema. The DTO pattern gives you a translation layer between internal data and external API contract. Change your database? Update the translation. The API stays stable.
- **Acceptance Criteria**:
  - [ ] Create `app/schemas/profile.py` with the following models:
    - `ProfileCreate` -- what the client sends when creating/completing a profile
    - `ProfileUpdate` -- what the client sends when updating (all fields optional)
    - `ProfileResponse` -- what the API returns to the client
  - [ ] Skill level and play style should be validated against allowed values
  - [ ] `ProfileResponse` should NOT include sensitive fields (if any exist)
  - [ ] `ProfileResponse` should include a computed `full_name` field
  - [ ] All schemas should have example values for OpenAPI documentation
  - [ ] Models use proper Python type hints
- **Think about**: Why separate `ProfileCreate` and `ProfileUpdate` schemas instead of one `Profile` schema? What's the difference between `Optional[str]` (field might not exist) vs `str | None` (field exists but might be null)?

---

### Ticket #9: Implement the Profile Service Layer
- **Status**: Done
- **Complexity**: Medium
- **Blocked By**: Ticket #8
- **System Design Lesson**: **Service Layer Pattern & Dependency Injection** -- Route handlers should be "thin" (parse request, call service, return response). Services should be "fat" (contain logic, coordinate DB operations, enforce business rules). What if you later add a CLI tool that creates profiles for testing? With logic in routes, you'd duplicate code. With a service layer, the CLI calls the same service.
- **Acceptance Criteria**:
  - [ ] Create `app/services/profile_service.py` with a `ProfileService` class
  - [ ] Methods to implement:
    - `get_profile(user_id: UUID) -> Profile | None`
    - `create_profile(user_id: UUID, data: ProfileCreate) -> Profile`
    - `update_profile(user_id: UUID, data: ProfileUpdate) -> Profile`
  - [ ] Service uses the Supabase client to interact with the database
  - [ ] Service methods accept and return domain objects (Pydantic models), NOT raw dictionaries
  - [ ] Proper error handling for database failures and not-found cases
- **Think about**: Your service returns `Profile | None` for `get_profile`. What should happen in the route handler when `None` is returned? Who is responsible for converting that to an HTTP 404? Read FastAPI docs on "Dependencies" -- `Depends()` is how you'll wire this up.

---

### Ticket #10: Create the Profile API Routes (CRUD Endpoints)
- **Status**: Done
- **Complexity**: Medium
- **Blocked By**: Ticket #9
- **System Design Lesson**: **RESTful Resource Design** -- Design your API around your domain, not your database tables. In Rally, you don't "create a profile" -- you complete YOUR profile. The `/me` endpoint is a common pattern for "the currently authenticated user's resource."
- **Acceptance Criteria**:
  - [ ] Create `app/api/v1/profiles.py` with a FastAPI router
  - [ ] Implement these endpoints:
    - `GET /api/v1/profiles/me` -- get the current user's profile
    - `PUT /api/v1/profiles/me` -- create or update the current user's profile
    - `GET /api/v1/profiles/{user_id}` -- get another user's profile (public view)
  - [ ] Routes use the `ProfileService` via dependency injection
  - [ ] Proper HTTP status codes:
    - 200 for successful GET/PUT
    - 404 when profile doesn't exist
    - 422 for validation errors (automatic from Pydantic)
  - [ ] Register the router in `app/main.py` with the `/api/v1` prefix
  - [ ] OpenAPI docs show all endpoints with example requests/responses
- **Think about**: Why `PUT` instead of `POST` + `PATCH`? What's the semantic difference? (Hint: idempotency) Should `GET /profiles/{user_id}` return the same data as `GET /profiles/me`? What if reliability_score should only be visible to game organizers?

---

### Ticket #11: Implement JWT Authentication Middleware
- **Status**: Open
- **Complexity**: High
- **Blocked By**: Ticket #10
- **System Design Lesson**: **Authentication vs Authorization & JWT Mechanics** -- Authentication = "Who are you?" (JWT proves identity). Authorization = "What can you do?" (permissions). A JWT has three parts (header.payload.signature) -- you're VERIFYING the signature, not decrypting it. The payload is base64-encoded, readable by anyone.
- **Acceptance Criteria**:
  - [ ] Create `app/core/auth.py` with authentication utilities
  - [ ] Implement a `get_current_user` dependency that:
    - Extracts the JWT from the `Authorization: Bearer <token>` header
    - Validates the JWT signature against Supabase's JWT secret
    - Extracts the user ID from the token payload
    - Raises 401 Unauthorized if token is missing/invalid/expired
  - [ ] Profile routes (`/me` endpoints) require authentication
  - [ ] Public routes (`GET /profiles/{user_id}`) do NOT require authentication
  - [ ] The health check endpoint remains public
- **Think about**: Where should auth logic live? Middleware (every request) vs per-route dependency (opt-in) vs decorator -- what are the tradeoffs? How will you ensure you don't accidentally leave a sensitive endpoint unprotected? Supabase's JWT secret is in your project settings -- store it in `.env`.

---

### Ticket #12: Set Up React Native Navigation Structure
- **Status**: Open
- **Complexity**: Medium
- **Blocked By**: Ticket #4
- **System Design Lesson**: **Navigation as Information Architecture** -- Navigation defines state management (what persists on tab switch?), deep linking (can someone share a link to a game?), performance (lazy-loaded vs all mounted?), and user flows (Create Game = modal or screen?).
- **Acceptance Criteria**:
  - [ ] Install `@react-navigation/native` and required dependencies
  - [ ] Install `@react-navigation/bottom-tabs` for tab navigation
  - [ ] Create the following directory structure in `frontend/`:
    - `src/navigation/` -- navigation configuration
    - `src/screens/` -- screen components
    - `src/components/` -- shared components
  - [ ] Implement bottom tab navigator with 5 tabs:
    - Home (game feed) -- placeholder screen
    - Map (court discovery) -- placeholder screen
    - Create (new game) -- placeholder screen
    - Chat (game chats) -- placeholder screen
    - Profile -- placeholder screen
  - [ ] Each placeholder screen shows the screen name and a basic layout
  - [ ] Tab bar uses icons (Expo vector icons) and labels
  - [ ] Active tab is visually distinguished
  - [ ] Navigation works -- tapping tabs switches screens
- **Think about**: The PRD says Create is a "+" button in the center. But it's not really a "tab" -- it's an action that opens a modal. How will you handle this? Chat and Home will need nested navigators (list -> detail). Read React Navigation docs on "Nesting navigators" before starting.

---

### Ticket #13: Implement Supabase Auth Flow in React Native
- **Status**: Open
- **Complexity**: High
- **Blocked By**: Ticket #12
- **System Design Lesson**: **Auth State as Global State & Secure Token Storage** -- Auth is one of the few truly global state pieces. React Context makes sense here. Subtleties: JWT expiry/refresh, secure encrypted storage on mobile (not AsyncStorage!), race conditions (user taps button before auth state restores).
- **Acceptance Criteria**:
  - [ ] Create `src/lib/supabase.ts` with properly configured Supabase client
  - [ ] Implement secure token storage (Expo SecureStore, not AsyncStorage)
  - [ ] Create an `AuthProvider` context that:
    - Tracks authentication state (loading, authenticated, user object)
    - Exposes sign-in, sign-up, and sign-out methods
    - Automatically restores sessions on app launch
    - Listens for auth state changes (token refresh, sign out from another device)
  - [ ] Create a basic sign-in screen with email/password
  - [ ] App shows sign-in screen when unauthenticated, main tabs when authenticated
  - [ ] After signing in, the user object is available throughout the app
  - [ ] Signing out returns to the sign-in screen
- **Think about**: Why SecureStore instead of AsyncStorage? What's the threat model? The loading state is critical -- your app shouldn't flash the sign-in screen before checking for a valid session. How do you handle this? Start with email/password; Apple and Google Sign-In add native SDK complexity.

---

### Ticket #14: Connect Frontend to Backend - First API Call
- **Status**: Open
- **Complexity**: Medium
- **Blocked By**: Ticket #11, Ticket #13
- **System Design Lesson**: **The API Contract & End-to-End Type Safety** -- FastAPI auto-generates OpenAPI spec from Python type hints. `openapi-typescript` generates TS types from that spec. If the backend changes, TypeScript catches the mismatch. This is the schema-first approach -- the alternative (manual types on both sides) leads to subtle sync bugs.
- **Acceptance Criteria**:
  - [ ] Generate TypeScript types from your FastAPI OpenAPI spec using `openapi-typescript`
  - [ ] Create `src/lib/api.ts` with a configured HTTP client (fetch or axios)
  - [ ] API client automatically attaches the auth token to requests
  - [ ] Implement `getMyProfile()` and `updateMyProfile()` API functions
  - [ ] Profile screen calls the API and displays the current user's profile data
  - [ ] Loading and error states are handled in the UI
  - [ ] If no profile exists yet, show a "Complete your profile" prompt
- **Think about**: Where does the generated types file live? Should you check it into git or regenerate as part of the build? What happens when an API call fails? Network error vs 401 vs 404 vs 500 all need different handling -- where does that logic live?

---

## Dependency Flow (Tickets #7-14)

```
INITIALIZATION COMPLETE (Tickets #1-6)
            |
            +---------------------------+
            |                           |
            v                           v
    #7 (Backend Structure)      #12 (Navigation)
            |                           |
            v                           v
    #8 (Pydantic Schemas)       #13 (Supabase Auth Flow)
            |                           |
            v                           |
    #9 (Profile Service)                |
            |                           |
            v                           |
    #10 (Profile API Routes)            |
            |                           |
            v                           |
    #11 (JWT Auth Middleware)            |
            |                           |
            +---------------------------+
                        |
                        v
             #14 (Connect FE to BE)
```

**Parallel work opportunity**: Backend (#7-11) and Frontend (#12-13) are independent tracks. #14 is where they converge.

## Check Your Understanding Before Starting

1. What's the difference between a **route handler** and a **service method**?
2. Why do we have separate `ProfileCreate`, `ProfileUpdate`, and `ProfileResponse` schemas?
3. What does a JWT contain, and what does "validating" a JWT actually mean?
4. Why use dependency injection (`Depends()`) instead of importing the service directly?
5. What's the difference between authentication and authorization?
