#-*- coding:utf-8 -*-
from utils import CryptographyException


class Vigenere():

    def __init__(self, alphabet, password=None):
        #Recomendación, ingeniárselas para no cargar siempre O(n^2) en memoria aunque esto no
        #será evaluado, con n el tamaño del alfabeto.
        """
        Constructor de clase, recibe un parámetro obligatorio correspondiente al alfabeto
        y un parámetro opcional que es la palabra clave, en caso de ser None, entonces
        generar una palabra pseudoaleatoria de al menos tamaño 4.
        :param alphabet: Alfabeto a trabajar con el cifrado.
        :param password: El password que puede ser o no dada por el usuario.
        """
        self.alphabet = alphabet
        self.password = password
        ce = CryptographyException()
        

    def cipher(self, message):
        """
        Usando el algoritmo de cifrado de vigenere, cifrar el mensaje recibido como parámetro,
        usando la tabla descrita en el PDF.
        :param message: El mensaje a cifrar.
        :return: Una cadena de texto con el mensaje cifrado.
        """
        new_cipher_msg = ""
        ce = CryptographyException()
        for index,cha in enumerate(message):
        	i = ce.get_index(cha, self.alphabet) #	Se obtiene el indice de cada caracter de la clave
        	cha_clave = self.password[index%len(self.password)]
        	j = ce.get_index(cha_clave, self.alphabet) #	Se obtiene el indice de cada caracter del mensaje
        	c = (i+j)%len(self.alphabet)
        	new_cipher_msg += self.alphabet[c] 
        print ("Mensaje Cifrado: %s" %(new_cipher_msg))
        return (new_cipher_msg)

    def decipher(self, ciphered):
        """
        Implementación del algoritmo de decifrado, según el criptosistema de vigenere.
        :param ciphered: El criptotexto a decifrar.
        :return: El texto plano correspondiente del parámetro recibido.
        """
        new_decipher_msg = ""
        ce = CryptographyException()
        for index,cha in enumerate(ciphered):
        	i = ce.get_index(cha, self.alphabet) #	Se obtiene el indice de cada caracter de la clave
        	cha_clave = self.password[index%len(self.password)]
        	j = ce.get_index(cha_clave, self.alphabet) #	Se obtiene el indice de cada caracter del mensaje
        	dec = (i-j)%len(self.alphabet)
        	new_decipher_msg += self.alphabet[dec] 
        print ("Mensaje Decifrado: %s" %(new_decipher_msg))
        return (new_decipher_msg)

message = input("Ingrese mensaje a Cifrar: ")
#password = input("Ingrese Clave minima de 4 cifras: ")
vigenere = Vigenere("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",password)
#mensajeCifrado = vigenere.cipher(message)
vigenere.decipher(message)

