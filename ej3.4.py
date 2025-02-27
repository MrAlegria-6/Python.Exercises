estudiantes = {
    "Juan": {"edad": 20, "curso": "Python", "promedio": 8.5},
    "María": {"edad": 22, "curso": "Java", "promedio": 9.0},
    "Pedro": {"edad": 21, "curso": "Python", "promedio": 7.8}
}

# a) Agregar un nuevo estudiante
estudiantes["Ana"] = {"edad": 23, "curso": "C++", "promedio": 8.0}

# b) Actualizar el promedio de Juan a 9.0
estudiantes["Juan"]["promedio"] = 9.0

# c) Mostrar solo los estudiantes de Python
python_students = {nombre: info for nombre, info in estudiantes.items() if info["curso"] == "Python"}
print("Estudiantes de Python:", python_students)

# d) Calcular el promedio de edad de todos los estudiantes
promedio_edad = sum([info["edad"] for info in estudiantes.values()]) / len(estudiantes)
print("Promedio de edad:", promedio_edad)
