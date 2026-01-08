# Algo en python


Faite la liste des prénoms de tous les apprenants de la promo dans un tableau
json dans un fichier .json
Créez une fonction groupes qui prend en paramètre un nombre k.
Cette fonction doit retourner un tableau qui contient des tableaux.
Chaque sous-tableau doit contenir un ensemble de k nom, sans doublon,
répartis aléatoirement.
Le programme doit afficher le résultat d’une manière ou d’une autre.
En bref, notre fonction groupes crée des groupes aléatoires de k apprenants.


```py
import math 
import random
eleves = ["a","b","c","d","e"]

# combien de groupe
k=2
n = len(eleves)
nb_de_grp = math.ceil(n/k) 
print("nb de groupe",nb_de_grp)

groupes = []

for i in range(nb_de_grp):
    groupes.append([])
print("groupe= ", groupes)

while len(eleves)>0:

    indice_au_hazard = random.randrange(0,len(eleves))
    eleve = eleves[indice_au_hazard]
    eleves.remove(eleve)
    print(indice_au_hazard)

groupe_hazard=random.randrange(0,nb_de_grp)
while len(groupes[groupe_hazard]) == k:
    groupe_hazard=random.randrange(0,nb_de_grp)
    groupes[groupe_hazard].append(eleve)

print(groupes)

```