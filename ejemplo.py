import streamlit as st
import pandas as pd
import plotly.express as px

# Lectura del conjunto de datos
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Función para mostrar la tabla de datos
def show_table():
    st.write(data)

# Función para filtrar los datos
def filter_data():
    # Opciones de filtrado
    species = data.species.unique()
    selected_species = st.multiselect("Especie", species)
    min_sepal_length = st.slider("Longitud del sépalo mínima", float(data.sepal_length.min()), float(data.sepal_length.max()))
    max_sepal_length = st.slider("Longitud del sépalo máxima", min_sepal_length, float(data.sepal_length.max()))
    min_sepal_width = st.slider("Anchura del sépalo mínima", float(data.sepal_width.min()), float(data.sepal_width.max()))
    max_sepal_width = st.slider("Anchura del sépalo máxima", min_sepal_width, float(data.sepal_width.max()))
    
    # Filtrar los datos
    filtered_data = data[(data.species.isin(selected_species)) & 
                         (data.sepal_length >= min_sepal_length) & 
                         (data.sepal_length <= max_sepal_length) &
                         (data.sepal_width >= min_sepal_width) &
                         (data.sepal_width <= max_sepal_width)]
    
    return filtered_data

# Función para mostrar un histograma de una columna
def show_histogram(data, column):
    fig = px.histogram(data, x=column)
    st.plotly_chart(fig)

# Función para mostrar una gráfica de barras relacionando dos columnas
def show_bar_chart(data, x, y):
    fig = px.bar(data, x=x, y=y)
    st.plotly_chart(fig)

# Función para mostrar una gráfica scatter
def show_scatter(data, x, y, color):
    fig = px.scatter(data, x=x, y=y, color=color)
    st.plotly_chart(fig)

# Encabezado de la aplicación web
st.title("Análisis de datos de flores iris")

# Menú de navegación
menu = ["Ver datos", "Filtrar datos", "Histograma", "Gráfica de barras", "Gráfica scatter"]
choice = st.sidebar.selectbox("Seleccione una opción", menu)

# Mostrar la opción seleccionada
if choice == "Ver datos":
    show_table()
elif choice == "Filtrar datos":
    filtered_data = filter_data()
    st.write(filtered_data)
elif choice == "Histograma":
    column = st.selectbox("Seleccione una columna", data.columns)
    show_histogram(data, column)
elif choice == "Gráfica de barras":
    x = st.selectbox("Seleccione una columna para el eje X", data.columns)
    y = st.selectbox("Seleccione una columna para el eje Y", data.columns)
    show_bar_chart(data, x, y)

