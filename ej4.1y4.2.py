import time

def suma_total(*numeros):
    return sum(numeros)

def medir_tiempo(func, *args):
    start_time = time.time()
    resultado = func(*args)
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    return resultado

resultado = medir_tiempo(suma_total, 1, 2, 3, 4)

print("Resultado de la suma:", resultado)
