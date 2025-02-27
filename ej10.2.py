import random

def generar_contraseña(longitud):
    if longitud < 4:
        return ValueError("La longitud debe ser al menos 4 para garantizar un carácter de cada tipo")

  #caracteres Posibles
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()-_=+[]{}|;:,.<>?'

#un Caracter de cada tipo
    contrasena = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    #Digitos Ramdom 
    todos_los_caracteres = mayusculas + minusculas + numeros + simbolos
    contrasena += random.choices(todos_los_caracteres, k=longitud - 4)

    # Mezclar los caracteres
    random.shuffle(contrasena)

    # Convertirla en una cadena
    return ''.join(contrasena)

#Ejemplo
longitud = 12  
contrasena_generada = generar_contraseña(longitud)
print(f"Contraseña generada: {contrasena_generada}")
