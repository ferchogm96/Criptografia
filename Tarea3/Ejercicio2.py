# -*- coding: utf-8 -*-
from arc4 import ARC4 	# instalar pip install arc4
from Crypto import Random
from pprint import pprint
# 


def apply_OR(bytes_a, bytes_b):
	"""
		Suponemos que bytes_b será el que tendrá más bytes
		para este caso, k
	"""
	result = bytearray(len(bytes_b))
	module = len(bytes_a)
	for index, b_b in enumerate(bytes_b):	# suponemos que bytes_b es de mayor tamaño
		result[index] = (b_b|bytes_a[index%module])	# aplicamos el OR a cada byte de bytes_b con los bytes_a
	return bytes(result)

def apply_XOR(bytes_a, bytes_b):
	"""
		Suponemos que bytes_b será el que tendrá más bytes
		para este caso, el mensaje
	"""
	result = bytearray(len(bytes_b))
	module = len(bytes_a)
	for index, b_b in enumerate(bytes_b):	# suponemos que bytes_b es de mayor tamaño
		result[index] = (b_b^bytes_a[index%module])
		#result += str(b_b^bytes_a[index%module])	# aplicamos el OR a cada byte de bytes_b con los bytes_a
	return bytes(result)

parejas_sc = []

def fun_que_hace_todo(iteration):
	k = Random.get_random_bytes(128)	# llave compartida
	m = 'Algun mensaje mamalon super secret con hartos valores que superan el numero de bytes de la llave k para que pueda funcionar el supuesto aplicado'	# mensaje a compartir
	s =  Random.get_random_bytes(48)	# llave aleatoria
	# Se aplica el primer OR entre s|k
	bytes_or = apply_OR(s, k)
	arc4 = ARC4(k)	# Creamos una instancia de RC4 con la llave compartida
	# Aplicamos el RC4 al OR sería la parte de RC4(s|k)
	cipher = arc4.encrypt(bytes_or)
	# Obtenemos la parte RC4(s|k) XOR m
	c = apply_XOR(cipher, bytes(m, 'utf-8'))

	parejas_sc.append((iteration, c))

	# Aplicamos el inverso del XOR
	decipher = apply_XOR(cipher, c)

for x in range(100):
	fun_que_hace_todo(x)

pprint(parejas_sc)


