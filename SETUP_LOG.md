# NexusOps Enterprise - Setup Log

**Developer:** Jason Lamichhane  
**Project:** NexusOps Enterprise  
**Phase:** Phase 0 - Environment & Infrastructure Setup

---

# 1. Windows Development Environment

## WSL2 Installation

Opened PowerShell as Administrator:

```powershell
wsl --install -d Ubuntu
```

Verified:

```powershell
wsl -l -v
```

Confirmed:

```text
Ubuntu VERSION 2
```

---

# 2. Docker Installation

Installed Docker Desktop for Windows.

Configured:

- WSL2 backend
- Ubuntu integration

Verification:

```bash
docker --version
docker compose version
docker run hello-world
```

Result:

```text
Hello from Docker!
```

---

# 3. VS Code Setup

Installed:

- WSL
- Python
- Docker
- GitLens
- PostgreSQL

Opened project inside WSL:

```bash
code .
```

---

# 4. Git and GitHub Setup

Configured git:

```bash
git config --global user.name "Jason Lamichhane"
git config --global user.email "YOUR_EMAIL"
```

Generated SSH key:

```bash
ssh-keygen -t ed25519
```

Added public key to GitHub.

Verified:

```bash
ssh -T git@github.com
```

Result:

```text
Hi jasonlamichhane! You've successfully authenticated.
```

---

# 5. Project Creation

Repository:

```text
nexusops-enterprise
```

Project location:

```text
/home/jason/projects/nexusops-enterprise
```

Initial structure:

```text
nexusops-enterprise
├── backend
├── frontend
├── README.md
├── .gitignore
├── .gitattributes
└── .env.example
```

---

# 6. Initial Git Commit

```bash
git init
git branch -M main
git add .
git commit -m "chore: initialize repo with project structure"
```

---

# 7. Python Virtual Environment

Created virtual environment:

```bash
cd backend

python3 -m venv .venv

source .venv/bin/activate
```

Prompt became:

```text
(.venv)
```

---

# 8. Backend Dependencies

Installed:

```bash
pip install django
pip install djangorestframework
pip install "psycopg[binary]"
pip install django-environ
```

Saved:

```bash
pip freeze > requirements.txt
```

Installed packages:

```text
Django
djangorestframework
psycopg
psycopg-binary
django-environ
```

---

# 9. Django Project

Created project:

```bash
django-admin startproject config .
```

Created application:

```bash
python manage.py startapp core
```

Added apps:

```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    "core",
]
```

---

# 10. Environment Variables

Created:

```text
.env
.env.example
```

Variables:

```env
DJANGO_SECRET_KEY=
DJANGO_DEBUG=
DJANGO_ALLOWED_HOSTS=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```

Configured django-environ.

---

# 11. Docker Setup

Created:

```text
backend/Dockerfile
backend/.dockerignore
docker-compose.yml
```

Services:

```text
backend
db (postgres)
```

Volume:

```text
pgdata
```

---

# 12. PostgreSQL Setup

Environment:

```env
POSTGRES_DB=nexusops
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

Changed Django database configuration from SQLite:

```python
django.db.backends.sqlite3
```

to PostgreSQL:

```python
django.db.backends.postgresql
```

using environment variables.

---

# 13. Docker Verification

Validated compose:

```bash
docker compose config
```

Started services:

```bash
docker compose up --build
```

Verified:

```bash
docker compose ps
```

Result:

```text
backend: Up
db: Up (healthy)
```

---

# 14. Migration Verification

Executed:

```bash
docker compose exec backend python manage.py migrate
```

Verified:

```bash
docker compose exec backend python manage.py showmigrations
```

All default migrations:

```text
admin
auth
contenttypes
sessions
```

successfully applied.

---

# Current Status

Completed:

✅ WSL2  
✅ Ubuntu  
✅ Docker Desktop  
✅ VS Code Integration  
✅ Git & GitHub SSH  
✅ Django Project  
✅ DRF Installation  
✅ PostgreSQL Container  
✅ Docker Compose  
✅ Environment Variables  
✅ Django ↔ PostgreSQL Connection  

Current Phase:

```text
Phase 0 - Infrastructure Setup
```

Next Phase:

```text
Health Endpoint
Database Design
RBAC
Employees
Departments
Leave Module
Expense Module
```

---

# Common Commands

Start stack:

```bash
docker compose up -d
```

View containers:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs backend
```

Run migrations:

```bash
docker compose exec backend python manage.py migrate
```

Open shell:

```bash
docker compose exec backend python manage.py shell
```

Stop stack:

```bash
docker compose down
```