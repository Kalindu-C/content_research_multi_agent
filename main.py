from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# get user query and start the research
class ResearchRequest(BaseModel):
    query: str

@app.post("/research")
def research(request: ResearchRequest):
    # Start the research process
    return {"message": f"Research started for query: {request.query}"}
