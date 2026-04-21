ADMIN HANDOVER DOCUMENTation — Bowling Economy Deviation API

1. API Name:
Bowling Economy Deviation API (Advanced Context-Aware Model)

2. Objective:
This API evaluates a bowler’s performance by comparing their economy rate against a relevant population (match or dataset).
Instead of reporting absolute economy, the API measures relative performance, determining whether the bowler is performing above or below the competitive baseline.
The model incorporates contextual adjustments (match phase) and a confidence score to ensure the output reflects both performance and reliability.

3. Scientific Principle Used:
* Statistical Deviation (Z-score concept)
Measures how far a bowler’s performance lies from the population mean relative to the spread.
* Sample Standard Deviation (n-1)
Used to estimate variability when working with sample data.
* Contextual Normalization
Adjusts economy using match-phase-based weighting.
* Uncertainty Modeling
Confidence score based on number of balls bowled.

4. Input Fields and Data Types:
Request Model: EconomyInput
Field	Type	Description
bowler.runs_conceded	float	Runs conceded by the bowler
bowler.balls_bowled	float	Number of legal deliveries
bowler.phase	string	Match phase ("powerplay", "middle", "death")
population	list	List of other bowlers
population[].runs_conceded	float	Runs conceded
population[].balls_bowled	float	Balls bowled
population[].phase	string	Match phase

5. Derived Variables and Their Meaning:
Variable	Meaning
p (Bowler Economy)	Runs per over of the bowler
p_adjusted	Economy adjusted using phase weight
q (Population Mean)	Average adjusted economy of all bowlers
r (Population Spread)	Sample standard deviation of population
z (Deviation Score)	Measures relative performance vs population
confidence_score	Indicates reliability based on sample size

6. Final Output Fields and Their Meaning:
Field	Description
bowler_economy	Raw economy rate
adjusted_economy	Economy after phase adjustment
population_mean	Average economy of population
population_spread	Variability of economies
deviation_score	Relative performance score
confidence_score	Reliability of the metric
interpretation	Human-readable performance category

7. Example Request:
{
  "bowler": {
    "runs_conceded": 28,
    "balls_bowled": 24,
    "phase": "death"
  },
  "population": [
    {"runs_conceded": 30, "balls_bowled": 24, "phase": "powerplay"},
    {"runs_conceded": 45, "balls_bowled": 36, "phase": "middle"},
    {"runs_conceded": 20, "balls_bowled": 18, "phase": "death"}
  ]
}

8. Example Response:
{
  "bowler_economy": 7.0,
  "adjusted_economy": 6.3,
  "population_mean": 7.8,
  "population_spread": 1.2,
  "deviation_score": 1.25,
  "confidence_score": 0.4,
  "interpretation": "Above average performance"
}

9. Validation Errors:
balls_bowled <= 0 → Invalid input
population size < 2 → Insufficient comparison data
Negative values for runs or balls → Invalid
Missing required fields → Request rejected

10. Assumptions Made:
Phase weights are heuristic (domain-based), not absolute scientific constants
Population represents a valid comparison group (same match or context)
Economy is calculated using only legal deliveries
Confidence score is approximated using ball count
All bowlers are treated equally (no opposition or pitch adjustment yet)

11. Any New Model Fields or Models Proposed:
New Model: BowlerData
Introduced to standardize bowler input structure
New Fields Added:
phase → Enables contextual weighting
confidence_score → Adds uncertainty awareness
adjusted_economy → Reflects contextual performance
Enhancements:
Raw data modeling (runs + balls instead of precomputed economy)
Sample standard deviation instead of population SD
Context-aware performance evaluation

12. Final Note:

This API goes beyond traditional score-based evaluation by introducing context-aware statistical comparison, ensuring that a bowler’s performance is interpreted relative to match conditions and population variability.

It is designed to be analytically robust, interpretable, and integration-ready.
