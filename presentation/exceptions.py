
class VideException(Exception):
    """
    Classe représentant une exception vide.

    Blablabla plus long
    Blablabla plus long
    
    """

    #def __init__(self, *args):
    #    super().__init__(*args)

    def __init__(self, nom_du_champ):
        self.message = f"La valeur de {nom_du_champ} est vide."
        super().__init__(self.message)