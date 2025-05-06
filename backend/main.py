from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, courses
from app.db import engine, Base  # match your structure
from app.models import user  # import your models so SQLAlchemy sees them

Base.metadata.create_all(bind=engine)

app = FastAPI()

# ★ CORS setup ★
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your Vite dev server origin
    allow_credentials=True,
    allow_methods=["*"],     # allow GET, POST, OPTIONS, etc.
    allow_headers=["*"],     # allow Authorization, Content-Type, etc.
)

# Optional root
@app.get("/")
def read_root():
    return {"message": "SSE backend running"}

# Routers
app.include_router(auth.router)
app.include_router(courses.router)
