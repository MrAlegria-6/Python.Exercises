def guardar_nombres(nombres, archivo):
    with open(archivo, 'w') as f:
        for nombre in nombres:
            f.write(nombre + '\n')

def leer_nombres(archivo):
    with open(archivo, 'r') as f:
        nombres = f.read().splitlines()
    return nombres
