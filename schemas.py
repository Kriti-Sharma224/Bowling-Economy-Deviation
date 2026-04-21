from pydantic import BaseModel, Field
from typing import List, Optional

class BowlerData(BaseModel):
    runs_conceded: float = Field(..., ge=0)
    balls_bowled: float = Field(..., gt=0)
    phase: Optional[str] = Field(default="middle")  # powerplay, middle, death

class EconomyInput(BaseModel):
    bowler: BowlerData
    population: List[BowlerData]

class EconomyOutput(BaseModel):
    bowler_economy: float
    adjusted_economy: float
    population_mean: float
    population_spread: float
    deviation_score: float
    confidence_score: float
    interpretation: str