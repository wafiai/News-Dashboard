from fastapi import FastAPI
from pydantic import BaseModel
import joblib as jb
import uvicorn
import requests



vectorizer = jb.load("models/vectorizer.pkl")
model = jb.load("models/model.pkl")
# Loading Model & Vectorizer Because global Varibles load faster

app = FastAPI()

class input(BaseModel):
    text: str 
# Defining Fastapi as app and creatng pydantic 

@app.post("/predict")
def root(data: input):
    vector = vectorizer.transform([data.text])
    mod = model.predict(vector)
    if mod == 1:
        return "World"
    elif mod == 2:
        return "Sports"
    elif mod == 3:
        return "Business"
    elif mod == 4:
        return "Scfi/Tech"

    # 1-World, 2-Sports, 3-Business, 4-Sci/Tech
    # Creating API and Loading model inside


