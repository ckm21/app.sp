import streamlit as st
import json
from funciones import (
    calcular_ganancia_total,
    mostrar_portafolio,
    mostrar_semillero,
    mostrar_objetivos
)

# Cargar datos de ejemplo
usuario = "ejemplo"
modo = "demo"
acciones = {
    "AAPL": {"ganancia": 4.5, "monto": 50},
    "WOLF": {"ganancia": -2.1, "monto": 40},
}
semillero = {
    "MSFT": {"ganancia": 1.2, "monto": 15}
}
objetivo = 16

# Título
st.markdown("# 📈 Sistema de Señales por Velas Japonesas")
st.markdown("Bienvenido a la aplicación de análisis de acciones basada en velas japonesas.")
st.success(f"Usuario: {usuario} | Modo: {modo}")

# Mostrar Portafolio
st.subheader("📊 Mi Portafolio")
mostrar_portafolio(acciones)

# Mostrar Semillero
st.subheader("🌱 Semillero de Inversiones")
mostrar_semillero(semillero)

# Mostrar Objetivos
st.subheader("🎯 Objetivos del Usuario")
mostrar_objetivos(objetivo)

# Ganancia total
ganancia, monto = calcular_ganancia_total(acciones)
st.markdown(f"📌 **Ganancia diaria**: {ganancia:.1f}% (${monto:.2f})")