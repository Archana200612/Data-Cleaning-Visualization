
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Data Cleaning & Visualization",
    page_icon="📊",
    layout="wide"
)

# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #f5f6fa;
}
.main-title {
    font-size: 32px;
    font-weight: 800;
    color: #4935a8;
}
.subtitle {
    color: #777;
    font-size: 15px;
}
div[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e5e5f0;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------
# LOAD DATASET
# --------------------------------

st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Select Dashboard",
    [
        "Overview",
        "Data Preview",
        "Data Cleaning",
        "Visualizations",
        "Download Data"
    ]
)

DATA_FILE = "data.csv"

if os.path.exists("cleaned_data.csv"):
    df = pd.read_csv("cleaned_data.csv")
elif os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    st.error("Dataset not found. Please run create_dataset.py first.")
    st.stop()

original_df = pd.read_csv(DATA_FILE) if os.path.exists(DATA_FILE) else df.copy()

# --------------------------------
# HEADER
# --------------------------------

st.markdown(
    '<p class="main-title">📊 Data Cleaning & Visualization Dashboard</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Explore, analyze, clean and visualize your retail dataset.</p>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------
# OVERVIEW
# --------------------------------

if page == "Overview":

    st.subheader("Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Records", f"{len(original_df):,}")
    col2.metric("Clean Records", f"{len(df):,}")
    col3.metric("Missing Values", f"{original_df.isnull().sum().sum():,}")
    col4.metric("Duplicates", f"{original_df.duplicated().sum():,}")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Sales by Product")

    if "Product" in df.columns and "Total_Sales" in df.columns:
        sales = df.groupby("Product", as_index=False)["Total_Sales"].sum()

        fig = px.bar(
            sales,
            x="Product",
            y="Total_Sales",
            color="Product",
            title="Total Sales by Product"
        )

        st.plotly_chart(fig, use_container_width=True)

# --------------------------------
# DATA PREVIEW
# --------------------------------

elif page == "Data Preview":

    st.subheader("Dataset Explorer")

    st.write("Dataset Shape:", df.shape)

    st.dataframe(df, use_container_width=True)

    st.subheader("Statistical Summary")
    st.dataframe(df.describe(include="all"), use_container_width=True)

# --------------------------------
# DATA CLEANING
# --------------------------------

elif page == "Data Cleaning":

    st.subheader("Data Quality Analysis")

    st.write("Missing Values by Column")

    missing = original_df.isnull().sum()

    missing_df = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })

    st.dataframe(missing_df, use_container_width=True)

    st.write("Duplicate Records")

    st.metric(
        "Duplicate Rows Found",
        original_df.duplicated().sum()
    )

    st.subheader("Cleaned Dataset")
    st.dataframe(df, use_container_width=True)

# --------------------------------
# VISUALIZATIONS
# --------------------------------

elif page == "Visualizations":

   
# --------------------------------
# ADVANCED VISUALIZATIONSs
# --------------------------------

    st.subheader("📊 Advanced Data Visualization")
    st.write("Explore your retail dataset through interactive charts.")

    numeric_df = df.select_dtypes(include=np.number)

    # Sidebar filters
    st.sidebar.subheader("Visualization Filters")

    filtered_df = df.copy()

    if "Region" in df.columns:
        regions = st.sidebar.multiselect(
            "Select Region",
            df["Region"].dropna().unique(),
            default=list(df["Region"].dropna().unique())
        )
        filtered_df = filtered_df[filtered_df["Region"].isin(regions)]

    if "Product" in df.columns:
        products = st.sidebar.multiselect(
            "Select Product",
            df["Product"].unique(),
            default=list(df["Product"].unique())
        )
        filtered_df = filtered_df[filtered_df["Product"].isin(products)]

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        st.stop()

    # 1. KPI Metrics
    c1, c2, c3 = st.columns(3)

    if "Total_Sales" in filtered_df.columns:
        c1.metric("Total Sales", f"₹{filtered_df['Total_Sales'].sum():,.0f}")
        c2.metric("Average Sales", f"₹{filtered_df['Total_Sales'].mean():,.0f}")

    if "Quantity" in filtered_df.columns:
        c3.metric("Total Quantity", f"{filtered_df['Quantity'].sum():,}")

    st.divider()

    # 2. Product Sales
    if "Product" in filtered_df.columns and "Total_Sales" in filtered_df.columns:

        st.subheader("1. Product-wise Sales Analysis")

        sales = filtered_df.groupby(
            "Product", as_index=False
        )["Total_Sales"].sum()

        fig = px.bar(
            sales,
            x="Product",
            y="Total_Sales",
            color="Product",
            text_auto=".2s",
            template="plotly_white",
            title="Total Sales by Product"
        )

        st.plotly_chart(fig, use_container_width=True)

    # 3. Category Distribution
    if "Category" in filtered_df.columns:

        st.subheader("2. Category Distribution")

        category_data = filtered_df["Category"].value_counts().reset_index()
        category_data.columns = ["Category", "Count"]

        fig = px.pie(
            category_data,
            names="Category",
            values="Count",
            hole=0.45,
            title="Product Category Distribution",
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

    # 4. Regional Analysis
    if "Region" in filtered_df.columns and "Total_Sales" in filtered_df.columns:

        st.subheader("3. Regional Sales Analysis")

        region_data = filtered_df.groupby(
            "Region", as_index=False
        )["Total_Sales"].sum()

        fig = px.bar(
            region_data,
            x="Region",
            y="Total_Sales",
            color="Total_Sales",
            color_continuous_scale="Purples",
            title="Sales by Region",
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

    # 5. Distribution Analysis
    if not numeric_df.empty:

        st.subheader("4. Numerical Distribution")

        selected_column = st.selectbox(
            "Choose a numerical variable",
            numeric_df.columns
        )

        fig = px.histogram(
            filtered_df,
            x=selected_column,
            marginal="box",
            nbins=30,
            title=f"Distribution of {selected_column}",
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

    # 6. Correlation Heatmap
    if numeric_df.shape[1] >= 2:

        st.subheader("5. Correlation Heatmap")

        correlation = filtered_df.select_dtypes(
            include=np.number
        ).corr()

        fig = px.imshow(
            correlation,
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1,
            title="Numerical Feature Correlation"
        )

        st.plotly_chart(fig, use_container_width=True)

    # 7. Scatter Plot
    if {"Quantity", "Total_Sales"}.issubset(filtered_df.columns):

        st.subheader("6. Quantity vs Sales Relationship")

        fig = px.scatter(
            filtered_df,
            x="Quantity",
            y="Total_Sales",
            color="Product" if "Product" in filtered_df.columns else None,
            hover_data=["Region"] if "Region" in filtered_df.columns else None,
            title="Quantity vs Total Sales",
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

    # 8. Outlier Detection
    if not numeric_df.empty:

        st.subheader("7. Outlier Detection")

        outlier_column = st.selectbox(
            "Select column for outlier analysis",
            numeric_df.columns,
            key="outlier_column"
        )

        fig = px.box(
            filtered_df,
            y=outlier_column,
            points="outliers",
            title=f"Outlier Analysis - {outlier_column}",
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.success("Interactive visualization analysis completed!")

# --------------------------------
# DOWNLOAD DATA
# --------------------------------

elif page == "Download Data":

    st.subheader("Download Cleaned Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Cleaned CSV",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )

    st.success("Your cleaned dataset is ready for download.")

# --------------------------------
# FOOTER
# --------------------------------

st.divider()

st.caption(
    "Data Cleaning & Visualization Project | Built using Python, Pandas, "
    "NumPy, Streamlit and Plotly"
)
