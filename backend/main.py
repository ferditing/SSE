from app.db import Base, engine  # match your structure
from app.routes import auth, courses, enrollments  # import your routers
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

# ★ CORS setup ★
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your Vite dev server origin
    allow_credentials=True,
    allow_methods=["*"],  # allow GET, POST, OPTIONS, etc.
    allow_headers=["*"],  # allow Authorization, Content-Type, etc.
)


# Optional root
@app.get("/")
def read_root():
    return {"message": "SSE backend running"}


# Routers
app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(enrollments.router)
