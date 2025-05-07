# Changelog

## [Unreleased]

## [Day 7] – 2025‑05‑13
- **Backend**
  - Added `GET /api/courses` endpoint
  - Added `POST /api/enrollments` endpoint with duplicate‑check
- **Frontend**
  - Implemented `Catalog.jsx` to fetch & list courses
  - “Enroll” button posts to `/api/enrollments` and toggles to “Enrolled!”

## [Day 6] – 2025‑05‑12
- **Frontend**
  - Scaffolded Vite + React app
  - Added `ProtectedRoute` component and login redirect
- **Backend**
  - Fixed CORS preflight errors
  - Unified `Base` across `db.py` and `models/`
  - Generated Alembic migration for `users` & `courses` tables

## [Day 5] – 2025‑05‑09
- **Backend**
  - Implemented `POST /api/register`, `/api/login`
  - Implemented protected `POST /api/courses`
- **Tests**
  - Added `pytest` suite for auth and course‑creation

## [Day 4] – 2025‑05‑08
- **Backend**
  - Defined SQLAlchemy models & Alembic migrations
  - Setup `.env`, `db.py`, and initial schema

## [Day 3] – 2025‑05‑07
- **Planning**
  - Tech‑stack diagram (`docs/architecture.png`)
  - Monorepo scaffold (`backend/`, `frontend/`, `docs/`)

## [Day 2] – 2025‑05‑06
- **Wireframes**
  - Login, course catalog, course detail, topic detail, instructor dashboard ASCII mockups

## [Day 1] – 2025‑05‑05
- **Specifications**
  - Created `docs/project-spec.md` with overview, roles, models, and key flows
