from file import *

class Repartiteur:
    def __init__(self,s):
        self.attenteTotale=0
        self.files=[]
        self.simul=s
    def entree_client(self):
        """ajoute un entier représentant le tour d'arrivée du client"""
        raise NotImplemented()
    
    def sortie_client(self,num):
        """retire un client de la file et ajoute son temps d'attente au total"""
        raise NotImplemented()
    
class RepartiteurUn(Repartiteur):
    def __init__(self, s):
        super().__init__(s)

class RepartiteurAlea(Repartiteur):
    def __init__(self, s):
        super().__init__(s)

class RepartiteurChoix(Repartiteur):
    def __init__(self, s):
        super().__init__(s)
    
class Client:
    def __init__(self,tick):
        self.temps_arrivee=tick

class File:
    def __init__(self):
        pass
    

class Guichet:
    def __init__(self):
        pass

    def tour(self):
        pass

class Simulateur:
    def __init__(self):
        pass