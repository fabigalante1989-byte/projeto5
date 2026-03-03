import streamlit as st
import pandas as pd
import plotly.express as px

# Lendo os dados
dados = pd.read_csv('C:/Users/fabi_/projeto5/notebooks/dados_tratados.csv')

# Cabeçalho
st.header('Análise de dados de acidentes aéreos entre os anos de 2000 e 2024')

#criando gráfico de dispersão

fig1 = px.scatter(dados, x='ano_da_ocorrencia', y='lesoes_fatais', color='tipo_de_operacao', labels={'ano_da_ocorrencia': 'Ano da ocorrência', 'lesoes_fatais': 'Número de lesões fatais', 'tipo_de_operacao':'Tipo de operação'}, title='Quantidade de lesões fatais em acidentes aéreos por ano')
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.histogram(dados, x='ano_da_ocorrencia', color='regiao', labels={'ano_da_ocorrência' : 'Ano da ocorrência', 'count' : 'Quantidade de acidentes', 'regiao' : 'Região brasileira'})
st.plotly_chart(fig2, use_container_width=True)
