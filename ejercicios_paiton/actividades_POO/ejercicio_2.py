# Ejercicio 02 Programación Orientada a Objetos 🤩

# Consigna

# Crea una clase llamada Perro que tenga los atributos nombre y raza.
# Agrega un método llamado ladrar que muestre un mensaje con el nombre del perro diciendo "¡Guau!".
# Luego crea un objeto de esa clase y haz que ladre.

class Perro:

        def __init__(self, nombre, raza):
                self.nombre = nombre
                self.raza = raza

        def ladrar(self):
                print(f"{self.nombre}: ¡Guau!")

perro1 = Perro("negrito", "Salchicha")
perro2 = Perro("Homero", "Labrador")

perro1.ladrar()
perro2.ladrar()