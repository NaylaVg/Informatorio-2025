# Creá un programa que guarde las notas de varios estudiantes en un diccionario, 
# Luego, crea funciones para: 
# A- Agregar estudiante con sus notas
#  B- Calcular el promedio de un estudiante
#  C- Mostrar los estudiantes aprobados (promedio >=6)

estudiantes = {}

def agregar_estudiante(nombre, notas):
    estudiantes[nombre] = notas
    print(f"Estudiante {nombre} agregado con notas {notas}")

def calcular_promedio(nombre):
    if nombre in estudiantes:
        notas = estudiantes[nombre]
        promedio = sum(notas) / len(notas)
        return promedio
    else:
        print(f"Estudiante {nombre} no encontrado.")
        return None

def mostrar_aprobados():
    aprobados = []
    for nombre in estudiantes:
        promedio = calcular_promedio(nombre)
        if promedio >= 6:
            aprobados.append((nombre, promedio))
    return aprobados

# Ejemplo de uso
agregar_estudiante("Gael", [9, 8, 9])
agregar_estudiante("Nayla", [8, 6, 7])
agregar_estudiante("Ana", [5, 4, 6])

print(f"Promedio de Gael: {calcular_promedio('Gael')}")
print(f"Promedio de Nayla: {calcular_promedio('Nayla')}")
print(f"Promedio de Ana: {calcular_promedio('Ana')}")
print("Estudiantes aprobados:", mostrar_aprobados())