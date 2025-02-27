from datetime import datetime

#Calcular edad exacta
def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    edad_anios = hoy.year - fecha_nacimiento.year
    edad_meses = hoy.month - fecha_nacimiento.month
    edad_dias = hoy.day - fecha_nacimiento.day

    if edad_meses < 0:
        edad_años -= 1
        edad_meses += 12

    if edad_dias < 0:
        edad_meses -= 1
        edad_dias += (hoy.replace(year=hoy.year, month=hoy.month-1) - fecha_nacimiento).days
    
    return edad_anios, edad_meses, edad_dias

# Función para calcular los días faltantes para el próximo cumpleaños
def dias_para_proximo_cumple(fecha_nacimiento):
    hoy = datetime.today()
    proximo_cumple = fecha_nacimiento.replace(year=hoy.year)

    if hoy > proximo_cumple:
        proximo_cumple = proximo_cumple.replace(year=hoy.year + 1)
    
    dias_faltantes = (proximo_cumple - hoy).days
    return dias_faltantes

