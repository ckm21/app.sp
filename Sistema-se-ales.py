import streamlit as st
from funciones import (
    obtener_datos, analizar_senal_velas, generar_grafico, 
    obtener_rendimiento_portafolio, registrar_inversion, 
    eliminar_favorita, obtener_mensaje_objetivo
)

st.set_page_config(layout="centered")
st.markdown("# 📉 Sistema de Señales por Velas Japonesas")
st.write("Bienvenido a la aplicación de análisis de acciones basada en velas japonesas.")
st.success("Usuario: ejemplo | Modo: demo")

menu = st.sidebar.selectbox("Selecciona una opción:", [
    "Análisis técnico", 
    "Mi Portafolio", 
    "Semillero de Inversiones", 
    "Objetivos del Usuario"
])

if menu == "Análisis técnico":
    st.markdown("## 🔍 Análisis técnico")
    ticker = st.text_input("Introduce el símbolo de la acción (ej. AAPL):")
    if ticker:
        try:
            df = obtener_datos(ticker)
            if df is not None:
                señal = analizar_senal_velas(df)
                grafico = generar_grafico(df, ticker, señal)
                st.pyplot(grafico)
                st.success("Análisis cargado con éxito.")
        except Exception as e:
            st.error(f"No se pudo analizar la acción: {str(e)}")

elif menu == "Mi Portafolio":
    st.markdown("## 📊 Mi Portafolio")
    st.info("Aquí podrás ver tus acciones favoritas, ganancias y estado general.")
    resultado = obtener_rendimiento_portafolio()
    st.markdown(resultado)

elif menu == "Semillero de Inversiones":
    st.markdown("## 🌱 Semillero de Inversiones")
    st.info("Acciones con pequeñas inversiones activas a largo plazo.")
    st.text("Ejemplo: WOLF, GME... (simulación visual)")

elif menu == "Objetivos del Usuario":
    st.markdown("## 🎯 Objetivos del Usuario")
    porcentaje = st.slider("Define tu meta de ganancia (%)", 1, 20, 5)
    mensaje = obtener_mensaje_objetivo(porcentaje)
    st.markdown(mensaje)
    st.markdown(f"**Tu objetivo semanal:** {porcentaje}%")
