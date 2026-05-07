# 🚀 Deployment Guide - AbsenIN API

Panduan lengkap untuk deploy AbsenIN API ke production.

## 📋 Prerequisites

- Python 3.8+
- MySQL 8.0+
- Git
- (Optional) Docker & Docker Compose

---

## 🔧 Setup Development

### 1. Clone Repository
```bash
git clone <repository-url>
cd API-absenIN
```

### 2. Setup Environment

**Windows**:
```bash
setup.bat
```

**Linux/Mac**:
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Configure Database
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # Linux/Mac

# Update DATABASE_URL
DATABASE_URL=mysql+pymysql://user:password@localhost/absenin
```

### 4. Create Database
```sql
CREATE DATABASE absenin CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 5. Run Migrations
```bash
# Windows
.venv\Scripts\python.exe -m alembic upgrade head

# Linux/Mac
source .venv/bin/activate
python -m alembic upgrade head
```

### 6. Seed Database (Optional)
```bash
# Windows
.venv\Scripts\python.exe -m app.seed

# Linux/Mac
python -m app.seed
```

### 7. Start Server
```bash
# Windows
start.bat

# Linux/Mac
./start.sh
```

Server akan berjalan di: http://localhost:8000

---

## 🐳 Deploy dengan Docker

### 1. Setup Environment
```bash
cp .env.docker .env
# Edit .env dan sesuaikan konfigurasi
```

### 2. Build & Run
```bash
docker-compose up -d
```

### 3. Check Logs
```bash
docker-compose logs -f api
```

### 4. Run Migrations
```bash
docker-compose exec api alembic upgrade head
```

### 5. Seed Database
```bash
docker-compose exec api python -m app.seed
```

### 6. Stop Services
```bash
docker-compose down
```

---

## 🌐 Deploy ke Production Server

### Option 1: Manual Deployment

#### 1. Setup Server
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3 python3-pip python3-venv mysql-server nginx -y
```

#### 2. Clone & Setup
```bash
cd /var/www
git clone <repository-url> absenin-api
cd absenin-api

# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-prod.txt
```

#### 3. Configure Environment
```bash
cp .env.production .env
nano .env

# Update values:
DATABASE_URL=mysql+pymysql://user:password@localhost/absenin
SECRET_KEY=<generate-random-32-chars>
APP_DEBUG=False
ALLOWED_ORIGINS=https://yourdomain.com
```

#### 4. Setup Database
```bash
# Create database
mysql -u root -p
CREATE DATABASE absenin CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'absenin_user'@'localhost' IDENTIFIED BY 'strong_password';
GRANT ALL PRIVILEGES ON absenin.* TO 'absenin_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# Run migrations
python -m alembic upgrade head

# Seed data
python -m app.seed
```

#### 5. Setup Systemd Service
```bash
sudo nano /etc/systemd/system/absenin-api.service
```

Paste configuration:
```ini
[Unit]
Description=AbsenIN API
After=network.target mysql.service

[Service]
Type=notify
User=www-data
Group=www-data
WorkingDirectory=/var/www/absenin-api
Environment="PATH=/var/www/absenin-api/.venv/bin"
ExecStart=/var/www/absenin-api/.venv/bin/gunicorn app.main:app \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --access-logfile /var/www/absenin-api/logs/access.log \
    --error-logfile /var/www/absenin-api/logs/error.log
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable & start service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable absenin-api
sudo systemctl start absenin-api
sudo systemctl status absenin-api
```

#### 6. Setup Nginx Reverse Proxy
```bash
sudo nano /etc/nginx/sites-available/absenin-api
```

Paste configuration:
```nginx
server {
    listen 80;
    server_name api.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/absenin-api /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 7. Setup SSL with Let's Encrypt
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d api.yourdomain.com
```

---

### Option 2: Deploy dengan Docker di Production

#### 1. Install Docker
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

#### 2. Clone & Configure
```bash
git clone <repository-url> absenin-api
cd absenin-api
cp .env.docker .env
nano .env  # Update production values
```

#### 3. Deploy
```bash
docker-compose -f docker-compose.yml up -d
```

#### 4. Setup Nginx (same as manual deployment)

---

## 🔄 Update Deployment

### Manual Update
```bash
cd /var/www/absenin-api
git pull origin main
source .venv/bin/activate
pip install -r requirements.txt
python -m alembic upgrade head
sudo systemctl restart absenin-api
```

### Docker Update
```bash
cd absenin-api
git pull origin main
docker-compose down
docker-compose build
docker-compose up -d
```

---

## 📊 Monitoring

### Check Service Status
```bash
sudo systemctl status absenin-api
```

### View Logs
```bash
# Application logs
tail -f /var/www/absenin-api/logs/error.log
tail -f /var/www/absenin-api/logs/access.log

# Systemd logs
sudo journalctl -u absenin-api -f

# Docker logs
docker-compose logs -f api
```

### Health Check
```bash
curl http://localhost:8000/health
```

---

## 🔒 Security Checklist

- [ ] Change SECRET_KEY to random 32+ characters
- [ ] Set APP_DEBUG=False in production
- [ ] Use strong database password
- [ ] Configure ALLOWED_ORIGINS properly
- [ ] Enable SSL/HTTPS
- [ ] Setup firewall (ufw/iptables)
- [ ] Regular backups
- [ ] Keep dependencies updated
- [ ] Monitor logs regularly

---

## 🆘 Troubleshooting

### Service won't start
```bash
sudo systemctl status absenin-api
sudo journalctl -u absenin-api -n 50
```

### Database connection error
```bash
# Check MySQL is running
sudo systemctl status mysql

# Test connection
mysql -u absenin_user -p absenin
```

### Permission errors
```bash
sudo chown -R www-data:www-data /var/www/absenin-api
sudo chmod -R 755 /var/www/absenin-api
```

---

## 📚 Additional Resources

- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Docker Documentation](https://docs.docker.com/)

---

**Deployment guide lengkap! Pilih metode yang sesuai dengan kebutuhan Anda.** 🚀
