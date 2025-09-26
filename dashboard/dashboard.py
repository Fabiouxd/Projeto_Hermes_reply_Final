import streamlit as st
import pandas as pd
import sqlite3
import os

# Define o caminho para o banco de dados
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
db_path = os.path.join(project_root, 'db', 'sensores.db')

# Título do Dashboard
st.title('Dashboard de Monitoramento Industrial')
st.markdown('---')

# Conecta ao banco de dados e carrega os dados
try:
    conn = sqlite3.connect(db_path)

    # Carrega dados dos sensores e leituras
    leituras_df = pd.read_sql_query("SELECT * FROM LeiturasSensor ORDER BY amostra ASC", conn)
    sensores_df = pd.read_sql_query("SELECT * FROM Sensores", conn)

    if leituras_df.empty:
        st.warning("O banco de dados de leituras está vazio. Por favor, rode 'implementar_banco.py' primeiro.")
    else:
        # Mostra estatísticas básicas
        st.subheader('Estatísticas das Leituras')
        st.dataframe(leituras_df.describe())

        st.markdown('---')

        # Gráfico de linhas para Temperatura e Umidade
        st.subheader('Gráfico: Temperatura e Umidade')
        st.line_chart(leituras_df[['temperatura', 'umidade']])

        # Gráfico de linhas para Aceleração
        st.subheader('Gráfico: Aceleração nos Eixos X, Y e Z')
        st.line_chart(leituras_df[['aceleracao_x', 'aceleracao_y', 'aceleracao_z']])

        st.markdown('---')

        # Alerta Simples (Temperatura)
        st.subheader('Alertas de Temperatura')
        temp_threshold = 25.0  # Limiar de temperatura
        leituras_anormais = leituras_df[leituras_df['temperatura'] > temp_threshold]

        if not leituras_anormais.empty:
            st.warning(f"**ALERTA!** {len(leituras_anormais)} leituras de temperatura acima do limiar de **{temp_threshold}°C**.")
            st.dataframe(leituras_anormais[['amostra', 'temperatura', 'umidade']])
        else:
            st.success("Não há alertas de temperatura. Sistema estável.")

except sqlite3.Error as e:
    st.error(f"Erro ao conectar ou ler o banco de dados: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()