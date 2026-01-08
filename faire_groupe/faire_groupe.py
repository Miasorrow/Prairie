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

##loç_àcd dhfhdjgkhfdkjghfjg

