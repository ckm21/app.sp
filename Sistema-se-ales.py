
import streamlit as st
import funciones

st.set_page_config(page_title="Sistema de Señales por Velas Japonesas", layout="wide")
st.title("📈 Sistema de Señales por Velas Japonesas")
st.markdown("Bienvenido a la aplicación de análisis de acciones basada en velas japonesas.")

ticker = st.sidebar.text_input("Ingresa el ticker de la acción", value="AAPL")
periodo = st.sidebar.selectbox("Selecciona el marco de tiempo", ["15m", "1h", "4h", "1d", "1wk"])

if st.sidebar.button("Analizar"):
    try:
        datos, senal, riesgo = funciones.obtener_datos_y_senal(ticker, periodo)
        st.write(f"Señal detectada: **{senal}**")
        st.write(f"Nivel de riesgo: **{riesgo}**")
        st.line_chart(datos['Close'])
    except ValueError as e:
        st.error(f"No se pudo analizar la acción: {str(e)}")
