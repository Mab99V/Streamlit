import streamlit as st
import pandas as pd
import plotly.express as px


# Lectura del conjunto de datos
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
data = pd.read_csv(data_url)

# Función para mostrar la tabla
def show_table():
    st.write(data)

# Función para mostrar el histograma
def show_histogram():
    column_name = st.selectbox("Selecciona una columna", data.columns)
    fig = px.histogram(data, x=column_name)
    st.plotly_chart(fig)

# Función para mostrar la gráfica de barras
def show_bar_chart():
    x_axis = st.selectbox("Selecciona el eje X", data.columns)
    y_axis = st.selectbox("Selecciona el eje Y", data.columns)
    fig = px.bar(data, x=x_axis, y=y_axis)
    st.plotly_chart(fig)

# Función para mostrar la gráfica scatter
def show_scatter_chart():
    x_axis = st.selectbox("Selecciona el eje X", data.columns)
    y_axis = st.selectbox("Selecciona el eje Y", data.columns)
    fig = px.scatter(data, x=x_axis, y=y_axis)
    st.plotly_chart(fig)

# Función para filtrar los datos
def filter_data():
    filter_column = st.selectbox("Selecciona la columna para filtrar", data.columns)
    filter_value = st.text_input("Ingresa el valor para filtrar")
    filtered_data = data[data[filter_column] == filter_value]
    st.write(filtered_data)

# Barra de navegación
menu = ["Tabla", "Histograma", "Gráfica de barras", "Gráfica scatter", "Filtrar datos"]
choice = st.sidebar.selectbox("Selecciona una opción", menu)

# Mostrar la opción seleccionada
if choice == "Tabla":
    st.header("Tabla de datos")
    show_table()
elif choice == "Histograma":
    st.header("Histograma")
    show_histogram()
elif choice == "Gráfica de barras":
    st.header("Gráfica de barras")
    show_bar_chart()
elif choice == "Gráfica scatter":
    st.header("Gráfica scatter")
    show_scatter_chart()
elif choice == "Filtrar datos":
    st.header("Filtrar datos")
    filter_data()

