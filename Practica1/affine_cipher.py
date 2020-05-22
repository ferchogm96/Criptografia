#-*- coding:utf-8 -*-
from utils import CryptographyException

class Affine():

    def __init__(self, alphabet, A=None, B=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado afín.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            A -- El coeficiente A que necesita el cifrado.
            B -- El coeficiente B de desplazamiento.
        """
	self.A = A
	self.B = B
        self.alphabet = alphabet

    def cipher(self, message):
	new_cipher_msg = ""
	ce = CryptographyException()
	for cha in message:
		i = ce.get_index(cha, self.alphabet)
		c = (self.A*i+self.B)%len(self.alphabet)
		new_cipher_msg += self.alphabet[c] 
	print ("Mensaje Cifrado: %s" %(new_cipher_msg))	
	return (new_cipher_msg)
	
 

    def decipher(self, criptotext):
	new_decipher_msg = ""
	ce = CryptographyException()
	for cha in criptotext:
		i = ce.get_index(cha, self.alphabet)        
		dec = (ce.modInverso(self.A, len(self.alphabet))*(i - self.B))%len(self.alphabet)
		new_decipher_msg += self.alphabet[dec]
	print ("Mensaje Decifrado: %s"%(new_decipher_msg))	
	return (new_decipher_msg)
	
message = raw_input("Ingrese mensaje a Cifrar: ")
affine = Affine("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ",7 , 3)
mensajeCifrado = affine.cipher(message)

affine.decipher(mensajeCifrado)




