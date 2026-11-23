
# 📊 Data Cleaning & Visualization Dashboard

## 📌 Project Overview
An interactive data analytics project developed using Python to clean, process, analyze, and visualize retail sales data.

## 🎯 Objectives
- Identify and handle missing values.
- Remove duplicate records.
- Perform exploratory data analysis.
- Generate meaningful data visualizations.
- Build an interactive analytics dashboard.

## 🚀 Features
- Dataset overview and preview
- Missing value analysis
- Duplicate record detection
- Data cleaning and preprocessing
- Interactive sales visualizations
- Correlation heatmap
- Outlier detection
- Cleaned CSV download

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit

## 📂 Project Structure
```text
Data_Cleaning_Visualization/
│
├── app.py
├── clean_data.py
├── create_dataset.py
├── data.csv
├── cleaned_data.csv
├── requirements.txt
├── README.md
│
└── visualizations/
    ├── histograms.png
    ├── correlation_heatmap.png
    └── boxplot.png
```

## ⚙️ Installation

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## ▶️ Run the Project

Generate the dataset:

```bash
python create_dataset.py
```

Clean the dataset:

```bash
python clean_data.py
```

Launch the dashboard:

```bash
python -m streamlit run app.py
```

## 📊 Dashboard Modules
1. Overview
2. Data Preview
3. Data Cleaning
4. Visualizations
5. Download Data

## 📌 Dataset
A synthetic retail dataset containing 1,005 records, including product, category, quantity, price, customer age, region, and total sales.

## 👩‍💻 Author
Archana DV

AIML Student
