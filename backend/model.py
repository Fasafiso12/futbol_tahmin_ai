import numpy as np

def predict_score(home_team, away_team):
    home_goals = np.random.randint(0, 5)
    away_goals = np.random.randint(0, 5)
    return {"home_team": home_team, "away_team": away_team,
            "home_goals": home_goals, "away_goals": away_goals}
