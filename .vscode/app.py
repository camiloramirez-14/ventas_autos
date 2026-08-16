import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us_cleaned.csv')  # leer los datos
st.header('Data viewer (Venta actual de vehiculos)')
# crear grafico de dispersion comparando precios y kilometraje
scatter_button = st.button('generar grafico')

if scatter_button:
    st.write('creacion de grafico de dispersion de precios vs kilometraje')
    fig = px.scatter(car_data, x='odometer', y='price', color='type',
                     title='Precio vs Kilometraje')  # comparacion de precios sobre kilometraje
    st.plotly_chart(fig)  # mostrar el grafico

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('creacion de histograma')
    fig = px.histogram(car_data, x='odometer', nbins=50,
                       title='Histograma de kilometraje')  # crear histograma )
    st.plotly_chart(fig, use_container_width=True)  # mostrar el histograma
