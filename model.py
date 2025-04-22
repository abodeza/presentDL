import pandas as pd
import numpy as np
import pickle
from catboost import CatBoostRegressor
from sklearn.preprocessing import LabelEncoder



def predict(data: dict) -> dict:

    # Input preprocessing
    df = pd.DataFrame([data])
    
    desired_order = ['Make', 'Model', 'Year', 'Mileage', 	'Cylinders', 'Condition', 'Rear_camera',
                      'Navigation_system', 'Leather_seats', 'Sunroof', 'cruise_control', 'Bluetooth']
    df = df[desired_order]
    

    encoder_Model = pickle.load(open("encoders/encoder_Model.pkl", "rb"))
    encoder_Make = pickle.load(open("encoders/encoder_Make.pkl", "rb"))
    encoder_Condition = pickle.load(open("encoders/encoder_Condition.pkl", "rb"))

    df["Model"] = encoder_Model.transform(df["Model"])
    df["Make"] = encoder_Make.transform(df["Make"])
    df["Condition"] = encoder_Condition.transform(df["Condition"])

    
    # Model loading and prediction
    file_name = "saved_model/used_car_price_model_catboost.pkl"
    model =  pickle.load(open(file_name, "rb"))

    prediction = model.predict(df)
    print(f"Prediction is: {prediction}")

    return prediction.item()

if __name__ == "__main__":

    # Test the prediction function
    data = {
        "Make": "toyota",
        "Model": "camry",
        "Year": 2016,
        "Mileage": 251861.71,
        "Cylinders": 4,
        "Condition": "Engine repaired",
        "Rear_camera": 1,
        "Navigation_system": 0,
        "Leather_seats": 1,
        "Sunroof": 0,
        "cruise_control": 0,
        "Bluetooth": 0
    }

    print(predict(data))