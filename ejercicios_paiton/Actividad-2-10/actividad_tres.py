# Nivel 2 | Registro de Stock {
# Dado un diccionario llamado stock que contiene productos como claves y una tupla con su
# precio y cantidad disponible como valor, escribí un programa que:
# A- Le pida al usuario que ingrese el nombre de un producto
# B- Verifique si el producto existe en el diccionario
# C- Si existe, muestre por pantalla el precio y la cantidad disponible
# D- Si no existe, deja un mensaje de que no se encontró el producto
# }

stock = {}

buscar_producto = input(f"Ingresa el producto que solicita buscar: ")

if buscar_producto in stock:
    precio, cantidad_disponible = stock[buscar_producto]
    print(f"¡Producto encontrado!, Nombre: {buscar_producto}, Precio: ${precio}, cantidad: {cantidad_disponible}")
else:
    print(f"No se encontró el producto indicado")
