from random import randint
from random import randrange
import random
from functools import reduce
from random import SystemRandom

def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    """
    rand = SystemRandom()
    if (size==None or size < 100):
        size = rand.randrange(100, 200)

    return rand.randrange(10 ** (size - 1), 10 ** size - 1)

def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    m = n - 1
    x = 0
    while m % 2 == 0:
        x = x + 1
        m >>= 1
    rand = SystemRandom()
    a = rand.randrange(1, n - 1)
    for j in range(0, x):
        if pow(a, m, n) == 1:
            print("True")
            return True
        if pow(a, (1 << j) * m, n) == n - 1:
            print("True")
            return True
    #print("False")
    return False

def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    f = factorial(n-1)
    #print("factorial de",n, "-1: ",f)
    if( f%n == n-1):
    	print("True")
    	return True
    elif( f%n != n-1):
    	print("False")
    	return False

def factorial(m):
	#Funcion auxiliar para sacar el factorial de un numero
	#param m : El numero inicial del factorial
	#return: El resultado final del factorial.
	resultado = 1
	for i in range(m):
		resultado *= (i + 1)
	return resultado


def generate_prime(size=None):
    """
    Genera un primo de al menos $size dígitos, si no se especifica,
    este tiene que asegurar que al menos tiene 100 dígitos.

    :param size: El tamaño del primo a generar.
    :return: Un número que se asegura que es primo.
    """
    #size = int(input("Ingresa el número de dígitos del primo que quieres generar: "))
    numeroGenerado = int(big_int(size))
    while(miller_rabin(numeroGenerado) != True):
    	numeroGenerado+=1
    #print(numeroGenerado)
    longitud = len(str(numeroGenerado))
    #print("Longitud: ",longitud)
    return numeroGenerado
