import streamlit as st

def mostrar_portafolio(acciones):
    st.info("Aquí podrás ver tus acciones favoritas, ganancias y estado general.")
    for ticker, datos in acciones.items():
        color = "🟢" if datos["ganancia"] > 0 else "🔴"
        st.write(f"{color} {ticker}: {datos['ganancia']}%")

def mostrar_semillero(semillero):
    st.info("Acciones con pequeñas inversiones activas a largo plazo.")
    for ticker, datos in semillero.items():
        st.write(f"🌱 {ticker}: {datos['ganancia']}%")

def mostrar_objetivos(objetivo):
    st.write("Define tu meta de ganancia (%)")
    st.slider("Meta", 1, 20, objetivo, key="slider_obj")
    if objetivo >= 15:
        st.error("🚨 ¿Te crees el lobo de Wall Street?")
    elif objetivo >= 10:
        st.warning("⚠️ Objetivo moderado")
    else:
        st.success("✅ Buen objetivo")
    st.markdown(f"**Tu objetivo semanal:** {objetivo}%")

def calcular_ganancia_total(acciones):
    if not acciones:
        return 0, 0
    total = sum(datos["monto"] for datos in acciones.values())
    ganancia = sum((datos["ganancia"] / 100) * datos["monto"] for datos in acciones.values())
    return (ganancia / total) * 100, ganancia