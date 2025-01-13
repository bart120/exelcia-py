class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque #public
        self.__modele = modele #privé

    @property
    def modele(self):
        return self.__modele
    
    @modele.setter
    def modele(self, valeur):
        if valeur != "":
            self.__modele = valeur

    
