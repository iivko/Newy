# Newy

A small Django project for testing deployment.

## 🧱 Stack

- **Django** — Python web framework  
- **Tailwind CSS** — Utility-first styling  
- **Mailgun** — Email sending service  
- **PostgreSQL** — Database  
- **Docker Compose** — Development environment  
- **Railway (optional)** — Deployment & managed Postgres  

---

## 🚀 Setup with Docker

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/newy.git
cd newy
```

### 2. Create a `.env` File

Docker reads environment variables from a `.env` file. This project includes a `.env.example` file with all the required variables. Create a real `.env` file by copying it:

```bash
cp .env.example .env
```

Now edit .env and fill in the values.

### 3. Start Docker Services
Use Docker Compose to build and start your app:
```bash
docker compose up --build
```
This will:

- Build the Django app image from the Dockerfile

- Start both the web and db containers

- Install Python dependencies

- Set up a volume for persistent Postgres storage

Once running, the app is available at:

📍 http://localhost:8000

---

## 🔨 Common Commands (Inside Docker)
Run Django commands inside the web container:
```bash
# Apply database migrations
docker compose exec web python manage.py migrate

# Create an admin user
docker compose exec web python manage.py createsuperuser

# Run the development server manually (optional)
docker compose exec web python manage.py runserver 0.0.0.0:8000

```