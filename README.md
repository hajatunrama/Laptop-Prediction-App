# 💻 Laptop Price Prediction

Proyek Machine Learning untuk memprediksi harga laptop berdasarkan spesifikasi perangkat menggunakan algoritma regresi.

---

## 📌 Deskripsi Proyek

Laptop memiliki banyak variasi spesifikasi yang memengaruhi harga jualnya, seperti:

- Brand
- Processor
- GPU
- RAM
- Storage
- Jumlah Core dan Thread
- Clock Speed
- TDP

Pada proyek ini dilakukan:

1. Data Cleaning
2. Feature Engineering
3. Data Preprocessing
4. Model Training
5. Model Evaluation
6. Deployment menggunakan Streamlit

---

## 📂 Dataset

Dataset berisi informasi spesifikasi laptop dan harga laptop.

Jumlah data:

- 120.500+ baris
- 17 fitur

Fitur yang digunakan:

| Feature |
|----------|
| Country |
| Laptop_Brand |
| Laptop_Model |
| CPU_Brand |
| GPU_Brand |
| GPU_Model |
| RAM_GB |
| Storage_GB |
| Cores |
| Threads |
| Base_Clock |
| Boost_Clock |
| TDP |
| CPU_Performance |
| GPU_Performance |
| Total_Performance |
| Usage_Type |

Target:

- Price

---

## 🛠️ Library yang Digunakan

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
joblib
streamlit
```

---

## ⚙️ Tahapan Project

### 1. Data Understanding

Memahami struktur dataset dan tipe data yang digunakan.

### 2. Data Cleaning

- Menghapus missing value
- Menghapus data duplikat
- Memastikan format data konsisten

### 3. Feature Engineering

Membuat fitur baru:

```python
Total_Performance =
CPU_Performance + GPU_Performance
```

Fitur ini membantu model memahami performa keseluruhan laptop.

### 4. Data Preprocessing

Menggunakan:

```python
ColumnTransformer
```

Untuk:

- OneHotEncoding fitur kategorikal
- Passthrough fitur numerik

### 5. Model Training

Model yang diuji:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

### 6. Model Evaluation

Metrik evaluasi:

- MAE
- RMSE
- R² Score
- Training Time
- Prediction Time

---

## 📊 Hasil Evaluasi

| Model | MAE | RMSE | R² |
|---------|---------|---------|---------|
| Linear Regression | 62.48 | 72.16 | 0.9963 |
| XGBoost | 63.21 | 73.40 | 0.9962 |
| Random Forest | 64.94 | 76.31 | 0.9959 |
| Decision Tree | 85.10 | 104.33 | 0.9924 |

Model terbaik:

🏆 **Linear Regression**

Alasan:

- R² tertinggi
- MAE terendah
- RMSE terendah
- Training tercepat

---

## 💾 Save Model

Model disimpan menggunakan:

```python
joblib.dump(
    linear_pipeline,
    "LaptopPricePrediction.pkl"
)
```

---

## 🚀 Deployment

Aplikasi dibuat menggunakan Streamlit.

Menjalankan aplikasi secara lokal:

```bash
streamlit run app.py
```

---

## 📁 Struktur Project

```bash
Laptop-Price-Prediction/
│
├── notebook.ipynb
├── app.py
├── LaptopPricePrediction.pkl
├── requirements.txt
├── README.md
└── dataset.csv
```

---

## 🎯 Contoh Prediksi

Input:

- Brand: ASUS
- RAM: 16 GB
- Storage: 512 GB
- CPU Performance: 15000
- GPU Performance: 12000

Output:

```bash
Predicted Price:
$1249.50
```

---

## 👨‍💻 Author

Nama: [Nama Kamu]

Mata Kuliah:
Machine Learning

Universitas:
[Universitas Kamu]
