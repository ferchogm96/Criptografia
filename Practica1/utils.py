import math

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

    def modInverso(self, a, m):
    	a = a % m
    	for x in range (1, m):
    		if (a*x) % m == 1:
    			return x
    	return 1

    	