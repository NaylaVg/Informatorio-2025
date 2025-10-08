# Nivel 4 | Sistema de votación {
# Se quiere implementar un sistema básico de votación donde cada persona puede votar una
# sola vez por su candidato favorito
# A- El programa debe permitir que tres personas voten
# B- Antes de permitir votar, debe pedir el nombre del votante
# C- Si el votante ya emitió su voto anteriormente, debe mostrar un mensaje: “Ya votaste” y
# no permitirle votar de nuevo
# D- Si es la primera vez que vota, el sistema debe pedir el nombre del candidato al que desea
# votar.
# E- Al finalizar, el programa debe mostrar los resultados con la cantidad de votos que recibió
# cada candidato
# }

votacion = []

for i in range(3):
    nombre: input(f"Ingrese su nombre: ")
    voto: input(f"Ingrese el candidato que quiere votar: ")
    votacion = [nombre, voto]

buscar_nombre = (f"Ingrese su nombre: ")
if buscar_nombre in votacion:
    votacion[buscar_nombre] = (nombre)
    print(f"¡Su nombre ya se encuentra registrado!, {votacion})
          
