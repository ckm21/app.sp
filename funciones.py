# funciones.py

def calcular_porcentaje_ganancia(precio_entrada, precio_actual):
    if precio_entrada == 0:
        return 0
    return round(((precio_actual - precio_entrada) / precio_entrada) * 100, 2)

def clasificar_objetivo(porcentaje):
    if porcentaje < 7:
        return ("🟢 Objetivo alcanzable", "verde")
    elif porcentaje < 13:
        return ("🟠 Objetivo moderado", "naranja")
    else:
        return ("🧨 ¿Te crees el lobo de Wall Street?", "rojo")

def mensaje_según_resultado(porcentaje):
    if porcentaje < 7:
        return "Buen objetivo."
    elif porcentaje < 13:
        return "Objetivo razonable, pero desafiante."
    else:
        return "Te deseo mucha suerte… o mucha fe."

def obtener_datos():
    return {
        "AAPL": {"entrada": 170.0, "actual": 177.65},
        "WOLF": {"entrada": 2.10, "actual": 2.06},
        "MSFT": {"entrada": 502.0, "actual": 514.25}
    }
