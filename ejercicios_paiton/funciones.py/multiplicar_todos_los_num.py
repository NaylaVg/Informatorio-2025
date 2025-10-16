# Escribí una función multiplicar() utilizando args, que reciba varios números y devuelva el 
# resultado de multiplicarlos todos. 

def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

    if not args:
        return 1
    
print(multiplicar_todos(1, 2, 3))