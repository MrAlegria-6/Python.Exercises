# main.py

from mis_matematicas import suma, resta, multiplicacion, division, factorial, es_primo

# Usando las funciones importadas
print(suma(5, 3))  # Resultado esperado: 8
print(resta(10, 4))  # Resultado esperado: 6
print(multiplicacion(6, 7))  # Resultado esperado: 42
print(division(8, 2))  # Resultado esperado: 4.0
print(division(5, 0))  # Resultado esperado: Error: División por cero.
print(factorial(5))  # Resultado esperado: 120
print(es_primo(11))  # Resultado esperado: True
print(es_primo(9))  # Resultado esperado: False
