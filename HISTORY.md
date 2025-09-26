# Project History — Online Library Exam Project

## Version 1.0 — Initial Setup
**Date:** 21.09.2025  
**Author:** Oleksandr Lapshin  
**Changes:**
- Created Django project `OnlineLibrary`.
- Created apps: `books`, `users`, `comments`.
- Configured PostgreSQL database via Docker.
- Integrated Bootstrap 5.3 for frontend styling.
- Added `base.html` template for consistent layout.

---

## Version 1.1 — Books Models and Admin
**Date:** 22.09.2025  
**Changes:**
- Added `Book` and `Author` models in `books/models.py`.
- Configured Django admin for `Book` and `Author`.
- Uploaded sample books, covers, and PDF files for testing.
- Implemented `book_list` and `book_detail` views.
- Added URL routing in `books/urls.py`.

---

## Version 1.2 — User Authentication & Superuser
**Date:** 23.09.2025  
**Changes:**
- Configured `users` app for login, logout, registration.
- Created superuser `alex_lib_admin` via Docker.
- Verified admin access at `/admin/`.
- Set up token authentication with Django REST Framework.

---

## Version 1.3 — API Endpoints
**Date:** 24.09.2025  
**Changes:**
- Created API endpoints for `books`:
  - `/books/` → list all books
  - `/books/<id>/` → book detail by ID
- Added token authentication for API requests.
- Verified endpoints in browser and Postman.
- Ensured `curl` requests work with Authorization header:
```bash
curl -H "Authorization: Token <your_token>" http://localhost:8080/books/
Version 1.4 — Docker Integration & Testing

Date: 25.09.2025
Changes:

Verified Docker containers for web and database:

onlinelibrary-web-1

onlinelibrary-db-1

Added makemigrations and migrate commands in README for instructor testing.

Added instructions for generating API tokens via drf_create_token.

Confirmed API access works in Postman without errors.

Version 1.5 — Final Documentation

Date: 26.09.2025
Changes:

Created README.md with:

Docker commands for running the project

Instructions for migrations and superuser creation

API endpoints table with examples

Postman testing instructions

Added project history and versioning in PROJECT_HISTORY.md.

Prepared for instructor submission with verified endpoints and working HTML responses.

Notes:

All project changes were committed to GitHub for version control.

The project can be tested entirely via Docker and browser.

API token authentication is required for all endpoints, but responses are currently HTML pages for exam purposes.
## GitHub Branching Strategy

- **main** — stable version with all exam requirements completed.
- **dev** — development branch for implementing new features and testing.
- **feature/<feature_name>** — temporary branches for specific tasks (e.g., `feature/api-endpoints`, `feature/ui-updates`).
- All changes are merged into `dev` after testing, then into `main` for final submission.
- Instructor can check commits and branches on GitHub:
  https://github.com/OleksandrLapshin564/OnlineLibrary
