import streamlit as st
import pandas as pd
import plotly.express as px

# Carregando os dados
df = pd.read_csv("MS_Financial Sample.csv", sep=';')

# Limpar nomes de colunas
df.columns = df.columns.str.strip()

# Título e introdução
st.title("Análise Financeira - Dashboard Básico")
st.write("Este é um exemplo simples de aplicação Streamlit usando um dataset financeiro.")

# Exibição dos dados
st.subheader("Visualização da Tabela")
st.dataframe(df.head())

# Converter colunas numéricas
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

# Paleta de cores (opcional)
colors = px.colors.qualitative.Set3  # ou: Plotly, D3, Pastel, etc.

# Gráfico 1: Total de Vendas por Segmento
st.subheader("Total de Vendas por Segmento")

if 'Segment' in df.columns and 'Sales' in df.columns:
    sales_by_segment = df.groupby("Segment", as_index=False)["Sales"].sum()
    fig1 = px.bar(
        sales_by_segment,
        x='Segment',
        y='Sales',
        color='Segment',
        title="Vendas por Segmento",
        color_discrete_sequence=colors
    )
    st.plotly_chart(fig1)
else:
    st.error("As colunas 'Segment' ou 'Sales' não foram encontradas no arquivo CSV.")

# Gráfico 2: Total de Lucro por País (Top 10)
st.subheader("Total de Lucro por País (Top 10)")

if 'Country' in df.columns and 'Profit' in df.columns:
    profit_by_country = df.groupby("Country", as_index=False)["Profit"].sum()
    top_profit_countries = profit_by_country.sort_values(by="Profit", ascending=False).head(10)
    fig2 = px.bar(
        top_profit_countries,
        x='Country',
        y='Profit',
        color='Country',
        title="Lucro por País (Top 10)",
        color_discrete_sequence=colors
    )
    st.plotly_chart(fig2)
else:
    st.error("As colunas 'Country' ou 'Profit' não foram encontradas no arquivo CSV.")
