import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo os dados
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho do aplicativo
st.header('Análise de Dados de Vendas de Veículos')

# Criando um botão para o histograma
hist_button = st.button('Criar histograma de odômetro')

# Verifica se o botão foi clicado
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer", title="Histograma de Odômetro")
    st.plotly_chart(fig, use_container_width=True)

# Criando uma caixa de seleção para um segundo histograma
build_histogram = st.checkbox('Criar histograma de preço')

if build_histogram:
    st.write('Criando um histograma para a coluna preço')
    fig = px.histogram(car_data, x="price", title="Histograma de Preço")
    st.plotly_chart(fig, use_container_width=True)

# Criando um gráfico de dispersão (Scatter plot)
st.write("Gráfico de Dispersão: Preço vs Odômetro")
scatter_fig = px.scatter(car_data, x="odometer", y="price", title="Dispersão: Odômetro vs Preço")
st.plotly_chart(scatter_fig, use_container_width=True)
