import random

def generar_hechizo():
    Prefijos = ['Abra', 'Alakaza', 'Zendo', 'Foco', 'Magi']
    Sufijos = ['cadabra', 'lumos', 'mora', 'nox', 'flama']

    prefijo_aleatorio = random.choice(Prefijos)
    sufijo_aleatorio = random.choice(Sufijos)
   
    print(f"{prefijo_aleatorio}-{sufijo_aleatorio}")

generar_hechizo()


