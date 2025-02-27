texto = "Python es un lenguaje de programación. Python es fácil de aprender."
text_fine = texto.split()
frecuencia = {}

for palabra in text_fine:
    palabra = palabra.replace('.', '').replace(',', '')
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(frecuencia)
