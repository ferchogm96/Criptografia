import copy, random
class Caesar():

    def __init__(self, alphabet, key=None):
        self.alphabet = alphabet
        if(key):
            self.key = key
        else:
            self.key = random.randint(3,len(alphabet)-1) 
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado de César.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            key -- el tamaño del desplazamiento sobre el alfabeto, si es
                   None, se debe de escoger una llave aleatoria, válida.
        """
        pass

    def cipher(self, message, flag=None):
        if(not flag and self.alphabet.count(" ") == 0):
            message = message.replace(" ","")
        clair_message = copy.copy(message)
        
        for i in range(len(self.alphabet)):
            #for j in range(len(message)): 
            new_char = self.alphabet[(i + self.key) % len(self.alphabet)]
            for j in range(len(clair_message)):
                if (message[j]== self.alphabet[i]):
                    clair_message = clair_message[:j] + new_char + clair_message[j+1:]
        return clair_message

        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado césar, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        pass

    def decipher(self, criptotext, flag=None):
        if(not flag and self.alphabet.count(" ") == 0):
            criptotext = criptotext.replace(" ","")
        clair_message = copy.copy(criptotext)

        for i in range(len(self.alphabet)):
            new_char = self.alphabet[(i - self.key) % len(self.alphabet)]
            for j in range(len(clair_message)):
                if (criptotext[j]== self.alphabet[i]):
                    clair_message = clair_message[:j] + new_char + clair_message[j+1:]
        return clair_message      
        
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el algoritmo de césar.
        Parámetro:
            cryptotext -- el mensaje a descifrar.
        """
        pass
