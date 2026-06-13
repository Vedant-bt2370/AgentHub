from fastapi import FastAPI

from api.auth import router as auth_router
from api.chat import router as chat_router
from api.health import router as health_router
from database.postgres import Base, engine
from models.user import User
from models.chat import Chat



Base.metadata.create_all(bind=engine)

app = FastAPI(title="AgentHub")

app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(health_router)