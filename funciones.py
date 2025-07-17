import yfinance as yf
import pandas as pd
import datetime

def obtener_datos(ticker, periodo='1mo', intervalo='1d'):
    data = yf.download(ticker, period=periodo, interval=intervalo)
    data = data.dropna()
    return data

def detectar_velas_japonesas(data):
    señales = []
    for i in range(2, len(data)):
        anterior = data.iloc[i-1]
        actual = data.iloc[i]
        apertura = actual['Open']
        cierre = actual['Close']
        apertura_ant = anterior['Open']
        cierre_ant = anterior['Close']
        
        cuerpo = abs(cierre - apertura)
        mecha_superior = actual['High'] - max(apertura, cierre)
        mecha_inferior = min(apertura, cierre) - actual['Low']
        
        if cuerpo < 0.1 * (actual['High'] - actual['Low']):
            señales.append(('Doji', actual.name))
        elif cierre > apertura and cierre_ant < apertura_ant:
            señales.append(('Martillo Invertido', actual.name))
        elif cierre < apertura and cierre_ant > apertura_ant:
            señales.append(('Estrella Fugaz', actual.name))
        elif cierre > apertura:
            señales.append(('Alcista', actual.name))
        elif cierre < apertura:
            señales.append(('Bajista', actual.name))
    return señales

def calcular_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calcular_porcentaje_ganancia(precio_entrada, precio_actual):
    if precio_entrada == 0:
        return 0
    return round(((precio_actual - precio_entrada) / precio_entrada) * 100, 2)

def clasificar_objetivo(valor):
    if valor < 4:
        return ("✅ Alcanzable", "green")
    elif valor < 10:
        return ("🟠 Moderado", "orange")
    else:
        return ("🚨 ¿Te crees el lobo de Wall Street?", "red")

def mensaje_según_resultado(porcentaje, objetivo):
    if porcentaje >= objetivo * 1.5:
        return "🔥 Jordan Belfort, ¿eres tú?"
    elif porcentaje >= objetivo:
        return "🎯 ¡Bien hecho, lo lograste!"
    elif porcentaje > 0:
        return "📈 De poco a poquito se va llenando el huequito..."
    else:
        return "😓 No te desanimes, no siempre se gana."
