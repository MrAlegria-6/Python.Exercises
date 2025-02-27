import re

def extraer_fechas(texto):
    patron = r'\b\d{2}/\d{2}/\d{4}\b'
    fechas = re.findall(patron, texto)
    return fechas

texto = "La reunión será el 15/04/2023 y la entrega está programada para el 30/05/2023."
fechas = extraer_fechas(texto)
print(fechas)
