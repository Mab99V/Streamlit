import pandas as pd
import streamlit as st
name_link = 'dataset.csv'
st.title('Streamlit con cache')
@st.cache
def load_data(nrows):
    data = pd.read_csv(name_link, nrows=nrows)
    return data
data_load_state = st.text('cargando')
data = load_data(1000)
data_load_state.text('hecho!! (using.cache)')
st.dataframe(data)
