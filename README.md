# LifeOS

A personal productivity dashboard built with Django. Currently in early development.

## Current Features

- Login page with glassmorphism UI
- Home dashboard with navigation
- Interactive code graph explorer (D3.js)

## Tech Stack

- **Backend:** Django 6.0.2
- **Database:** PostgreSQL
- **Frontend:** Bootstrap 5, D3.js
- **Font:** Nunito Sans (Google Fonts)

---

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/Grey-PeaCock/Task-Manager.git
cd Task-Manager
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL

Install PostgreSQL from https://www.postgresql.org/download/ then create a database:

```sql
CREATE DATABASE lifeos;
```

### 5. Create a `.env` file in the project root

```bash
DJANGO_SECRET_KEY=your-secret-key-here
DB_NAME=lifeos
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## Project Structure

```
LifeOS/
├── config/             # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/               # Main app
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── templates/          # HTML templates
│   ├── login.html
│   ├── index.html
│   └── graph.html
├── static/
│   ├── css/
│   │   ├── login.css
│   │   └── style.css
│   ├── image/
│   └── large_graph_data.json
├── .env                # Your local environment variables (not committed)
├── manage.py
└── requirements.txt
```

---

## URL Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | `home_page` | Dashboard homepage |
| `/login/` | `login_page` | Login page |
| `/logout/` | `LogoutView` | Logout |
| `/graph/` | `GraphView` | Code graph explorer |
| `/admin/` | Django Admin | Admin panel |

---

## Notes

- Never commit your `.env` file — it's in `.gitignore`
- `DEBUG = True` — do not deploy with this setting enabled
- Generate a new `SECRET_KEY` for production

---

## Roadmap

- [ ] Login form authentication wired up
- [ ] User profile page
- [ ] Notes module
- [ ] Tasks / Todo module
- [ ] Habit tracker
