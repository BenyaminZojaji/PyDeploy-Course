import streamlit as st
import pandas as pd

with st.sidebar:
    st.info("You can upload a CSV file to quickly see dataframe in a table and scatter chart.")


uploaded_file = st.file_uploader("Upload a CSV file...", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    st.dataframe(data)

    # data['Date'] = pd.to_datetime(data['Date'])
    # data['Date'] = data['Date'].map(lambda date: date.year*10000 + date.month*100 + date.day)
    
    st.scatter_chart(data=data, x='Date', y=['MSFT', 'KLM', 'ING', 'MOS'], size=5)
