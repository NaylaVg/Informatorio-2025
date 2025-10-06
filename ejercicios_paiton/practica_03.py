# estudiante = {
#   "nombre": "Ana",
#   "edad": 20,
#   "materias": ["Matemática", "Historia"]
#}
#1- Mostrá el nombre y la edad
#2- Agregá una materia nueva a la lista materias
#3- Mostrá cuántas materias cursa con len()
#4- Usá .get() para obtener la clave “promedio” con valor por defecto 0

estudiante = {
   "nombre": "Ana",
   "edad": 20,
   "materias": ["Matemática", "Historia"]
}

print(estudiante["nombre"])

print(estudiante["edad"])

estudiante["materias"].append("Biología")
cantidad_materias = len(estudiante['materias'])

print("La cantidad de materias son: ", cantidad_materias)

promedio = estudiante.get("promedio", 0)
print("El promedio que tenes es: ", promedio)