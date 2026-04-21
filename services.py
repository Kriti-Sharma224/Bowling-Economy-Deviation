from schemas import EconomyInput
from utils import (
    calculate_mean,
    calculate_sample_std_dev,
    calculate_economy,
    get_phase_weight,
    validate_population
)

def calculate_economy_deviation(payload: EconomyInput):

    bowler = payload.bowler
    population = payload.population

    validate_population(population)

    # --- Bowler Economy ---
    base_economy = calculate_economy(bowler.runs_conceded, bowler.balls_bowled)

    # Apply phase weight
    weight = get_phase_weight(bowler.phase)
    adjusted_economy = base_economy * weight

    # --- Population Economies ---
    population_economies = []
    for b in population:
        econ = calculate_economy(b.runs_conceded, b.balls_bowled)
        econ *= get_phase_weight(b.phase)
        population_economies.append(econ)

    # --- Derived Variables ---
    population_mean = calculate_mean(population_economies)
    population_spread = calculate_sample_std_dev(population_economies, population_mean)

    # --- Deviation Score ---
    if population_spread == 0:
        deviation_score = 0
    else:
        deviation_score = (population_mean - adjusted_economy) / population_spread

    # --- Confidence Score (based on balls bowled) ---
    balls = bowler.balls_bowled
    confidence_score = min(balls / 60, 1.0)  # normalized (10 overs = high confidence)

    # --- Interpretation ---
    if deviation_score > 1.5:
        interpretation = "Elite performance"
    elif deviation_score > 0.5:
        interpretation = "Above average performance"
    elif deviation_score > -0.5:
        interpretation = "Average performance"
    else:
        interpretation = "Below average performance"

    return {
        "bowler_economy": round(base_economy, 2),
        "adjusted_economy": round(adjusted_economy, 2),
        "population_mean": round(population_mean, 2),
        "population_spread": round(population_spread, 2),
        "deviation_score": round(deviation_score, 2),
        "confidence_score": round(confidence_score, 2),
        "interpretation": interpretation
    }