import streamlit as st
from funciones import *
import datetime

st.set_page_config(page_title="Sistema de Señales", layout="centered")
st.title("📈 Sistema de Señales por Velas Japonesas")

st.markdown("Bienvenido a la aplicación de análisis de acciones basada en velas japonesas.")

# Modo demo y usuario
st.markdown("#### Usuario: ejemplo | Modo: demo")

# ---- MI PORTAFOLIO ----
st.subheader("📊 Mi Portafolio")
st.info("Aquí podrás ver tus acciones favoritas, ganancias y estado general.")

portafolio = {
    "AAPL": {"entrada": 180, "actual": 188},
    "WOLF": {"entrada": 1.54, "actual": 1.51}
}

ganancia_total = 0
for ticker, datos in portafolio.items():
    ganancia = calcular_porcentaje_ganancia(datos["entrada"], datos["actual"])
    ganancia_total += ganancia
    color = "🟢" if ganancia >= 0 else "🔴"
    st.markdown(f"{color} **{ticker}**: {ganancia}%")

st.markdown(f"📌 **Ganancia diaria**: {round(ganancia_total / len(portafolio), 2)}% (${round(ganancia_total * 2, 2)})")

# ---- SEMILLERO ----
st.subheader("🌱 Semillero de Inversiones")
st.info("Acciones con pequeñas inversiones activas a largo plazo.")

# ---- OBJETIVOS ----
st.subheader("🎯 Objetivos del Usuario")
objetivo = st.slider("Define tu meta de ganancia (%)", 1, 20, 5)
mensaje, color = clasificar_objetivo(objetivo)
st.markdown(f":red_circle: **{mensaje}**")
st.markdown(f"**Tu objetivo semanal**: {objetivo}%")

# ---- RESULTADO FINAL ----
ganancia_diaria = 2.1  # ejemplo
st.subheader("📅 Resultado del Día")
st.metric("Tu rendimiento", f"{ganancia_diaria}%")

st.markdown(mensaje_según_resultado(ganancia_diaria, objetivo))

# ---- ANÁLISIS ----
st.subheader("🔍 Análisis técnico")
ticker = st.text_input("Introduce el símbolo de la acción (ej. AAPL):", value="Mp")

if ticker:
    datos = obtener_datos(ticker)
    if not datos.empty:
        st.line_chart(datos['Close'])
        st.success("Análisis cargado con éxito.")
