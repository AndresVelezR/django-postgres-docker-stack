# Django + PostgreSQL + Nginx (Dockerized)

## Project overview
Docker Compose stack that runs a Django application behind Nginx with PostgreSQL for persistent storage. The application implements a minimal user registration flow with server-side validations and database-backed persistence.

## Functional scope
- Create a user with a unique `nombre_usuario`
- Validate empty input and duplicate usernames
- List registered users ordered by creation time
- Persist user data in PostgreSQL

## High-level architecture
- **Django**: application runtime and request handling (runs on port 8000 inside the network).
- **PostgreSQL**: primary data store, exposed on port 5432.
- **Nginx**: reverse proxy and static/media file server, exposed on port 80.
- **Docker Compose**: orchestrates the three services, shared network, and volumes (`postgres_data`, `static_volume`, `media_volume`).

## Repository structure
```
.
├── backend
│   ├── Dockerfile              # Django application image definition
│   ├── manage.py               # Django management entry point
│   ├── requirements.txt        # Python dependencies
│   ├── media                   # User-uploaded media files
│   ├── staticfiles             # Collected static assets
│   ├── usuario_project         # Django project configuration
│   │   ├── asgi.py              # ASGI entry point
│   │   ├── settings.py          # Django settings
│   │   ├── urls.py              # Root URL configuration
│   │   └── wsgi.py              # WSGI entry point
│   └── usuarios                # Domain app: user registration
│       ├── admin.py             # Django admin configuration
│       ├── apps.py              # App configuration
│       ├── migrations           # Database migrations
│       ├── models.py            # Database models
│       ├── templates            # HTML templates
│       │   └── usuarios
│       │       └── formulario.html
│       ├── urls.py              # App-level routing
│       └── views.py             # Request handling logic
├── docker-compose.yml          # Multi-container orchestration
├── nginx
│   ├── Dockerfile              # Nginx image definition
│   └── nginx.conf              # Nginx reverse proxy configuration
├── screenshots                 # Execution and persistence evidence
└── README.md                   # Project documentation
```

## Prerequisites
- Docker
- Docker Compose

## How to run the project
```
docker compose up --build
```

To stop and remove containers while keeping volumes:
```
docker compose down
```

## How to access the application
- Open `http://localhost/` (served by Nginx on port 80)
- Django admin is available at `http://localhost/admin/` (requires a Django superuser created inside the container)

## Verify PostgreSQL persistence
The database credentials and name are defined in `.env`. Using the current values:

Open a psql shell inside the database container:
```
docker compose exec db psql -U usuario_django -d usuarios_db
```

From the psql prompt, you can verify the `usuarios` table and data:
```
\dt
SELECT count(*) FROM usuarios;
SELECT nombre_usuario, fecha_creacion FROM usuarios ORDER BY fecha_creacion DESC;
```

You can also execute a one-off query without entering the psql prompt:
```
docker compose exec db psql -U usuario_django -d usuarios_db -c "SELECT count(*) FROM usuarios;"
```

## Evidence
- The `screenshots/` directory is reserved for evidence assets related to the application UI or runtime behavior.

## Operational commands (Docker Compose)
```
docker compose up -d --build
docker compose ps
docker compose logs -f
docker compose restart
docker compose stop
docker compose down
```

## Conclusion
This repository provides a production-oriented Docker Compose stack for a Django user registration application with PostgreSQL persistence and Nginx as the HTTP entrypoint and static/media server.
