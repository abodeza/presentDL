import requests

if __name__ == "__main__":
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
    
    predicted_price = requests.post("http://127.0.0.1:8000/predict", json=data).json()["prediction"]
    print(f"well, the prediction is: {predicted_price}")
