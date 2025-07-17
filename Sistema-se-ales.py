import streamlit as st
import json
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from funciones import saludar

# Cargar configuración
with open("config.json", "r") as f:
    config = json.load(f)

usuario = config.get("usuario", "ejemplo")
modo = config.get("modo", "demo")

# Interfaz principal
st.set_page_config(page_title="📈 Sistema de Señales por Velas Japonesas", layout="centered")

st.title("📈 Sistema de Señales por Velas Japonesas")
st.write("Bienvenido a la aplicación de análisis de acciones basada en velas japonesas.")

# Mensaje de prueba para verificar conexión
st.success(f"Usuario: **{usuario}** | Modo: **{modo}**")

# Barra lateral con navegación
menu = st.sidebar.selectbox("Selecciona una sección:", ["Inicio", "Mi portafolio", "Semillero", "Objetivos"])

if menu == "Inicio":
    st.subheader("🔍 Análisis técnico")
    ticker = st.text_input("Introduce el símbolo de la acción (ej. AAPL):")

    if ticker:
        try:
            df = yf.download(ticker, period="7d", interval="1h")
            if df.empty:
                st.error("No se encontraron datos para ese símbolo.")
            else:
                st.line_chart(df["Close"])
                st.success("Análisis cargado con éxito.")
        except Exception as e:
            st.error(f"No se pudo analizar la acción: {str(e)}")

elif menu == "Mi portafolio":
    st.subheader("📊 Mi Portafolio")
    st.info("Aquí podrás ver tus acciones favoritas, ganancias y estado general.")
    # Simulación de datos:
    st.write("🟢 AAPL: +4.5%  \n🔴 WOLF: -2.1%")
    st.write("📌 **Ganancia diaria:** +2.1% ($4.20)")

elif menu == "Semillero":
    st.subheader("🌱 Semillero de Inversiones")
    st.info("Acciones con pequeñas inversiones activas a largo plazo.")

elif menu == "Objetivos":
    st.subheader("🎯 Objetivos del Usuario")
    perfil = "alto riesgo"  # Simulado
    objetivo = st.slider("Define tu meta de ganancia (%)", min_value=1, max_value=20, value=5)

    if perfil == "bajo riesgo" and objetivo > 10:
        st.warning("⚠️ ¿Te crees el lobo de Wall Street?")
    elif objetivo <= 5:
        st.success("✅ Buen objetivo.")
    elif objetivo <= 10:
        st.info("🟡 Objetivo moderado.")
    else:
        st.error("🚨 ¿Te crees el lobo de Wall Street?")

    st.write(f"Tu objetivo semanal: **{objetivo}%**")
