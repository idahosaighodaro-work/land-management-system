from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Database setup
from database import SessionLocal, engine
from models import Base

# Routers
from app.routes.subscription import router as subscription_router
from app.routes.register import router as register_router
from app.routes.login import router as login_router
from app.routes.request import router as request_router
from app.me import router as me_router

# 🔧 Create database tables
Base.metadata.create_all(bind=engine)

# 🚀 Initialize FastAPI app
app = FastAPI(title="EagleEye Backend", version="1.0")

# 🌐 Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📦 Include API routers
app.include_router(register_router, prefix="/api", tags=["Register"])
app.include_router(login_router, prefix="/api", tags=["Login"])
app.include_router(subscription_router, prefix="/api", tags=["Subscription"])
app.include_router(request_router, prefix="/api", tags=["Request"])
app.include_router(me_router, prefix="/api", tags=["User"])


# 🩺 Health check endpoint
@app.get("/", tags=["Health"])
def health_check():
    return {"status": "EagleEye backend is alive"}