respuesta = str(input()) 

def play(v):
	print("//===============================================================//")
	print("Teclea No sé si quieres una ayuda, sólo puedes hacerlo una vez.")
	print("Teclea salir si quieres salir del juego, tienes 7 intentos")
	print("Suerte!!!!")
	print("//===============================================================//")
	while v >= 1:
		intento = str(input("Adivina la palabra: "))

		if intento == respuesta:
			print("Ganaste!!")
			v = 0 
		
		elif intento == "salir":
			break

		elif intento == "No sé":
			print(respuesta[:2])

		else:
			print("Error!!")
			v -= 1
			print("turnos restantes: ", v)
			print("//===============================================================//")

	print("Game Over")

vidas = 7
play(vidas)		

