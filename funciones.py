
import yfinance as yf
import pandas as pd

# Detectar señales básicas por velas
def detectar_senal(velas):
    if velas is None or len(velas) < 2:
        return "Sin datos suficientes"

    cuerpo_anterior = velas.iloc[-2]['Close'] - velas.iloc[-2]['Open']
    cuerpo_actual = velas.iloc[-1]['Close'] - velas.iloc[-1]['Open']

    if cuerpo_anterior < 0 and cuerpo_actual > 0:
        return "Posible señal de compra"
    elif cuerpo_anterior > 0 and cuerpo_actual < 0:
        return "Posible señal de venta"
    else:
        return "Sin señal clara"

# Calcular RSI para nivel de riesgo
def calcular_rsi(data, periodo=14):
    delta = data['Close'].diff()
    ganancia = delta.where(delta > 0, 0.0)
    perdida = -delta.where(delta < 0, 0.0)
    media_ganancia = ganancia.rolling(window=periodo).mean()
    media_perdida = perdida.rolling(window=periodo).mean()
    rs = media_ganancia / media_perdida
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Calcular riesgo con base en RSI
def evaluar_riesgo_por_rsi(rsi_actual):
    if rsi_actual < 30:
        return "Bajo riesgo"
    elif rsi_actual > 70:
        return "Alto riesgo"
    else:
        return "Riesgo moderado"

# Obtener datos y análisis
def obtener_datos_y_analisis(ticker, periodo="1mo", intervalo="1h"):
    datos = yf.download(ticker, period=periodo, interval=intervalo, progress=False)

    if datos.empty:
        return None, "No se pudieron obtener datos", None

    datos['RSI'] = calcular_rsi(datos)
    senal = detectar_senal(datos)
    rsi_actual = datos['RSI'].iloc[-1]
    riesgo = evaluar_riesgo_por_rsi(rsi_actual)

    return datos, senal, riesgo
