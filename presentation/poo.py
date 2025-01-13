from abc import ABC, abstractmethod
from exceptions import VideException
conso_max = 10 

class Vehicule(ABC):
    def __init__(self, marque, modele):
        self.marque = marque #public
        self.__modele = None #privé
        self.modele = modele

    @property
    def modele(self):
        return self.__modele
    
    @modele.setter
    def modele(self, valeur):
        """
        définir le modèle

        Raises:
            VideException: si le modèle est vide
        """
        if valeur != "":
            self.__modele = valeur
        else:
            raise VideException("modele")
    
    @abstractmethod
    def demarrer(self):
        pass

    def __str__(self):
        return f"{self.marque} {self.__modele}"

class Voiture(Vehicule):
    def __init__(self, marque, modele, nbr_portes):
        super().__init__(marque, modele)
        self.nbr_portes = nbr_portes
    
    def demarrer(self):
        print(f"La voiture {self.marque} {self.modele} démarre.")

    def __str__(self):
        return f"{super().__str__()} et {self.nbr_portes}"




