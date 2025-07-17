
import streamlit as st

st.set_page_config(page_title="Sistema de Señales", layout="wide")

st.title("📈 Sistema de Señales por Velas Japonesas")
st.write("Bienvenido a la aplicación de análisis de acciones basada en velas japonesas.")

st.sidebar.header("Opciones")
ticker = st.sidebar.text_input("Ingresa el ticker de la acción", "AAPL")

if st.sidebar.button("Analizar"):
    st.success(f"Análisis ejecutado para {ticker}")
