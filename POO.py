class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}"

    def cumplir_anos(self):
        self.edad += 1

    def cambiar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion


class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, curso):
        super().__init__(nombre, edad, direccion)
        self.curso = curso

    def cambiar_curso(self, nuevo_curso):
        self.curso = nuevo_curso

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}, Curso: {self.curso}"




# Except Personalizado
class EdadInvalidaError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

def verificar_edad(edad):
    if edad < 0 or edad > 120:
        raise EdadInvalidaError("La edad debe estar entre 0 y 120 años.")
    return True
