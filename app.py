import streamlit as st
import pandas as pd
import joblib

model = joblib.load("LaptopPricePrediction.pkl")

st.title("💻 Laptop Price Prediction")

brand = st.selectbox(
    "Brand",
    ["Dell", "HP", "Lenovo", "Asus", "Acer", "Apple"]
)

ram = st.number_input(
    "RAM (GB)",
    min_value=2,
    max_value=128,
    value=8
)

storage = st.number_input(
    "Storage (GB)",
    min_value=64,
    max_value=4000,
    value=512
)

screen_size = st.number_input(
    "Screen Size (inch)",
    min_value=10.0,
    max_value=20.0,
    value=15.6
)

processor_speed = st.number_input(
    "Processor Speed (GHz)",
    min_value=1.0,
    max_value=6.0,
    value=3.0
)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "Brand": [brand],
        "RAM": [ram],
        "Storage": [storage],
        "Screen Size": [screen_size],
        "Processor Speed": [processor_speed]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Laptop Price: ${prediction:,.2f}"
    )
