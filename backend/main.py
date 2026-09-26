from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import models, schemas

app = FastAPI(title="NexusScout AI Backend")

# When the server starts, it checks if the 'competitors' table exists. If not, it creates it!
Base.metadata.create_all(bind=engine)

#CORS
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Allow the Next.js frontend
    allow_credentials=True,
    allow_methods=["*"], # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"], # Allow all headers
)

#---API Endpoints---

@app.post("/", response_model=schemas.CompetitorResponse)
def create_competitor(competitor: schemas.CompetitorCreate, db: Session = Depends(get_db)):
    # Create a new SQLAlchemy model instance using the validated Pydantic data.
    db_competitor = models.Competitor(**competitor.model_dump())
    
    db.add(db_competitor)
    db.commit()
    
    db.refresh(db_competitor)
    return db_competitor

@app.get("/competitors", response_model=list[schemas.CompetitorResponse])
def read_competitors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    competitors = db.query(models.Competitor).offset(skip).limit(limit).all()
    return competitors
