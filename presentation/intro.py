
'''
grand commentaire
'''
nom: str = "Alain"
prix: float = 344

def __presentation__():
    est_present: bool = False # commentaire
    if est_present:
        print(f"Bonjour {nom}")
    elif prix == nom:
        print("y'a personne")
    else:
        print("erreur")

presentation()
#print(est_present)

