import csv

def crear_csv(empleados, archivo):
    with open(archivo, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Edad", "Cargo", "Salario"])
        for empleado in empleados:
            writer.writerow(empleado)

def leer_calcular(archivo):
    cargos = []
    salarios = []
    
    with open(archivo, mode='r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            nombre, edad, cargo, salario = row
            cargos.append(cargo)
            salarios.append(float(salario))
    
    salario_promedio_por_cargo = {}
    for i in range(len(cargos)):
        cargo = cargos[i]
        salario = salarios[i]
        if cargo not in salario_promedio_por_cargo:
            salario_promedio_por_cargo[cargo] = {'total': 0, 'cantidad': 0}
        salario_promedio_por_cargo[cargo]['total'] += salario
        salario_promedio_por_cargo[cargo]['cantidad'] += 1
    
    for cargo, data in salario_promedio_por_cargo.items():
        promedio = data['total'] / data['cantidad']
        salario_promedio_por_cargo[cargo] = promedio
    
    return salario_promedio_por_cargo
