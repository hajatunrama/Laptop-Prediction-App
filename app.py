import streamlit as st
import pandas as pd
import joblib

# ==========================
# CONFIG
# ==========================

st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="wide"
)

# ==========================
# LOAD MODEL
# ==========================

@st.cache_resource
def load_model():
    return joblib.load("LaptopPricePrediction.pkl")

model = load_model()

# ==========================
# TITLE
# ==========================

st.title("💻 Laptop Price Prediction")
st.markdown(
    """
    Prediksi harga laptop berdasarkan spesifikasi hardware
    menggunakan model Machine Learning Linear Regression.
    """
)

# ==========================
# INPUTS
# ==========================

col1, col2 = st.columns(2)

with col1:

    country = st.selectbox(
        "Country",
        [
            "USA",
            "China",
            "India",
            "Germany",
            "Canada",
            "UK",
            "Japan",
            "Brazil",
            "Pakistan",
            "UAE"
        ]
    )

    laptop_brand = st.selectbox(
        "Laptop Brand",
        [
            "Acer",
            "Lenovo",
            "HP",
            "Asus",
            "Dell",
            "MSI",
            "Apple"
        ]
    )

    cpu_brand = st.selectbox(
        "CPU Brand",
        [
            "Intel",
            "AMD",
            "Apple"
        ]
    )

    gpu_brand = st.selectbox(
        "GPU Brand",
        [
            "Intel",
            "AMD",
            "NVIDIA"
        ]
    )

    usage_type = st.selectbox(
        "Usage Type",
        [
            "Basic",
            "Student",
            "Professional",
            "High-End Gaming"
        ]
    )

    ram = st.number_input(
        "RAM (GB)",
        min_value=4,
        max_value=64,
        value=16
    )

    storage = st.number_input(
        "Storage (GB)",
        min_value=128,
        max_value=4000,
        value=512
    )

with col2:

    cores = st.number_input(
        "CPU Cores",
        min_value=2,
        max_value=24,
        value=8
    )

    threads = st.number_input(
        "CPU Threads",
        min_value=2,
        max_value=48,
        value=16
    )

    base_clock = st.number_input(
        "Base Clock (GHz)",
        min_value=1.0,
        max_value=5.0,
        value=3.0
    )

    boost_clock = st.number_input(
        "Boost Clock (GHz)",
        min_value=1.0,
        max_value=6.0,
        value=4.5
    )

    tdp = st.number_input(
        "TDP (W)",
        min_value=5,
        max_value=250,
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

# ==========================
# AUTO CALCULATE
# ==========================

total_perf = cpu_perf + gpu_perf

st.info(f"Total Performance Score: {total_perf:,}")

# ==========================
# PREDICT
# ==========================

if st.button("🚀 Predict Laptop Price"):

    try:

        input_data = pd.DataFrame({
            "Country": [country],
            "Laptop_Brand": [laptop_brand],
            "Laptop_Model": ["Custom Model"],
            "CPU_Brand": [cpu_brand],
            "GPU_Brand": [gpu_brand],
            "GPU_Model": ["Custom GPU"],
            "RAM_GB": [ram],
            "Storage_GB": [storage],
            "Cores": [cores],
            "Threads": [threads],
            "Base_Clock": [base_clock],
            "Boost_Clock": [boost_clock],
            "TDP": [tdp],
            "CPU_Performance": [cpu_perf],
            "GPU_Performance": [gpu_perf],
            "Total_Performance": [total_perf],
            "Usage_Type": [usage_type]
        })

        prediction = model.predict(input_data)[0]

        st.success(
            f"💰 Estimated Laptop Price: ${prediction:,.2f}"
        )

    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )

# ==========================
# FOOTER
# ==========================

st.markdown("---")
st.caption(
    "Machine Learning Project | Laptop Price Prediction"
)
