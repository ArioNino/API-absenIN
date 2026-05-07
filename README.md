# AbsenIN API

API backend untuk sistem manajemen absensi mahasiswa berbasis FastAPI dan MySQL.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MySQL 8.0+
- Git

### Installation

1. **Clone repository**
```bash
git clone <repository-url>
cd API-absenIN
```

2. **Setup environment**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
# Copy .env.example to .env
cp .env.example .env

# Edit .env dengan konfigurasi database Anda
# DATABASE_URL=mysql+pymysql://user:password@localhost/absenin
```

5. **Setup database**
```bash
# Buat database
mysql -u root -p
CREATE DATABASE absenin;
exit;

# Run migrations
alembic upgrade head

# Seed data (optional)
python -m app.seed
```

6. **Run server**
```bash
# Development
uvicorn app.main:app --reload

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Server akan berjalan di: http://localhost:8000

## 📚 API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔐 Default Credentials

Setelah seeding:
- **Email**: dosen@absenin.local
- **Password**: dosen123

## 📁 Project Structure

```
API-absenIN/
├── app/
│   ├── models/          # Database models
│   ├── routes/          # API endpoints
│   ├── schemas/         # Pydantic schemas
│   ├── utils/           # Utilities (auth, security)
│   ├── seeders/         # Database seeders
│   ├── config.py        # Configuration
│   ├── database.py      # Database connection
│   └── main.py          # FastAPI application
├── alembic/             # Database migrations
├── .env.example         # Environment template
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔧 Development

### Create new migration
```bash
alembic revision --autogenerate -m "description"
alembic upgrade head
```

### Run tests
```bash
pytest
```

## 🚀 Deployment

### Using Docker

```bash
docker build -t absenin-api .
docker run -p 8000:8000 absenin-api
```

### Using Docker Compose

```bash
docker-compose up -d
```

### Manual Deployment

1. Setup production environment
2. Configure `.env` with production values
3. Run migrations: `alembic upgrade head`
4. Start with gunicorn: `gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker`

## 📝 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| DATABASE_URL | MySQL connection string | mysql+pymysql://root:password@localhost/absenin |
| SECRET_KEY | JWT secret key | (generate new for production) |
| ALGORITHM | JWT algorithm | HS256 |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiration | 30 |
| APP_NAME | Application name | AbsenIN API |
| APP_DEBUG | Debug mode | True |

## 🔒 Security

- JWT authentication untuk semua endpoints (kecuali login)
- Password hashing dengan bcrypt
- CORS enabled (configure untuk production)
- Input validation dengan Pydantic

## 📖 API Endpoints

### Authentication
- `POST /auth/login` - Login

### Mahasiswa
- `GET /mahasiswa` - List mahasiswa
- `GET /mahasiswa/{id}` - Get by ID
- `GET /mahasiswa/nim/{nim}` - Get by NIM
- `POST /mahasiswa` - Create mahasiswa
- `PUT /mahasiswa/{id}` - Update mahasiswa
- `DELETE /mahasiswa/{id}` - Delete mahasiswa

### Mata Kuliah
- `GET /matakuliah` - List mata kuliah
- `GET /matakuliah/{kode}` - Get by kode
- `POST /matakuliah` - Create mata kuliah
- `PUT /matakuliah/{kode}` - Update mata kuliah
- `DELETE /matakuliah/{kode}` - Delete mata kuliah

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- FastAPI
- SQLAlchemy
- Alembic
