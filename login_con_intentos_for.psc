Algoritmo login_con_intentos_for
		Definir usuario, contrasenia Como Cadena
		Definir intentos Como Entero
		
		intentos = 3
		Para intentos Desde 2 hasta 0 Hacer
			Escribir 'Ingrese su usuario'
			Leer usuario
			Escribir 'Ingrese su contraseña'
			Leer contrasenia
			
			
			Si usuario='admin' Y contrasenia='dificil123' Entonces
				Escribir 'Login exitoso. Bienvenido!'
				intentos = 0
			SiNo
				Escribir 'Credenciales incorrectas!'
				
				Escribir 'Le quedan ', intentos , ' intentos'
			FinSi
		Fin Para
FinAlgoritmo
