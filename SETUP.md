# AbsenIN API - Setup Guide

## 🚀 Quick Setup (Development)

### Prerequisites
- Python 3.8+
- MySQL 5.7+ atau MariaDB 10.3+
- Git

### Setup Steps

1. **Clone Repository**
```bash
git clone <repository-url>
cd API-absenIN
```

2. **Create Virtual Environment**
```bash
python -m venv .venv
```

3. **Activate Virtual Environment**
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

5. **Setup Environment Variables**
```bash
# Copy .env.example to .env
cp .env.example .env

# Edit .env dengan konfigurasi database Anda
```

6. **Create Database**
```sql
CREATE DATABASE absenin CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

7. **Run Migrations**
```bash
python -m alembic upgrade head
```

8. **Seed Database (Optional)**
```bash
python -m app.seed
```

9. **Run Server**
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

10. **Access API**
- Server: http://localhost:8000
- Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 🐳 Docker Setup (Production Ready)

### Using Docker Compose

1. **Build and Run**
```bash
docker-compose up -d
```

2. **Run Migrations**
```bash
docker-compose exec api python -m alembic upgrade head
```

3. **Seed Database**
```bash
docker-compose exec api python -m app.seed
```

4. **Access API**
- Server: http://localhost:8000
- Docs: http://localhost:8000/docs

### Stop Services
```bash
docker-compose down
```

---

## 🌐 Production Deployment

### Environment Variables (Production)

Edit `.env` untuk production:
```env
# Database
DATABASE_URL=mysql+pymysql://user:password@host:3306/dbname

# JWT
SECRET_KEY=<generate-secure-key>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application
APP_NAME=AbsenIN API
APP_DEBUG=False
```

### Generate Secure Secret Key
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Run with Gunicorn (Production)
```bash
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

---

## 📦 Deployment Platforms

### Heroku
```bash
# Install Heroku CLI
heroku login
heroku create absenin-api

# Add MySQL addon
heroku addons:create jawsdb:kitefin

# Set environment variables
heroku config:set SECRET_KEY=<your-secret-key>

# Deploy
git push heroku main

# Run migrations
heroku run python -m alembic upgrade head

# Seed database
heroku run python -m app.seed
```

### Railway
1. Connect GitHub repository
2. Add MySQL database
3. Set environment variables
4. Deploy automatically

### DigitalOcean App Platform
1. Connect GitHub repository
2. Add MySQL database
3. Set environment variables
4. Deploy

---

## 🔧 Troubleshooting

### Database Connection Error
```bash
# Check MySQL is running
mysql -u root -p

# Test connection
python -c "from app.database import engine; engine.connect(); print('Connected!')"
```

### Migration Error
```bash
# Reset migrations (CAUTION: Deletes all data)
python -m alembic downgrade base
python -m alembic upgrade head
```

### Port Already in Use
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8000 | xargs kill -9
```

---

## 📚 Documentation

- **API Documentation**: `/docs` (Swagger UI)
- **Alternative Docs**: `/redoc` (ReDoc)
- **Request Guide**: `API_REQUEST_GUIDE.md`
- **Validation Errors**: `VALIDATION_ERRORS.md`

---

## 🔐 Default Credentials

After seeding:
- **Email**: dosen@absenin.local
- **Password**: dosen123

**⚠️ Change in production!**

---

## 📝 Notes

- Virtual environment (`.venv/`) is not committed to git
- Always run migrations after pulling new changes
- Keep `.env` file secure and never commit it
- Use `.env.example` as template

---

## 🆘 Support

For issues, check:
1. `TROUBLESHOOTING.md`
2. `VALIDATION_ERRORS.md`
3. GitHub Issues
