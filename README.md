# Expose Gym 2.0

A production-minded Django gym management application. This first milestone establishes the Django project, PostgreSQL-ready configuration, initial management models, Django Admin, and a responsive data-driven marketing homepage based on the supplied visual reference.

## Run locally

```bash
cd /Users/gouthamms/Documents/Codex/2026-10-05/li
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python app/manage.py migrate
.venv/bin/python app/manage.py runserver
```

Open `http://127.0.0.1:8000/`. Create an administrator with:

```bash
.venv/bin/python app/manage.py createsuperuser
```

Then open `http://127.0.0.1:8000/admin/` to manage gym data.

## PostgreSQL configuration

For this initial local setup, the project automatically uses SQLite when `DATABASE_NAME` is not supplied. This makes the first run work without a database server. For PostgreSQL, create a `.env` file from `.env.example`, export its variables, and run migrations:

```bash
export DATABASE_NAME=expose_gym
export DATABASE_USER=expose_gym
export DATABASE_PASSWORD='your-password'
export DATABASE_HOST=127.0.0.1
export DATABASE_PORT=5432
.venv/bin/python app/manage.py migrate
```

The database credentials are never committed. Docker and deployment infrastructure are intentionally deferred until the local application feature set is complete.

## Run with Docker Compose

```bash
cp .env.example .env
# Set a strong DATABASE_PASSWORD and SECRET_KEY in .env first.
docker compose up --build
```

Open `http://127.0.0.1:8000/`. Stop containers with `docker compose down`; add `-v` only if you intentionally want to delete the PostgreSQL data volume.

## Verify

```bash
.venv/bin/python app/manage.py check
.venv/bin/python app/manage.py test gym
.venv/bin/python app/manage.py collectstatic --noinput
```

## First milestone contents

- Core gym models: members, trainers, services, plans, classes, bookings, contacts, gallery, and homepage features.
- Admin screens with list filters and search for managing operational data.
- Reusable base, navbar, and footer templates.
- Responsive homepage, including dynamic service, trainer, and class blocks populated from the database.
- A copied brand asset at `static/images/expose-gym-brand.png`.

## Next application milestone

Build the individual public pages, contact and membership forms, Django authentication, member dashboard, and booking-capacity workflow. Containerization and AWS/Terraform/CI/CD come after that end-to-end local flow is working.
