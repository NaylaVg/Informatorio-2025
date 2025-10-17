from info_personas import mostrar_info, mayor_de_edad

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad: ")

print("\n Información de la persona:")
print(mostrar_info(nombre, edad, ciudad))

if mayor_de_edad(edad):
    print(" Es mayor de edad.")
else:
    print(" No es mayor de edad.")
