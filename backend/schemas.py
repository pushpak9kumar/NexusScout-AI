from pydantic import BaseModel

class CompetitorCreate(BaseModel):

     name: str
     url: str

class CompetitorResponse(BaseModel):
    id: int
    name: str
    url: str

    model_config = {
        "from_attributes": True
    }    