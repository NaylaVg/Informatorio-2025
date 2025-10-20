#  Creá una función mostrar_info() que reciba datos como nombre, edad, ciudad, etc, y los 
# muestre con un formato legible. 

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}") 

mostrar_info(nombre="Ana", edad=28, ciudad="Madrid", profesion="Bailarina")