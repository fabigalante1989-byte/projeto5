import streamlit as st
import pandas as pd
import plotly.express as px

# Lendo os dados
dados = pd.read_csv('dados_tratados.csv')

# Cabeçalho
st.header('Análise de dados de acidentes aéreos entre os anos de 2000 e 2024')

# Botão para mostrar os dados
graph_button = st.button('Criar gráfico de dispersão')

if graph_button:
    st.write('Criando o gráfico de dispersão sobre lesões fatais em acidentes aéreos')
    #criando gráfico de dispersão
    dados_lesoes = dados[dados['lesoes_fatais'] > 0]
    fig1 = px.scatter(dados_lesoes, x='data_da_ocorrencia', 
                      y='lesoes_fatais', color='tipo_de_operacao', 
                      labels={'data_da_ocorrencia': 'Ano da ocorrência', 
                              'lesoes_fatais': 'Número de lesões fatais', 
                              'tipo_de_operacao':'Tipo de operação'}, 
                              title='Quantidade de lesões fatais em ' \
                              'acidentes aéreos por ano', 
                              range_x=[2000, 2024], 
                              range_y=[0, dados_lesoes['lesoes_fatais'].max() + 10])
    st.plotly_chart(fig1)

# Criando seletor múltiplo de regiões
regioes_unicas = sorted(dados['regiao'].astype(str).unique())
regioes_selecionadas = st.multiselect('Selecione as regiões:', 
                                      regioes_unicas, 
                                      default=regioes_unicas) 

# Filtrando os dados
if regioes_selecionadas:
    dados_filtrados = dados[dados['regiao'].isin(regioes_selecionadas)]
    
    # Criando histograma
    fig2 = px.histogram(dados_filtrados, x='ano_da_ocorrencia', color='regiao',
                       labels={'ano_da_ocorrencia': 'Ano da ocorrência', 
                              'count': 'Quantidade de acidentes'},
                       title=f'Acidentes aéreos por região: {", ".join(regioes_selecionadas)}')
    
    st.plotly_chart(fig2)
else:
    st.warning('Selecione pelo menos uma região!')
