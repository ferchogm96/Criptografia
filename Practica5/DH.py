from random import randint

class Participant():


    def __init__(self, p, g, participant):
        """
        Constructor de clase
        """
        self.p = p
        self.g = g
        self.participant = participant
        self.x = randint(0,1000) % self.p
        self.X = 0

    def seed(self):
        """
        Generador de la parte propia del intercambio de Diffie-Hellmann
        """
        self.X = self.g**self.x % self.p      
        return self.X   

    def exchange(self):
        """
        Adquiero el número de la otra persona y calculo mi propia llave.
        """
        s =  self.participant.seed()**self.x % self.p
        print("S: ",s)
        return s
