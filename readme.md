# FastAPI Authentication and Posts API

A FastAPI application organized into separate modules for authentication, user registration, login, and posts.

## Project Structure

```text
fastAPI_project_2/
├── alembic/             # Database migration files
├── router/
│   ├── login.py         # Login routes
│   ├── posts.py         # Post-related routes
│   └── register.py      # User registration routes
├── .env                 # Local environment configuration
├── .gitignore           # Files excluded from version control
├── alembic.ini          # Alembic configuration
├── auth.py              # Authentication logic
├── database.py          # Database connection and session setup
├── main.py              # Application entry point
├── models.py            # Database models
├── readme.md            # Project documentation
├── schemas.py           # Request and response schemas
└── security.py          # Security utilities
```

Local environment folders and generated cache files are omitted from this overview.

## Project Modules

### Authentication

Authentication-related code is organized across:

- `router/register.py` — user registration endpoints.
- `router/login.py` — user login endpoints.
- `auth.py` — authentication logic.
- `security.py` — security-related utilities.

### Posts

`router/posts.py` contains the post-related API routes.

### Database

- `database.py` manages database configuration and connections.
- `models.py` defines database models.
- `schemas.py` defines request and response data structures.
- `alembic/` and `alembic.ini` contain database migration configuration.

## Getting Started

### 1. Clone the Repository

Replace the placeholder with your repository URL:

### 1. Clone the Repository

```bash
git clone [https://github.com/Melak-tefera/fastAPI_project_2.git](https://github.com/Melak-tefera/fastAPI_project_2.git)
cd fastAPI_project_2
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS / Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the packages required by the project.


### 4. Configure Environment Variables

Create a `.env` file in the project root and add the configuration values used by your application.

Check `database.py`, `auth.py`, and `security.py` for the exact variable names and required settings.

> Do not commit real credentials, database passwords, or secret keys.

### 5. Apply Database Migrations

After configuring the database and Alembic connection:

```bash
alembic upgrade head
```

### 6. Start the Application

If the FastAPI instance in `main.py` is named `app`, run:

```bash
uvicorn main:app --reload
```

The local server will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

With FastAPI's default documentation settings, open:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

Use the interactive documentation to inspect the registered endpoints, request bodies, and response schemas.

## API Route Organization

| Module | Purpose |
|---|---|
| `router/register.py` | User registration |
| `router/login.py` | User login |
| `router/posts.py` | Post-related operations |

The exact endpoint paths and HTTP methods depend on the route definitions and prefixes configured in the application.

## Development Notes

- Register the routers in `main.py`.
- Keep database models in `models.py`.
- Keep request and response schemas in `schemas.py`.
- Keep authentication and security logic separate from route handlers.
- Create database migrations when changing the database schema.
- Use `--reload` for local development.

## Version Control

Ensure `.gitignore` excludes local configuration and generated files, including:

```gitignore
.venv/
__pycache__/
*.pyc
.env
```

## License

Add the project's license information here.