from pydantic import BaseModel
from scraper import scrape_website
from agent import analyze_competitor
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

    db_competitor = models.Competitor(**competitor.model_dump())
    
    db.add(db_competitor)
    db.commit()
    
    db.refresh(db_competitor)
    return db_competitor

@app.get("/competitors", response_model=list[schemas.CompetitorResponse])
def read_competitors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    competitors = db.query(models.Competitor).offset(skip).limit(limit).all()
    return competitors

   
class ScanRequest(BaseModel):
    url: str

@app.post("/scan")
async def scan_competitor(request: ScanRequest, db: Session = Depends(get_db)):
    url = request.url
    
    raw_text = await scrape_website(url)
    if "Error" in raw_text or len(raw_text) < 100:
        raise HTTPException(status_code=400, detail="Failed to scrape website.")
        
    analysis = await analyze_competitor(raw_text)
    
    competitor = db.query(models.Competitor).filter(models.Competitor.url == url).first()
    if competitor:
        competitor.analysis = analysis
        db.commit()
        db.refresh(competitor)
    
    return {"analysis": analysis}