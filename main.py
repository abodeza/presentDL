# Imports
from pydantic import BaseModel
from fastapi import FastAPI
import logging

from model import *


# Defining model input schema using pydantic
class ModelInput(BaseModel):
    
    # This matches what is above
    Make: str # e.g. toyota 
    Model: str # e.g. camry
    Year: int # e.g. 2016
    Mileage: float # e.g. 251861.71000
    Cylinders: int # e.g. 4
    Condition: str # e.g. Engine repaired
    Rear_camera: int # e.g. 1
    Navigation_system: int # e.g. 0
    Leather_seats: int # e.g. 1
    Sunroof: int # e.g. 0
    cruise_control: int # e.g. 0
    Bluetooth: int # e.g. 0



# Creating FastAPI endpoint
app = FastAPI()

@app.get("/")
def home():
    return {"You're not": "supposed to be here!"}

@app.post("/predict")
def return_prediction(input: ModelInput):
    return {"prediction": predict(input.model_dump())}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
