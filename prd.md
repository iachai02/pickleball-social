# Rally - Product Requirements Document

> **Status**: Draft v1.0
> **Author**: Immanuel Chai
> **Last Updated**: 2026-02-05

---

## 1. Overview

**App Name**: Rally

**Mission**: Make it effortless for pickleball players of any skill level to find people to play with, build community, and fall deeper in love with the sport.

**Vision**: Rally becomes the default app every pickleball player has on their phone -- not because they have to, but because it's where their pickleball life happens. In 3 years, "rally up" is a verb meaning "let's get a game going."

**Launch Strategy**: Single-city launch (city TBD, based on where we have the strongest local connections). Build density before expanding.

---

## 2. Problem Statement

### What's Broken Today

Pickleball is the fastest-growing sport in America, attracting players from every age group and skill level thanks to its incredibly low barrier to entry. Yet the experience of actually *finding people to play with* is stuck in the dark ages.

Most players rely on group texts with the same 6 friends, scroll through disorganized Facebook Groups hoping someone posted a game near them, or simply show up at public courts and pray there's an open spot. Each of these workarounds breaks in its own way: group texts exclude new players, Facebook Groups are noisy and hard to search, and showing up blind wastes time and leads to mismatched skill levels.

The apps that do exist have leaned hard into the competitive tracking space -- ELO ratings, DUPR scores, match history spreadsheets. They serve the tournament grinder but completely ignore the casual player who just wants to hit with someone new on a Tuesday evening. Worse, they look and feel like utility software from 2015 -- cluttered interfaces, no personality, zero sense of community.

There's a gap: a beautiful, social-first app that treats pickleball as a community sport, not just a competitive one.

### Competitive Landscape

| App/Solution | What They Do | Why They Fail |
|---|---|---|
| DUPR | Official rating system for competitive players, tracks match results | Over-indexes on ELO/competition, cluttered UI, feels like a database not a community, intimidating for casual players |
| Pickleplay | Court finder and session scheduling | Sparse user base, lacks social features, looks dated and generic |
| PlayTime Scheduler | Scheduling tool for court reservations | Pure utility -- no community, no discovery, no personality |
| Facebook Groups | Local communities post game times and court availability | Noisy, hard to search, posts get buried, no structure for organizing games, no profiles |
| Group Texts | Friends coordinate games via iMessage/WhatsApp | Excludes new players, doesn't scale, impossible to discover open games beyond your circle |

---

## 3. Target Users

### Primary Persona: Alex (The Social Player)

- **Age**: 25-40
- **Play Frequency**: 2-3 times per week
- **Skill Level**: Intermediate (3.0-3.5)
- **Primary Pain Point**: Moved to a new city, knows nobody who plays. Wants to find regular playing partners but doesn't know where to start beyond awkwardly showing up at courts alone.
- **Current Workaround**: Scrolls local Facebook Groups, sometimes drives to popular courts hoping to get picked up for a game. Hit or miss.
- **What They Want**: Open the app, see who's playing nearby today, join a game, make friends, do it again next week.

### Secondary Persona: Maria (The Community Organizer)

- **Age**: 35-55
- **Play Frequency**: 4-5 times per week
- **Skill Level**: Advanced (4.0+)
- **Primary Pain Point**: Runs a weekly round robin at her local rec center. Currently manages it through a spreadsheet and a WhatsApp group of 40+ people. It's a mess -- people flake, she can't track who's coming, and new players don't know how to join.
- **Current Workaround**: WhatsApp group + Google Sheets + manual bracket creation
- **What They Want**: A single place to organize events, manage signups, run brackets, and grow her community.

### Tertiary Persona: Jake (The Competitor)

- **Age**: 20-30
- **Play Frequency**: 5+ times per week
- **Skill Level**: Advanced/Pro (4.5+)
- **Primary Pain Point**: Wants to track improvement, find similarly ranked opponents, and compete in local tournaments -- but existing apps feel sterile and disconnected from the broader community.
- **What They Want**: Ranked play, stats, leaderboards -- but within an app he actually enjoys using.

---

## 4. Core Value Proposition

> "Unlike DUPR and Pickleplay, Rally is built around community and discovery -- making it dead simple to find your next game, your next partner, or your next tournament, all inside an app that actually looks and feels like it was made in this decade."

### Design Pillars

1. **Social-First**: Every feature connects people. Finding a game isn't a search query -- it's joining a group of real people with profiles, photos, and play styles. The feed isn't an afterthought -- it's where the community comes alive.

2. **Beautiful by Default**: Anti-clutter, anti-spreadsheet. Clean typography, intentional whitespace, smooth animations. When someone opens Rally, it should feel like opening Instagram, not filing taxes.

3. **Community Over Competition**: Rankings and stats exist, but they're opt-in and secondary. The default experience celebrates playing, not winning. A casual doubles game with friends is treated with the same importance as a tournament final.

---

## 5. Feature Roadmap

### Phase 1: Find People to Play (MVP)

**Goal**: Solve the core matchmaking problem. A user should be able to find and join a game within 2 minutes of opening the app.

| Feature | Description | Why It Matters |
|---|---|---|
| Player Profiles | Photo, name, skill level (self-reported: Beginner/Intermediate/Advanced), home court(s), play style (casual/competitive), member since, reliability score | People join games with people, not slots. Profiles build trust and help you decide who to play with. |
| Court Discovery | Map-based view of nearby courts (10-mile default radius) seeded from Google Places API. Users can submit corrections and add missing courts. Details include public/private, number of courts, amenities. | Players need to know WHERE to play. Pre-seeding courts means the app has value on day 1. |
| Game Creation (Quick Post) | Minimal required fields: court, date/time, player count (2 or 4). Optional: skill range, notes ("Friendly doubles, all levels welcome!"). Create a game in under 30 seconds. | Low friction = more games posted. The easier it is to create, the more games exist for others to find. |
| Game Discovery & Join | Browse open games within 10-mile radius, filter by date/skill/distance, one-tap join, see who else is in (profile previews) | Removes the friction of finding a game. No more scrolling Facebook or sending 10 texts. |
| Notifications & Reminders | Essential notifications only: game confirmations, reminders (1 hour before), someone joins/leaves your game, chat messages in your games. No marketing or social notifications. | Reduces no-shows without being annoying. Respects user attention. |
| Game Chat | Auto-created group chat per game, visible only to joined players, lives inside the game detail screen. For coordinating logistics (which court, bringing balls, running late). | Players need to communicate once a game is set. Scoped to the game keeps it contained -- no noise. |
| No-Show Handling | Soft reputation system: track attendance as a "reliability score" shown subtly on profiles ("Shows up 95% of the time"). No punishment, just transparency. Game creators can see it. | Builds accountability without being punitive. Trust signals help strangers feel comfortable joining. |

**Navigation**: Bottom tab bar with 5 tabs: Home (game feed), Map (court discovery), + Create (new game), Chat (game chats), Profile.

**Authentication**: Apple Sign-In + Google Sign-In + Email/password (via Supabase Auth). Apple Sign-In is required for iOS App Store when offering social login.

---

### Phase 2: Social Feed + Live Presence

**Goal**: Give players a reason to open the app even when they're not looking for a game. Build connection and community identity.

| Feature | Description |
|---|---|
| Post Creation | Share photos, game recaps, highlights, court reviews, or just thoughts about pickleball |
| Follow System | Follow players, courts, and local communities to curate your feed |
| Reactions & Comments | Engage with posts -- celebrate wins, welcome new players, share tips |
| Game Recaps | Auto-generated post after a completed game ("Alex played doubles at Riverside Park with 3 others") |
| Court Check-ins | "I'm at [court] right now!" -- manual check-in button for spontaneous games (saved from MVP to here to manage scope) |

---

### Phase 3: Tournaments

**Goal**: Let anyone create and run a tournament -- from a casual 8-person friend group bracket to a 64-player competitive event.

| Feature | Description |
|---|---|
| Tournament Creation | Set format (single elimination, double elimination, round robin), skill range, player cap, entry fee (optional), date/location |
| Registration & Seeding | Players sign up, organizer seeds or uses auto-seeding based on skill level |
| Live Brackets | Real-time bracket updates as matches are reported |
| Score Reporting | Players or organizers report match scores, with opponent confirmation |
| Tournament Feed | Each tournament gets its own mini-feed for updates, trash talk, and highlights |

---

### Phase 4: Gamification & Ranks

**Goal**: Add progression and motivation without turning the app into a spreadsheet. Gamification should feel fun, not clinical.

| Feature | Description |
|---|---|
| Rally Rating | A simple, transparent skill rating that adjusts based on reported match results (lighter-weight than DUPR, but meaningful) |
| Achievements | Unlockable badges: "First Game," "10 Different Partners," "Tournament Champion," "7-Day Streak" |
| Streaks | Play X days/weeks in a row, maintain your streak. Visible on profile. |
| Leaderboards | Local leaderboards (your city, your favorite court) -- not global. Keep it community-sized. |
| Seasonal Challenges | Monthly/seasonal challenges ("Play 20 games this month," "Try 3 new courts") to drive engagement |

---

### Phase 5: AI Features

**Goal**: Use AI where it genuinely adds value -- not as a gimmick, but as a feature that makes the app smarter the more you use it.

| Feature | Value Proposition | Feasibility |
|---|---|---|
| Smart Match Recommendations | "You'd enjoy playing with Sarah -- similar skill level, same home court, overlapping free times" | High -- collaborative filtering on play history, location, and availability |
| AI Game Summaries | After a game, AI generates a fun recap from scores and player reactions ("The comeback kings struck again...") | Medium -- LLM-based text generation from structured data |
| Skill Insights | "Your win rate in doubles is 15% higher than singles. Consider focusing on doubles tournaments." | Medium -- analytics on match history |
| Smart Scheduling | "Based on your group's availability, Thursday 6pm works best for everyone" | High -- calendar/availability optimization |
| Court Recommendations | "Players at your level love Riverside Park on weekday evenings" | High -- aggregated user behavior data |

---

## 6. Tech Stack

### Frontend
- **Framework**: React Native (Expo)
- **Language**: TypeScript
- **Reasoning**: Cross-platform (iOS first, Android later without rewrite), JavaScript/TypeScript ecosystem, massive community, huge job market relevance. Trade-off vs native Swift: slightly less native feel, but dramatically faster development and cross-platform reach.

### Backend
- **Framework**: FastAPI (Python)
- **Language**: Python 3.12+
- **Reasoning**: Leverages existing Python knowledge, excellent async performance, auto-generated OpenAPI/Swagger docs, first-class type hints, and natural fit for AI/ML features in Phase 5. The backend handles business logic, API endpoints, and orchestration.

### API Contract
- **Strategy**: OpenAPI/Swagger auto-generated from FastAPI
- **Frontend Types**: Use `openapi-typescript` to generate TypeScript types from the OpenAPI spec. Ensures type safety across the Python backend and TypeScript frontend without manual synchronization.

### Database
- **Primary**: PostgreSQL (via Supabase)
- **Reasoning**: Supabase provides Postgres + Auth + Realtime + Storage in one platform. Perfect for an MVP -- reduces infrastructure complexity while being production-grade. PostGIS extension handles geospatial queries for court/game discovery within the 10-mile radius.

### Authentication
- **Provider**: Supabase Auth
- **Methods**: Apple Sign-In + Google Sign-In + Email/password
- **Note**: Apple Sign-In is mandatory for iOS App Store when offering any social login option.

### Real-time Features
- **Provider**: Supabase Realtime (built on Phoenix Channels/WebSockets)
- **Use Cases**: Live game updates, game chat messages, notification triggers, bracket updates (Phase 3)

### Additional Services
- **Maps**: React Native Maps + Google Places API (court discovery and seeding)
- **Push Notifications**: Expo Push Notifications (wraps APNs/FCM)
- **Image Storage**: Supabase Storage (profile photos, post images in Phase 2)
- **AI/ML** (Phase 5): Anthropic API or OpenAI API for text generation; custom recommendation models as data grows

---

## 7. Design System

### Visual Direction
- **Style**: Modern & clean (think Airbnb/Strava -- soft shadows, rounded cards, intentional whitespace)
- **Theme**: Dark mode only
- **Primary Brand Color**: Green (court-inspired) -- emerald/teal tones
- **Typography**: Clean, modern sans-serif (not Inter/Arial defaults)

### Design Principles

1. **Clarity Over Cleverness**: Every screen should have one clear purpose. If a user has to think about what to do next, we've failed.

2. **Warm, Not Corporate**: The tone is friendly, casual, and encouraging. Copy should sound like a friend, not a terms of service. Rounded corners, green accents against dark backgrounds, playful micro-interactions.

3. **People, Not Data Points**: Always show faces, names, and personalities. A game listing shows who's playing, not just a time slot. A leaderboard shows people, not just numbers.

4. **Progressive Disclosure**: Don't overwhelm new users. Show the simple path first (find a game, join it). Reveal depth (stats, tournaments, AI features) as they explore.

5. **Fast by Default**: Every action should feel instant. Optimistic UI updates, skeleton loaders, preloaded data. Waiting kills engagement.

---

## 8. Learning Goals

| Phase | Engineering Concepts You'll Master |
|---|---|
| Phase 1 (MVP) | React Native fundamentals (components, hooks, navigation), Expo workflow, TypeScript in practice, user authentication flows (OAuth + email), PostgreSQL schema design, FastAPI endpoint design, OpenAPI type generation, geolocation/maps integration, push notifications, Supabase Realtime subscriptions, project structure and clean architecture |
| Phase 2 (Social) | Infinite scroll/pagination, image upload and optimization, feed algorithms (chronological vs ranked), optimistic UI updates, caching strategies, content moderation basics |
| Phase 3 (Tournaments) | Complex state machines, bracket generation algorithms, transactional database operations, concurrent user updates, conflict resolution |
| Phase 4 (Gamification) | ELO/rating calculation algorithms, leaderboard data structures (sorted sets), caching with Redis, background job processing |
| Phase 5 (AI) | LLM API integration, recommendation systems, prompt engineering, ML model serving, feature engineering from user behavior data |

**Cross-cutting skills across all phases**: Git workflow, code organization and clean architecture, TypeScript + Python best practices, testing strategies (unit/integration/e2e), CI/CD, App Store deployment, monitoring and error tracking.

---

## 9. Success Metrics (MVP)

| Metric | Target | Why This Matters |
|---|---|---|
| Time to first game joined | < 2 minutes from signup | If it takes too long, users won't come back |
| Games created per week (per active user) | 1+ | Shows the core loop is working |
| Game fill rate | > 60% of posted games get enough players | If games stay empty, the app feels dead |
| Day-7 retention | > 30% | Users who come back after a week have formed a habit |
| Avg players per game | 3-4 | Doubles is the most popular format -- games should fill |
| Game creation time | < 30 seconds | Quick post flow must be frictionless |

---

## 10. Decisions Made

Resolved decisions from the planning phase:

- [x] **Skill levels**: Self-reported at signup (Beginner/Intermediate/Advanced). Transition to data-driven ratings in Phase 4.
- [x] **Court data source**: Google Places API seed + user corrections/additions
- [x] **Default radius**: 10 miles for game and court discovery
- [x] **No-show handling**: Soft reputation system (reliability score on profile, no punishment)
- [x] **Navigation pattern**: Bottom tab bar (Home, Map, Create, Chat, Profile)
- [x] **Game creation flow**: Quick post -- minimal required fields, optional details
- [x] **Live presence**: Deferred to Phase 2 (court check-ins)
- [x] **Chat scope**: Game-specific group chat only (no DMs in MVP)
- [x] **Backend framework**: FastAPI (Python)
- [x] **API contract**: OpenAPI auto-generated types
- [x] **Auth methods**: Apple + Google + Email/password
- [x] **Visual direction**: Modern & clean, dark mode only, green brand color
- [x] **Monetization**: Free for now, decide post-traction
- [x] **Launch scope**: Single city (TBD)
- [x] **Push notifications**: Essential only (game confirmations, reminders, join/leave, chat)

## 11. Open Questions

Remaining decisions for future discussion:

- [ ] How do we bootstrap the chicken-and-egg problem? (Seed with local communities? Partner with rec centers? Personal recruitment?)
- [ ] Do we need a web app, or is mobile-only sufficient for MVP?
- [ ] What's the content moderation strategy for the social feed (Phase 2)?
- [ ] Which specific AI provider for Phase 5 (Anthropic vs OpenAI)?
- [ ] How do we handle the transition from self-reported skill levels to data-driven Rally Rating?
- [ ] What specific courts/city will we seed for launch?

---

*This is a living document. Update it as decisions are made and phases are completed.*
