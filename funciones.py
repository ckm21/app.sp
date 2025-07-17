import yfinance as yf
import pandas as pd

def obtener_datos(ticker, intervalo):
    df = yf.download(ticker, period="7d", interval=intervalo)
    df = df.dropna()
    return df

def detectar_senal(df):
    if len(df) < 2:
        return "No hay suficientes datos"

    cuerpo_anterior = df["Close"].iloc[-2] - df["Open"].iloc[-2]
    cuerpo_actual = df["Close"].iloc[-1] - df["Open"].iloc[-1]
    mecha_superior = df["High"].iloc[-1] - max(df["Close"].iloc[-1], df["Open"].iloc[-1])
    mecha_inferior = min(df["Close"].iloc[-1], df["Open"].iloc[-1]) - df["Low"].iloc[-1]

    if cuerpo_anterior < 0 and cuerpo_actual > 0 and mecha_inferior > mecha_superior:
        return "Opción de compra"
    elif cuerpo_anterior > 0 and cuerpo_actual < 0 and mecha_superior > mecha_inferior:
        return "Riesgo de caída"
    else:
        return "Sin señal clara"

def calcular_riesgo(df):
    rsi_periodo = 14
    delta = df['Close'].diff()
    ganancia = delta.where(delta > 0, 0)
    perdida = -delta.where(delta < 0, 0)

    media_ganancia = ganancia.rolling(window=rsi_periodo).mean()
    media_perdida = perdida.rolling(window=rsi_periodo).mean()

    rs = media_ganancia / media_perdida
    rsi = 100 - (100 / (1 + rs))

    ultimo_rsi = rsi.iloc[-1]

    if ultimo_rsi > 70:
        return "Alto"
    elif ultimo_rsi < 30:
        return "Bajo"
    else:
        return "Moderado"

def obtener_senal_y_riesgo(ticker, intervalo):
    datos = obtener_datos(ticker, intervalo)
    senal = detectar_senal(datos)
    riesgo = calcular_riesgo(datos)
    return datos, senal, riesgo
