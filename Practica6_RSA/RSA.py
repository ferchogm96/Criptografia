from prime_generator import generate_prime
from utils import prime_relative
from random import randint

class RSA():

    def __init__(self):
        """
        Constructor de RSA, aquí se deben de generar los primos p y q
        para que puedan ser vistos por toda la clase, así como la llave
        pública y privada.
        """
        #Aquí también deben de generar su priv_key y pub_key
        
        self.p = generate_prime()
        self.q = generate_prime()
        self.n = self.p * self.q
        self.phi_n = self.__phi__()
       	self.e = self.generaE()
       	self.d = self.generaD()
        self.pub_key = self.e % self.n
        self.priv_key = self.d
        """
        e es un numero primo relativo con phi(n)
        d es el inverso de d mod phi(n)
       	genera archivos de las llaves publica y privada. e d congr 1 mod n
        """
        #SE CREA EL ARCHIVO DE PUBLIC KEY
        n0 = str(self.n)
        e0 = str(self.e)
        llave_publica = n0+"\n"+e0
       	#Hay que guardar (n,e)
       	out_file1 = open("pub_key", "w") 
       	out_file1.write(llave_publica)
       	out_file1.close()

        #SE CREA EL ARCHIVO DE PRIVATE KEY
        d0 = str(self.d)
        llave_privada = n0+"\n"+d0
        #Hay que guardar (n,d)
        out_file2 = open("priv_key", "w") 
        out_file2.write(llave_privada)
        out_file2.close()

    def generaE(self):
    	#e es un numero primo relativo con phi(n)
        self.e = 0
        while not prime_relative(self.e,self.phi_n):
            self.e = randint(1,self.n)
        print("e: ",self.e)
        return self.e

    def generaD(self):
        #d es el inverso multiplicativo de e mod phi(n)
        self.d = self.AEE(self.e,self.phi_n)
        return self.d

    #Algoritmo Extendido de Euclides para sacar el mcd de dos numeros    
    def AEE(self,a,b):
        if b == 0:
            return 0,1,0
        u0 = 1
        u1 = 0
        v0 = 0
        v1 = 1
        while b != 0:
            q = a//b
            r = a - b * q
            u = u0 - q * u1
            v = v0 - q * v1
            #Update a,b
            a = b
            b = r
            #Update for next iteration
            u0 = u1
            u1 = u
            v0 = v1
            v1 = v
        return  u0

    def __phi__(self):
        """
        Función completamente privada y auxiliar, únicamente para el uso de las
        pruebas unitarias.
        :return: el número de primos relativos con n.
        """
        self.phi_n = (self.p-1)*(self.q-1)
        print("phi de n: ", self.phi_n)
        return self.phi_n

    #Funcion auxiliar que calcular el exponencial modular rapido a^n mod(m)
    def exp_mod(self,a, b, m):
        exp = 1
        while(b):
            if(b&1):
                exp = (exp*a)%m
            b>>=1
            a = ((a%m)*(a%m))%m
        return exp

    def encrypt(self, message):
        """
        Encripta un mensaje recibido como parámetro y lo regresa a manera
        de lista de enteros.
        :param message: el mensaje a encriptar.
        :return: una lista de enteros con el mensaje encriptado.
        c = m^e mod(n)
        """
        in_file = open("pub_key", "r") 
        lineas = in_file.read() 
        in_file.close()
        n, e = lineas.split(sep='\n')
        n = int(n)
        e = int(e)
        lista = []
        for m in message:
            m1 = ord(m)
            c = self.exp_mod(m1,e,n) 
            lista.append(c)

        print("mensaje encriptado: ",lista)
        return lista

    def decrypt(self, criptotext):
        """
        Desencripta un criptotexto cifrado con RSA y lo regresa a manera
        de cadena, recuperando la información del mensaje original.
        :param criptotext: el mensaje recibido que se va a desencriptar.
        :return: una cadena con el mensaje original.
        m = c^d mod(n)
        """
        in_file = open("priv_key", "r") 
        lineas = in_file.read() 
        in_file.close()
        n, d = lineas.split(sep='\n')
        n = int(n)
        d = int(d)
        mensaje = ''
        for c in criptotext:
            m = self.exp_mod(c,d,n)
            m1 = chr(m)
            mensaje += m1    
        print("mensaje original: ",mensaje)
        return mensaje


c=RSA()
#m="Hola mundo como esta, mi nombre es Fernando y estoy cifrando un text con RSA"
#res = c.encrypt(m)
#res2 = c.decrypt(res)

phi_n=c.__phi__()

"""
cifrado = 10
pub_key =(35,5)
e= 5
n = 35 = p*q = 7 * 5
phi_n = (p-1)*(q-1) = 6*4 =24
"""
