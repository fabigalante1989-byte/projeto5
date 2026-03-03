import streamlit as st
import pandas as pd
import plotly.express as px

# Lendo os dados
dados = pd.read_csv('C:/Users/fabi_/projeto5/notebooks/dados_tratados.csv')

# Cabeçalho
st.header('Análise de dados de acidentes aéreos entre os anos de 2000 e 2024')

'''
# Botão para gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # Criando o gráfico
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Ordenando o eixo y
    fig.update_yaxes(categoryorder="total ascending")
    
    # Exibindo no Streamlit
    st.plotly_chart(fig, use_container_width=True)
'''

#criando gráfico de dispersão

fig = px.scatter(dados, x='ano_da_ocorrencia', y='lesoes_fatais', color='tipo_de_operacao', labels={'ano_da_ocorrencia': 'Ano da ocorrência', 'lesoes_fatais': 'Número de lesões fatais', 'tipo_de_operacao':'Tipo de operação'}, title='Quantidade de lesões fatais em acidentes aéreos por ano')
fig.show()