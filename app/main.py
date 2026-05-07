from fastapi import FastAPI
from app.database import engine
from app.models import user
from app.routes import auth
from fastapi.middleware.cors import CORSMiddleware

user.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # untuk dev, bebas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)