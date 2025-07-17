
import streamlit as st
import funciones

st.set_page_config(page_title="Sistema de Señales por Velas Japonesas", layout="centered")

st.sidebar.title("Opciones")
ticker = st.sidebar.text_input("Ingresa el ticker de la acción", value="AAPL")
periodo = st.sidebar.selectbox("Periodo", ["1d", "5d", "1mo", "3mo", "6mo", "1y"], index=2)
intervalo = st.sidebar.selectbox("Intervalo", ["15m", "1h", "4h", "1d", "1wk"], index=2)

if st.sidebar.button("Analizar"):
    datos, senal, riesgo = funciones.obtener_datos_y_analisis(ticker, periodo, intervalo)

    if datos is None:
        st.error(senal)
    else:
        st.title("📈 Sistema de Señales por Velas Japonesas")
        st.markdown(f"**Acción:** {ticker}")
        st.markdown(f"**Señal detectada:** `{senal}`")
        st.markdown(f"**Nivel de riesgo actual:** `{riesgo}`")

        st.subheader("Últimos datos de velas")
        st.dataframe(datos.tail(10))

        st.line_chart(datos['Close'])
