from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.model import predict_score
import os
import requests

app = FastAPI()

# CORS ayarı
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("API_KEY")  # Backend environment variable

@app.get("/predict/live")
def live_predict(home_team: str = "TeamA", away_team: str = "TeamB"):
    prediction = predict_score(home_team, away_team)
    return prediction

