#from poo import Voiture as Voit
from poo import Voiture, conso_max
from exceptions import VideException

try:
    v = Voiture("fiat", "", 4)
    v.modele = ""
    print(v)
except VideException as e:
    print(e)
except Exception:
    print("Grosse erreur")
finally :
    print("toujours éxécuté")