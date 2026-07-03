import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("LaptopPricePrediction.pkl")

st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Laptop Price Prediction")
st.write("Prediksi harga laptop menggunakan Machine Learning (Linear Regression).")

# ========================
# INPUT USER
# ========================

country = st.text_input("Country", "USA")

laptop_brand = st.text_input("Laptop Brand", "Dell")
laptop_model = st.text_input("Laptop Model", "Inspiron 15")

cpu_brand = st.text_input("CPU Brand", "Intel")
gpu_brand = st.text_input("GPU Brand", "NVIDIA")
gpu_model = st.text_input("GPU Model", "RTX 4060")

ram = st.number_input(
    "RAM (GB)",
    min_value=4,
    max_value=128,
    value=16
)

storage = st.number_input(
    "Storage (GB)",
    min_value=128,
    max_value=4000,
    value=512
)

cores = st.number_input(
    "CPU Cores",
    min_value=2,
    max_value=32,
    value=8
)

threads = st.number_input(
    "CPU Threads",
    min_value=2,
    max_value=64,
    value=16
)

base_clock = st.number_input(
    "Base Clock (GHz)",
    min_value=1.0,
    max_value=6.0,
    value=3.0
)

boost_clock = st.number_input(
    "Boost Clock (GHz)",
    min_value=1.0,
    max_value=7.0,
    value=4.5
)

tdp = st.number_input(
    "TDP",
    min_value=5,
    max_value=300,
    value=65
)

cpu_perf = st.number_input(
    "CPU Performance",
    min_value=1000,
    max_value=100000,
    value=25000
)

gpu_perf = st.number_input(
    "GPU Performance",
    min_value=0,
    max_value=100000,
    value=20000
)

total_perf = st.number_input(
    "Total Performance",
    min_value=1000,
    max_value=200000,
    value=45000
)

usage_type = st.selectbox(
    "Usage Type",
    [
        "Office",
        "Gaming",
        "Student",
        "Programming",
        "Content Creation"
    ]
)

# ========================
# PREDIKSI
# ========================

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "Country":[country],
        "Laptop_Brand":[laptop_brand],
        "Laptop_Model":[laptop_model],
        "CPU_Brand":[cpu_brand],
        "GPU_Brand":[gpu_brand],
        "GPU_Model":[gpu_model],
        "RAM_GB":[ram],
        "Storage_GB":[storage],
        "Cores":[cores],
        "Threads":[threads],
        "Base_Clock":[base_clock],
        "Boost_Clock":[boost_clock],
        "TDP":[tdp],
        "CPU_Performance":[cpu_perf],
        "GPU_Performance":[gpu_perf],
        "Total_Performance":[total_perf],
        "Usage_Type":[usage_type]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Laptop Price: ${prediction:,.2f}"
    )
