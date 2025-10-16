# Creá una función registrar_usuario() que reciba_
#  *args con los intereses del usuario, por ejemplo (Música, Programación, Videojuegos, etc)
#  **kwargs con su información básica (nombre, edad, etc.)
#  Y que devuelva un resumen legible. 

def registrar_usuario(*args, **kwargs):
    intereses = ', '.join(args)
    info_basica = ', '.join(f"{clave.capitalize()}: {valor}" for clave, valor in kwargs.items())
    return f"Información del usuario:\n{info_basica}\nIntereses: {intereses}"   

print(registrar_usuario("Música", "Inglés", "Basket", nombre="Darío", edad=35, ciudad="Resistencia"))