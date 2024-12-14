import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
raw_data = pd.read_csv("elderly_online_safety.csv")  # Update with actual path
processed_data = pd.read_csv("preprocessed_data.csv")  # Update with actual path

# Dataset selection
dataset_choice = st.selectbox("Select Dataset to Explore", ["Raw Data", "Processed Data"])
data = raw_data if dataset_choice == "Raw Data" else processed_data

# Dataset preview
st.write("### Dataset Preview")
st.dataframe(data.head())

# Histogram
if st.checkbox("Show Histogram"):
    st.write("### Histogram")
    numerical_feature = st.selectbox("Select a Numerical Feature", data.select_dtypes(include=["float64", "int64"]).columns)
    fig, ax = plt.subplots()
    sns.histplot(data[numerical_feature], kde=True, ax=ax, color="skyblue")
    st.pyplot(fig)

# Bar Chart
if st.checkbox("Show Bar Chart"):
    st.write("### Bar Chart")
    categorical_feature = st.selectbox("Select a Categorical Feature", data.select_dtypes(include=["object"]).columns)
    fig, ax = plt.subplots()
    data[categorical_feature].value_counts().plot(kind="bar", ax=ax, color="orange")
    st.pyplot(fig)

# Box Plot
if st.checkbox("Show Box Plot"):
    st.write("### Box Plot")
    numerical_feature = st.selectbox("Select a Numerical Feature for Box Plot", data.select_dtypes(include=["float64", "int64"]).columns)
    category = st.selectbox("Select a Categorical Feature to Group By", data.select_dtypes(include=["object"]).columns)
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x=category, y=numerical_feature, ax=ax)
    st.pyplot(fig)

# Correlation Heatmap
if st.checkbox("Show Correlation Heatmap"):
    st.write("### Correlation Heatmap")
    numerical_features = data.select_dtypes(include=["float64", "int64"]).columns
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(data[numerical_features].corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Scatter Plot
if st.checkbox("Show Scatter Plot"):
    st.write("### Scatter Plot")
    x_axis = st.selectbox("Select X-axis Feature", data.select_dtypes(include=["float64", "int64"]).columns)
    y_axis = st.selectbox("Select Y-axis Feature", data.select_dtypes(include=["float64", "int64"]).columns)
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x=x_axis, y=y_axis, hue="Gender", ax=ax)  # Update 'hue' as needed
    st.pyplot(fig)

# Pie Chart
if st.checkbox("Show Pie Chart"):
    st.write("### Pie Chart")
    categorical_feature = st.selectbox("Select a Feature for Pie Chart", data.select_dtypes(include=["object"]).columns)
    pie_data = data[categorical_feature].value_counts()
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", colors=sns.color_palette("pastel"))
    st.pyplot(fig)
