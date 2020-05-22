import math
import random

class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message

    def get_index(self,c,alpahabet):
    	for i,x in enumerate(alpahabet):
    		if c == x:
    			return (i)
    	return (None)

    def generaClave(self, alphabet):
        clave = ""
        for x in range(0,4):
            x = random.range(len(self.alphabet))
            clave += alphabet[x]
        print (clave)
        return (clave)
