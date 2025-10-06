from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="VIP API", description="Returns a list of VIPs", version="1.0.0")

# Example data
class VIP(BaseModel):
    id: int
    name: str
    occupation: str

vips = [
    VIP(id=1, name="Elon Musk", occupation="Entrepreneur"),
    VIP(id=2, name="Taylor Swift", occupation="Singer"),
    VIP(id=3, name="Serena Williams", occupation="Athlete"),
    VIP(id=4, name="Barack Obama", occupation="Former President")
]

@app.get("/vips", response_model=List[VIP])
def get_vips():
    """Return the list of VIPs."""
    return vips
