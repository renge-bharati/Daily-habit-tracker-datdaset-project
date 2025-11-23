import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Daily Habit Completion Prediction")

model = pickle.load(open("model.pkl", "rb"))

st.write("Enter Habit Details to Predict if it will be Completed")

# Example Input (Modify based on dataset)
day = st.number_input("Day", min_value=1, max_value=31)
month = st.number_input("Month", min_value=1, max_value=12)
year = st.number_input("Year", min_value=2000, max_value=2100)
dayofweek = st.number_input("Day of Week (0=Mon)", min_value=0, max_value=6)

# Make DataFrame for model
input_data = pd.DataFrame(
    {
        "Day": [day],
        "Month": [month],
        "Year": [year],
        "DayOfWeek": [dayofweek]
    }
)

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("👍 Habit Likely Completed!")
    else:
        st.error("👎 Habit Likely Not Completed")
