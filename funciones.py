import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def obtener_datos(ticker):
    df = yf.download(ticker, period="7d", interval="1d")
    return df if not df.empty else None

def analizar_senal_velas(df):
    if df is None or df.empty:
        raise ValueError("No hay datos disponibles.")
    df['cuerpo'] = abs(df['Open'] - df['Close'])
    df['mecha'] = df['High'] - df['Low']
    ultima = df.iloc[-1]
    if ultima['Close'] > ultima['Open']:
        return "compra"
    elif ultima['Close'] < ultima['Open']:
        return "venta"
    else:
        return "indecisión"

def generar_grafico(df, ticker, señal):
    fig, ax = plt.subplots()
    ax.plot(df['Close'], label='Precio cierre')
    ax.set_title(f"{ticker.upper()} - Señal: {señal}")
    ax.legend()
    return fig

def obtener_rendimiento_portafolio():
    # Simulación de acciones en portafolio
    portafolio = {
        "AAPL": +4.5,
        "WOLF": -2.1,
    }
    total = sum(portafolio.values()) / len(portafolio)
    total_dolares = round(total * 200 / 100, 2)
    salida = []
    for k, v in portafolio.items():
        emoji = "🟢" if v > 0 else "🔴"
        salida.append(f"{emoji} {k}: {v}%")
    salida.append(f"\n📌 **Ganancia diaria:** {total:.1f}% (${total_dolares})")
    return "\n".join(salida)

def registrar_inversion(ticker, monto, precio_entrada):
    return f"Registrada inversión de ${monto} en {ticker} a ${precio_entrada}"

def eliminar_favorita(ticker):
    return f"Eliminada {ticker} de favoritos."

def obtener_mensaje_objetivo(pct):
    if pct < 5:
        return "🟢 Buen objetivo: **alcanzable**"
    elif pct < 10:
        return "🟠 Objetivo moderado"
    elif pct < 15:
        return "🔴 ¿Te crees el lobo de Wall Street?"
    else:
        return "🚨 Reza a Dios… y si no tienes, te deseo mucha suerte 😅"
