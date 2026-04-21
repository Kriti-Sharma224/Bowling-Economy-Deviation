from fastapi import FastAPI
from schemas import EconomyInput, EconomyOutput
from services import calculate_economy_deviation

app = FastAPI(title="Bowling Economy Deviation API - Advanced")

@app.get("/")
def home():
    return {"message": "Advanced Bowling Economy API is running"}

@app.post("/economy/deviation", response_model=EconomyOutput)
def economy_deviation(payload: EconomyInput):
    return calculate_economy_deviation(payload)