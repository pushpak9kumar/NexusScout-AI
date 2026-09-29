from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from database import Base

class Competitor(Base):
    __tablename__ = "competitors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String, unique=True, index=True) # <-- Made unique so we can easily find it to update
    
    analysis = Column(Text, nullable=True) # Stores the long AI Markdown report. Nullable=True means existing competitors don't break.

    created_at = Column(DateTime(timezone=True), server_default=func.now())
