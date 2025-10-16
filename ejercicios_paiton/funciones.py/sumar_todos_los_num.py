# Definí una función sumar_todos() utilizando args que reciba una cantidad indefinida de 
# números y devuelva la suma total (Acá podemos usar la función integrada de python sum)

def sumar_todos(*args):
    return sum(args)

print(sumar_todos(1, 2, 3, 4, 5))