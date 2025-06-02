from fastapi import FastAPI
from app import auth, qr, attendance, admin
from app.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(auth.router, prefix="/auth")
app.include_router(qr.router, prefix="/qr")
app.include_router(attendance.router, prefix="/attendance")
app.include_router(admin.router, prefix="/admin")

@app.get("/")
def root():
    return {"message": "Attendance Tracker API"}
