import joblib 
from fastapi import FastAPI

model = joblib.load("Mental_Health_Model1.pkl")

app = FastAPI()

