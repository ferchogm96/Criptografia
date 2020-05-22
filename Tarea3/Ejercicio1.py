#-*- coding: utf-8 -*-
from Crypto.Util import number
import random
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto.Random import get_random_bytes
import os


def rand_int():
	return random.randint(0, (2**(8*7))-1) # Se necesitan 14 bytes

def rc4_4bytes():
	key = b'key1'
	nonce = get_random_bytes(4)	# semilla random de 4 bytes 
	tempkey = SHA.new(nonce+key).digest()	# regresa un hash en bytes como string
	cipher = ARC4.new(tempkey)	# creamos un cifrador 
	msg = nonce + cipher.encrypt(b'hola')	# ciframos un mesnaje
	return int.from_bytes(msg, 'big')

def _urandom():
	f_byt = os.urandom(7) # Se necesitan 7 bytes
	f_entero = int.from_bytes(f_byt,'big')
	return f_entero


def cycle(fun, times):
	"""
		Función que calcula el valor de PI
		comparando si dos números aleatorios
		generados por la función 'fun' son coprimos,
		repitiendo el proceso 'times' veces, 
		cada que dos números son coprimos
		el valor de PI aumenta en uno
		
		fun - función que será ejecutada para crear números aleatorios
		times - número de veces que se ejecutará la comparación de dos números
	"""
	pi = 0
	# iteramos 'times' veces
	for i in range(times):
		x = fun()
		y = fun()
		# verificamos que si los aleatorios son coprimos
		if number.GCD(x, y) == 1:
			pi += 1
	return pi



#	Funciones para mandar a llamar en los ciclos
f_randint = rand_int	# función random.randint
f_rc4_4bytes = rc4_4bytes	#función rc4 con semilla de 4 bytes
f_urandom = _urandom

# Ciclos de ranint
print("Ciclos randint")
pi_randint_100 = cycle(f_randint, 100)
print("randint 100:",pi_randint_100)
pi_randint_1_000 = cycle(f_randint, 1000)
print("randint 1,000:",pi_randint_1_000)
pi_randint_10_000 = cycle(f_randint, 10000)
print("randint 10,000:",pi_randint_10_000)

# Ciclos de rc4
print("\nCilos rc4")
pi_rc4_100 = cycle(f_rc4_4bytes, 100)
print("rc4 100:",pi_rc4_100)
pi_rc4_1_000 = cycle(f_rc4_4bytes, 1000)
print("rc4 1,000:",pi_rc4_1_000)
pi_rc4_10_000 = cycle(f_rc4_4bytes, 10000)
print("rc4 10,000:",pi_rc4_10_000)

# Ciclos de urandom
print("\nCiclos urandom")
pi_urandom_100 = cycle(f_urandom, 100)
print("urandomt 100:",pi_urandom_100)
pi_urandom_1_000 = cycle(f_urandom, 1000)
print("urandom 1,000:",pi_urandom_1_000)
pi_urandom_10_000 = cycle(f_urandom, 10000)
print("urandom 10,000:",pi_urandom_10_000)