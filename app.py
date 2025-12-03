import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el conjunto de datos
car_data = pd.read_csv("vehicles_us.csv")

st.header("Análisis Interactivo de Vehículos")

# Checkbox para histograma
build_histogram = st.checkbox("Mostrar histograma del odómetro")

if build_histogram:
    st.write("Histograma para la columna 'odometer'")
    fig = px.histogram(car_data, x="odometer", title="Distribución del odómetro")
    st.plotly_chart(fig)

# Checkbox para gráfico de dispersión
build_scatter = st.checkbox("Mostrar gráfico de dispersión (precio vs odómetro)")

if build_scatter:
    st.write("Gráfico de dispersión entre precio y odómetro")
    fig2 = px.scatter(car_data, x="odometer", y="price",
                      title="Precio vs Odómetro")
    st.plotly_chart(fig2)



