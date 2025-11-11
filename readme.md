# Journal Articles Backend (Django)

A Django REST API backend for a journal article publishing system. Provides user accounts, article submission, peer review workflow, editorial management, and public article access with search and pagination.

## Features
- JWT / token-based authentication
- Roles: Author, Reviewer, Editor, Admin
- Article CRUD with versioning and status (draft, submitted, under review, accepted, rejected, published)
- Submission and assignment workflows for peer review
- Reviews, comments, and editorial decisions
- File uploads (manuscripts, supplementary files)
- Search, filtering, sorting, and pagination
- Internationalization-ready and configurable email notifications
- Tests and CI-ready

## Tech stack
- Python 3.10+ (recommended)
- Django 4.x
- Django REST Framework
- PostgreSQL or

## Quick start (development)

1. Clone and open project
    ```bash
    git clone https://github.com/Chukseo/journalBack
    ```

2. Create virtual environment and install
    ```bash
    python -m venv .venv
    source .venv/Scripts/activate  
    pip install -r requirements.txt
    ```

3. Create `.env` (example)
    ```
    DEBUG=True
    SECRET_KEY=replace-with-secret
    DATABASE_URL=postgres://user:pass@localhost:5432/journal_db
    EMAIL_HOST=smtp.example.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=...
    EMAIL_HOST_PASSWORD=...
    ```

4. Apply migrations and create superuser
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

5. Run development server
    ```bash
    python manage.py runserver
    ```

## Docker (optional)
- Build and run with docker-compose:
  ```bash
  docker-compose up --build
  ```

## Tests
- Run test suite:
  ```bash
  pytest
  # or
  python manage.py test
  ```

## Important management commands
- Collect static files:
  ```bash
  python manage.py collectstatic --noinput
  ```
- Rebuild search index (if configured):
  ```bash
  python manage.py rebuild_index
  ```

## Configuration & env vars
- SECRET_KEY
- DEBUG
- DATABASE_URL or standard DATABASES config
- EMAIL_* settings
- MEDIA_ROOT / MEDIA_URL and file storage backend
- CELERY / Redis settings if async tasks are used

## API (high level)
- Auth
  - POST /api/auth/token/ (login)
  - POST /api/auth/token/refresh/
  - POST /api/auth/register/
- Articles
  - GET /api/articles/ (list, search, filter, pagination)
  - POST /api/articles/ (create — author)
  - GET /api/articles/{id}/
  - PUT/PATCH /api/articles/{id}/
  - DELETE /api/articles/{id}/
- Submissions & workflow
  - POST /api/submissions/ (submit manuscript)
  - POST /api/submissions/{id}/assign-reviewer/
  - POST /api/submissions/{id}/decision/ (editor actions)
- Reviews & comments
  - POST /api/reviews/
  - GET /api/reviews/?submission={id}

(For exact endpoint names, request/response schemas and permissions, consult the API schema or the browsable API in development.)

## Security
- Rotate SECRET_KEY and credentials.
- Use HTTPS in production.
- Configure CORS and allowed hosts.
- Store sensitive settings outside source control.

## License
MIT — see LICENSE file.

## Contact / Maintainers
- Project maintainers: chuks@ugtf.org

