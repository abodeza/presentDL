import streamlit as st
import pandas as pd
import requests

# -------- Page Config --------
st.set_page_config(page_title="Used Car Price Prediction", page_icon="🚗", layout="wide")

# -------- Custom CSS Styling --------
st.markdown(
    """
    <style>
    header, footer {visibility: hidden;}

    .stApp {
        background: #f9fafc !important;
        font-family: 'Segoe UI', sans-serif !important;
        color: #212121 !important;
        margin: 0;
    }

    .block-container {
        padding: 0 !important;
    }

    h2 {
        text-align: center;
        color: #191a1f !important;
        margin-top: 2rem;
        margin-bottom: 5px;
    }

    p {
        text-align: center;
        font-size: 1.05rem;
        color: #5d6d7e !important;
    }

    .predict-box {
        background: transparent !important;
        border-radius: 12px !important;
        padding: 35px 40px !important;
        margin: auto !important;
        margin-top: 30px !important;
        box-shadow: none !important;
        max-width: 950px;
    }

    [data-testid="stSidebar"] {
        background-color: #708ba1 !important;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    input[type="number"],
    input[type="text"],
    textarea,
    div[data-baseweb="select"] > div {
        background-color: #324556 !important;
        color: white !important;
        border: none !important;
        border-radius: 0px !important;
        height: 40px !important;
        padding: 0 12px !important;
        font-size: 0.95rem !important;
        line-height: 1.5rem !important;
        display: flex !important;
        align-items: center !important;
    }

    div[data-baseweb="select"]:hover > div,
    input[type="number"]:focus,
    input[type="text"]:focus,
    textarea:focus {
        background-color: #89bdc2 !important;
        color: white !important;
        outline: none !important;
        box-shadow: none !important;
        border: none !important;
    }

    div[data-baseweb="select"] * {
        color: white !important;
    }

    /* NEW Stylish Button */
    div.stButton > button {
        background-color: #1f78b4 !important;  /* Vibrant blue */
        color: white !important;
        border: none !important;
        padding: 12px 28px !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        cursor: pointer !important;
        transition: background-color 0.3s ease-in-out !important;
        width: 100% !important;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1) !important;
    }

    div.stButton > button:hover {
        background-color: #125e96 !important;
        color: white !important;
    }

    div.stButton > button:focus {
        outline: none !important;
        box-shadow: 0 0 0 2px #89bdc2 !important;
    }

    .stCheckbox [role="checkbox"] {
        background-color: #324556 !important;
        border-color: #324556 !important;
    }

    .stCheckbox [role="checkbox"]:hover {
        background-color: #89bdc2 !important;
        border-color: #89bdc2 !important;
    }

    .stCheckbox [aria-checked="true"] {
        background-color: #89bdc2 !important;
        border-color: #89bdc2 !important;
    }

    .stCheckbox [role="checkbox"] svg {
        color: white !important;
    }

    label {
        color: #324556 !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        display: flex !important;
        align-items: center !important;
    }

    div.stNumberInput button {
        background-color: #324556 !important;
        color: white !important;
        border: none !important;
        border-radius: 0px !important;
        height: 40px !important;
        width: 40px !important;
        font-size: 1rem !important;
        padding: 0 !important;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    div.stNumberInput button:hover {
        background-color: #89bdc2 !important;
        color: white !important;
    }

    div.stNumberInput button:focus {
        outline: none !important;
    }

    [data-baseweb="tag"] {
        background-color: #89bdc2 !important;
        color: white !important;
    }

    [data-baseweb="input"]:focus-within {
        box-shadow: none !important;
        border-color: #89bdc2 !important;
    }

    [data-baseweb="option"]:hover {
        background-color: #89bdc2 !important;
    }

    [aria-selected="true"] {
        background-color: #89bdc2 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------- Header --------
st.markdown("<h2>Used Car Price Prediction</h2>", unsafe_allow_html=True)
st.markdown("<p>Fill in the details below to get an estimated price for your used car.</p>", unsafe_allow_html=True)

# -------- Loading Select Box Options ---------
if "df" not in st.session_state:
    st.session_state.df = pd.read_pickle("data/unique_make_model.pkl")
    st.session_state.makes = sorted(st.session_state.df["Make"].unique())

selected_make = st.selectbox("Select Make", st.session_state.makes, key="make_selector")

# Store selected make to use for filtering
st.session_state.filtered_models = sorted(
    st.session_state.df[st.session_state.df["Make"] == st.session_state.make_selector]["Model"].unique()
)

# Force rerun to refresh model list when make changes
if "prev_make" not in st.session_state or st.session_state.prev_make != st.session_state.make_selector:
    st.session_state.prev_make = st.session_state.make_selector
    st.rerun()

# -------- Form Section --------
with st.form("prediction_form"):
    st.markdown("<div class='predict-box'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # selected_make = st.selectbox("Select Make", st.session_state.makes)

        # Filter models for selected make
        selected_model = st.selectbox("Select Model", st.session_state.filtered_models)

        # filtered_models = sorted(st.session_state.df[st.session_state.df["Make"] == selected_make]["Model"].unique())
        # selected_model = st.selectbox("Select Model", filtered_models)

        year = st.number_input("Year", min_value=1990, max_value=2025, value=2020)
        mileage = st.number_input("Mileage (km)", min_value=0, max_value=500000, value=100000)

    with col2:
        cylinders = st.selectbox("Cylinders", [3, 4, 6, 8])
        fuel_type = st.selectbox("Fuel Type", ["Gasoline", "Diesel", "Hybrid", "Electric"])
        transmission = st.selectbox("Transmission", ["Automatic", "Manual"])

    # -------- Car Condition Section --------
    st.markdown("<h4 style='text-align:left; color:#191a1f; font-size:1.2rem;'>Car Condition</h4>", unsafe_allow_html=True)

    all_conditions = [
        'Engine repaired',
        'Accident history',
        'Minor scratches',
        'Dented door',
        'Repainted bumper',
        'No damage'
    ]

    selected_condition = st.selectbox("Choose the car condition:", all_conditions)

    

    # -------- Features Section --------
    st.markdown("<h4 style='text-align:left; color:#191a1f; font-size:1.2rem;'>Features</h4>", unsafe_allow_html=True)

    all_features = [
        "Rear Camera",
        "Navigation System",
        "Sunroof",
        "Bluetooth",
        "Cruise Control",
        "Leather Seats"
    ]

    selected_features = st.multiselect(
        "Select Feature(s)",
        options=all_features,
        default=["Rear Camera"]
    )

    # Convert selections into 0/1 feature vector
    binary_feature_vector = [1 if feature in selected_features else 0 for feature in all_features]



    # -------- Submit --------
    submitted = st.form_submit_button("Predict Price")

    if submitted:
        st.success("Your request is being handled")

        data = data = {
            "Make": selected_make,
            "Model": selected_model,
            "Year": int(year),
            "Mileage": float(mileage),
            "Cylinders": int(cylinders),
            "Condition": selected_condition,
            "Rear_camera": binary_feature_vector[0],
            "Navigation_system": binary_feature_vector[1],
            "Leather_seats": binary_feature_vector[2],
            "Sunroof": binary_feature_vector[3],
            "cruise_control": binary_feature_vector[4],
            "Bluetooth": binary_feature_vector[5]
        }

        URL_predict = st.secrets["my_secrets"]["URL_predict"]
        prediction = requests.post(URL_predict, json=data).json()["prediction"]
        # prediction = requests.post("http://127.0.0.1:8000/predict", json=data).json()["prediction"]

        st.markdown(f"## Your prediction is: {prediction}")

    st.markdown("</div>", unsafe_allow_html=True)


