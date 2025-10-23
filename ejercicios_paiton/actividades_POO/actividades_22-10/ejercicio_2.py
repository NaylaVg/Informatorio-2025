#  Polimorfismo – Vehículo {En este ejercicio, vamos a practicar el concepto de polimorfismo en Python. Crearás una clase 
# base llamada Vehiculo, y luego crearás varias clases derivadas que implementarán el método mover() de manera diferente, 
# dependiendo del tipo de vehículo.
#  Requerimientos: 
# 1- Clase Vehiculo: 
# * Debe tener un método mover(), pero este método debe estar vacío (puede estar definido con pass). Las clases hijas 
# implementarán este método de manera específica.
# 2- Clases derivadas de Vehiculo
#  * Clase Coche:
#  Debe sobrescribir el método mover() para que imprima: “El coche está conduciendo por la carretera”
#  * Clase Bicicleta:
#  Debe sobrescribir el método mover() para que imprima: “La bicicleta está pedaleando” 
# * Clase Avion:
#  Debe sobrescribir el método mover() para que imprima: “El avión está volando en el cielo” 
# 3- Polimorfismo:
#  * Crea una lista de objetos que incluya instancias de las clases Coche, Bicicleta y Avion.
#  * Utiliza un bucle for para recorrer la lista y llamar al método mover() en cada vehículo. El resultado debe ser 
# diferente dependiendo del tipo de vehículo, lo que demuestra el uso del polimorfismo. 


class Vehiculo:

    def __init__(self):
        pass

    def mover(self):
        pass

class Coche:

    def __init__(self):
        super().__init__()
        pass

    def mover(self):
        super().__init__()
        return "El coche está conduciendo por la carretera"

class Bicicleta:

    def __init__(self):
        super().__init__()
        pass

    def mover(self):
        super().__init__()
        return "La bicicleta está pedaleando"

class Avión:

    def __init__(self):
        super().__init__()
        pass

    def mover(self):
        super().__init__()
        return "El avión está volando en el cielo"
    

transportes = [Coche(), Bicicleta(), Avión()]

for Vehiculo in transportes:
    print(Vehiculo.mover())