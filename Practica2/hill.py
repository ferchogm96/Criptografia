from utils import CryptographyException
import copy, random

class Hill():

    def __init__(self, alphabet, n, key=None):
        """
        Constructor de clase, recibiendo un alfabeto completamente necesario pero
        podría no recibir una llave de cifrado, en cuyo caso, hay que generar una,
        para el caso del tamañHo de la llave, hay que asegurarse que tiene raíz entera.
        :param alphabet: una cadena con todos los elementos del alfabeto.
        :param n: el tamaño de la llave, obligatorio siempre.
        :param key: una cadena que corresponde a la llave, en caso de ser una llave inválida
        arrojar una CryptographyException.
        """
        self.alphabet = {
                'a': 0,  'b': 1,  'c': 2,  'd': 3,  'e': 4,  'f': 5,  'g': 6,  'h': 7,  
                'i': 8,  'j': 9,  'k': 10, 'l': 11, 'm': 12, 'n': 13, 'ñ': 14, 'o': 15, 
                'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                'x': 24, 'y' : 25, 'z' : 26
            }
        self.n=n
        
        if(key):
            self.key = key
        else:
            self.key = random.randint(27,4)


    valores_num = {v: k for k, v in valores.items()}        

   
    def cipher(self, message):
        """
        Aplica el algoritmo de cifrado con respecto al criptosistema de Hill, el cual recordando
        que todas las operaciones son mod |alphabet|.
        :param message: El mensaje a enviar que debe ser cifrado.
        :return: Un criptotexto correspondiente al mensaje, este debe de estar en representación de
        cadena, no lista.
        """
        self.message=message
        
        criptotexto = "";
        message = message.replace(" ", "")
        message = message.lower()
        """Cortar la llave de 2*2"""
        a = key[0]
        b = key[1]
        c = key[2]
        d = key[3]
            
        clave = [[a,b],[c,d]]
        if (len(message)%2 != 0):
            message += 'a' 
        if (n==2):
            for m in range(0,len(message), 2):
                temp = [0,0]
                temp[0] = valores[message[m]]
                temp[1] = valores[message[m+1]]
                pareja = (np.dot(temp,clave)%27)
                respuesta += str(valores_num[pareja[0]]) + str(valores_num[pareja[1]])
        
        return criptotexto;
        

    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """
        self.ciphered
        textoclaro = "";
        message = message.replace(" ", "")
        message = message.lower()
        """Cortar la llave de 2*2"""
        a = key[0]
        b = key[1]
        c = key[2]
        d = key[3]
        
        
        clave = [[a,b],[c,d]]
        clave_inversa=[[d,(-b)%26],[(-c)%26,a]]  
        if (len(message)%2 != 0):
            message += 'a' 
        if (n==2):
            for m in range(0,len(message), 2):
                temp = [0,0]
                temp[0] = valores[message[m]]
                temp[1] = valores[message[m+1]]
                pareja = (np.dot(temp,clave_inversa)%27)
                respuesta += str(valores_num[pareja[0]]) + str(valores_num[pareja[1]])
        
        return textoclaro;
