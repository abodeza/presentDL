# Preparation script (run once to create the pickle file)
import pandas as pd

df = pd.read_csv("uae_used_cars_10k.csv", usecols=["Make", "Model"])
unique_pairs = df.drop_duplicates().reset_index(drop=True)
unique_pairs.to_pickle("unique_make_model.pkl")


# # streamlit_app.py
# import streamlit as st
# import pandas as pd

# # Load data
# df = pd.read_pickle("unique_make_model.pkl")

# # Step 1: Get unique makes
# makes = sorted(df["Make"].unique())

# # Step 2: Select Make
# selected_make = st.selectbox("Select Make", makes)

# # Step 3: Filter models for selected make
# filtered_models = df[df["Make"] == selected_make]["Model"].unique()
# filtered_models = sorted(filtered_models)

# # Step 4: Select Model
# selected_model = st.selectbox("Select Model", filtered_models)

# # Step 5: Display selection
# st.write(f"You selected: {selected_make} - {selected_model}")
