import json

class Personne:
    age_du_capitaine:int  # variable de class pas dans le init

    def __init__(self, **kwargs):
        self.__nom = kwargs['nom']
        self.__age = kwargs['age']
        self.__description = ""
        if 'description' in  kwargs.keys():
            self.__description = kwargs['description']

    def afficher(self):
        print(self.__description)

    def get_nom(self):
        return self.__nom
    
    def set_nom(self, nom):
        self.__nom = nom

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
    
    def __str__(self):
        return self.__nom
    
    def __repr__(self):
        return json.dumps(self.__dict__, indent=3)
    
pers = Personne(nom="bob", age=12)
print(pers.get_nom())
print(pers.age)
pers.afficher()
print(pers) # appel __str__ ou __repr__ si __str__ pas défini
print(repr(pers)) # appel __repr__
        
        
    
