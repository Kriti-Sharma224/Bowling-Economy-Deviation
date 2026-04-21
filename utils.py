import math

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_sample_std_dev(data, mean):
    n = len(data)
    if n < 2:
        return 0
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    return math.sqrt(variance)

def calculate_economy(runs, balls):
    return (runs / balls) * 6

def get_phase_weight(phase: str):
    weights = {
        "powerplay": 1.1,
        "middle": 1.0,
        "death": 0.9
    }
    return weights.get(phase, 1.0)

def validate_population(population):
    if len(population) < 2:
        raise ValueError("Population must have at least 2 bowlers")