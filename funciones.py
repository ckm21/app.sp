
import yfinance as yf

def obtener_datos_y_senal(ticker, periodo):
    datos = yf.download(ticker, period="7d", interval=periodo)
    if datos.empty or len(datos) < 2:
        raise ValueError("No hay suficientes datos para analizar las velas.")
    senal = detectar_senal(datos)
    riesgo = evaluar_riesgo(datos)
    return datos, senal, riesgo

def detectar_senal(datos):
    if len(datos) < 2:
        raise ValueError("No hay suficientes datos para analizar las velas.")
    cuerpo_anterior = datos['Close'].iloc[-2] - datos['Open'].iloc[-2]
    cuerpo_actual = datos['Close'].iloc[-1] - datos['Open'].iloc[-1]
    if cuerpo_anterior < 0 and cuerpo_actual > 0:
        return 'Opción de compra'
    elif cuerpo_anterior > 0 and cuerpo_actual < 0:
        return 'Riesgo de pérdida / vender'
    else:
        return 'Sin señal clara'

def evaluar_riesgo(datos):
    rsi = calcular_rsi(datos['Close'])
    if rsi < 30:
        return 'Bajo'
    elif rsi > 70:
        return 'Alto'
    else:
        return 'Moderado'

def calcular_rsi(series, period=14):
    delta = series.diff()
    ganancia = delta.where(delta > 0, 0.0)
    perdida = -delta.where(delta < 0, 0.0)
    media_ganancia = ganancia.rolling(window=period).mean()
    media_perdida = perdida.rolling(window=period).mean()
    rs = media_ganancia / media_perdida
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]
