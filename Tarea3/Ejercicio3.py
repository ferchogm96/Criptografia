
from arc4 import ARC4 
import random

rand = random.randint(1,10)
print("LLave:",6)

def cifrar(r):
	file = open("archivo_prueba.txt", "rb")
	filecipher = open("archivo_prueba_cifrada.txt", "wb")
	contenido = ""
	arc4 = ARC4(bytes(r))

	for x in file:
		contenido += str(x)
		cipher = arc4.encrypt(x)
		filecipher.write(cipher)
		print(x)

	print("\nContenido cifrado:",contenido)

def descifrar(r):
	file = open("archivo_prueba_cifrada.txt", "rb")
	contenido = ""
	plano = ""
	arc4 = ARC4(bytes(r))
	for x in file:
		contenido += str(x)
		plano += str(arc4.decrypt(x), "utf-8")
		print(x)

	print("\nContenido decifrado:",plano)
	
cifrar(6)
descifrar(6)