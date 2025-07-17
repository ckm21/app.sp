# Sistema-se-ales.py

import streamlit as st
import matplotlib.pyplot as plt
from funciones import (
    calcular_porcentaje_ganancia,
    clasificar_objetivo,
    mensaje_según_resultado,
    obtener_datos
)

st.set_page_config(page_title="Sistema de Señales", layout="centered")

st.title("📈 Sistema de Señales por Velas Japonesas")
st.write("Bienvenido a la aplicación de análisis de acciones basada en velas japonesas.")
st.success("Usuario: ejemplo | Modo: demo")

# 📊 MI PORTAFOLIO
st.subheader("📊 Mi Portafolio")
st.info("Aquí podrás ver tus acciones favoritas, ganancias y estado general.")

datos = obtener_datos()
ganancia_total = 0
cantidad = len(datos)

for ticker, info in datos.items():
    ganancia = calcular_porcentaje_ganancia(info["entrada"], info["actual"])
    color = "🟢" if ganancia >= 0 else "🔴"
    st.write(f"{color} {ticker}: {ganancia}%")
    ganancia_total += ganancia

promedio = round(ganancia_total / cantidad, 2)
st.markdown(f"📌 **Ganancia diaria:** {promedio}% (${round((promedio/100)*200,2)})")  # Simulando sobre $200

# 🌱 SEMILLERO
st.subheader("🌱 Semillero de Inversiones")
st.info("Acciones con pequeñas inversiones activas a largo plazo.")

# 🎯 OBJETIVOS
st.subheader("🎯 Objetivos del Usuario")
objetivo = st.slider("Define tu meta de ganancia (%)", 1, 20, 5)
mensaje, color = clasificar_objetivo(objetivo)
st.error(mensaje) if color == "rojo" else st.warning(mensaje) if color == "naranja" else st.success(mensaje)
st.markdown(f"**Tu objetivo semanal:** {objetivo}%")
st.caption(mensaje_según_resultado(objetivo))

# 🔍 ANÁLISIS TÉCNICO (simulado)
st.subheader("🔍 Análisis técnico")
ticker_input = st.text_input("Introduce el símbolo de la acción (ej. AAPL):", "Mp")

if ticker_input:
    fechas = ["Thu 10", "Fri 11", "Sat 12", "Jul 13", "Mon 14", "Tue 15", "Wed 16", "Thu 17"]
    precios = [30, 44, 47, 45, 46, 48, 60, 61]

    fig, ax = plt.subplots()
    ax.plot(fechas, precios, color="skyblue", linewidth=2)
    ax.set_title(f"Gráfico de {ticker_input.upper()}")
    ax.set_ylabel("Precio ($)")
    ax.set_xlabel("Fecha")
    ax.grid(True)
    st.pyplot(fig)
    st.success("Análisis cargado con éxito.")
