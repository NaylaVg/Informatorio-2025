# ------------------------------------------------------------------------------
# Realizá un programa en Python que permita al usuario ingresar 10 números enteros. El programa debe:

# Almacenar los números ingresados en una lista.

# Calcular la suma de todos los números pares.

# Contar cuántos números impares se ingresaron.

# Mostrar por pantalla:

# La lista completa de números ingresados.

# La cantidad de los números pares.

# La cantidad de números impares

numeros = []

for i in range(10):
    n = int(input(f"Ingresa un numero: "))
    numeros.append(n)

pares = [n for n in numeros if n %2 ==0]
impares = [n for n in numeros if n %2 !=0]

suma_pares = sum(pares)
print(f"La suma de todos los números pares es: ", suma_pares)

cantidad_impares = len(impares)
print(f"La cantidad de números pares ingresados son: ", cantidad_impares)

print(f"La lista completa de los números es: ", numeros)