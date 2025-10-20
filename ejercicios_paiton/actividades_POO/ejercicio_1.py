# Consigna 🐍

# Crea una clase llamada Persona que tenga los atributos nombre y edad.
# Luego, crea un método que muestre un saludo con el nombre y la edad de la persona.
# Finalmente, crea un objeto de esa clase y haz que se muestre su saludo.


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")


persona1 = Persona("Darío", 35)
persona2 = Persona("Gael", 7)


persona1.saludar()
persona2.saludar()