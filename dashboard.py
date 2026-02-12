import streamlit as st
import pandas as pd

st.title("Student Performance Monitoring Dashboard")

data = pd.read_csv("data/student_data.csv")

st.write("Dataset Preview")
st.dataframe(data.head())

st.write("Feature Distribution")
st.bar_chart(data["study_hours"])
