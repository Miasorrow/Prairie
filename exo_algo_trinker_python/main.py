import json
from pprint import pprint
from termcolor import colored

with open('people.json', 'r') as p:
    people = json.loads(p.read())

print(colored("""
$$$$$$$$\\        $$\\           $$\\                           $$\\                               
\\__$$  __|       \\__|          $$ |                          $$ |                              
   $$ | $$$$$$\\  $$\\ $$$$$$$\\  $$ |  $$\\  $$$$$$\\   $$$$$$\\  $$ | $$$$$$\\ $$\\    $$\\  $$$$$$\\  
   $$ |$$  __$$\\ $$ |$$  __$$\\ $$ | $$  |$$  __$$\\ $$  __$$\\ $$ |$$  __$$\\\\$$\\  $$  |$$  __$$\\ 
   $$ |$$ |  \\__|$$ |$$ |  $$ |$$$$$$  / $$$$$$$$ |$$ |  \\__|$$ |$$ /  $$ |\\$$\\$$  / $$$$$$$$ |
   $$ |$$ |      $$ |$$ |  $$ |$$  _$$<  $$   ____|$$ |      $$ |$$ |  $$ | \\$$$  /  $$   ____|
   $$ |$$ |      $$ |$$ |  $$ |$$ | \\$$\\ \\$$$$$$$\\ $$ |$$\\   $$ |\\$$$$$$  |  \\$  /   \\$$$$$$$\\ 
   \\__|\\__|      \\__|\\__|  \\__|\\__|  \\__| \\_______|\\__|\\__|  \\__| \\______/    \\_/     \\_______|
================================================================================================
   
""", 'yellow'))
print(colored('Modele des données :', 'yellow'))
pprint(people[0])

# debut de l'exo
print(colored(''.join(['_' for _ in range(80)]), 'green', 'on_green'))

print(colored("Nombre d'hommes : ", 'yellow'))
# pour chaque personne du tableau, si son genre == 'Male' je le met dans le tableau hommes
hommes = [p for p in people if p['gender'] == 'Male']
# len() revoie la taille (nombre d'élément) d'un tableau
pprint(len(hommes))

################################################################################

# je peux aussi l'écrire avec une boucle classique
hommes2 = []                        # un tableau vide
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Male":  # si c'est un homme (2-266-02250-4)
        hommes2.append(person)      # je l'ajoute au tableau
print(len(hommes2))

################################################################################

# dans la même idée, plutot que de mettre tous les hommes dans un tableau
# puis afficher la longueur du tableau, je peux juste les compter dans une variable
nb_hommes = 0                       # je commence à 0
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Male":  # si c'est un homme
        nb_hommes = nb_hommes + 1   # j'ajoute 1 à mon compteur
print(nb_hommes)

################################################################################

print(colored("Nombre de femmes : ", 'yellow'))
# je peux compter les femmes ou calculer : nombre d'élement dans people - nombre d'homme
nb_femme = len(people) - nb_hommes
print(nb_femme)
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Nombre de personnes qui cherchent un homme :", 'yellow'))
nb_cherche_homme = 0
for person in people : 
    if person["looking_for"] == "M":
        nb_cherche_homme = nb_cherche_homme +1
print(nb_cherche_homme)
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Nombre de personnes qui cherchent une femme :", 'yellow'))
nb_cherche_femme= 0
for person in people : 
    if person["looking_for"] == "F":
        nb_cherche_femme = nb_cherche_femme +1
print(nb_cherche_femme)
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Nombre de personnes qui gagnent plus de 2000$ :", 'yellow'))
riche = 0
for person in people:
    salaire  = float(person["income"].replace("$", "").strip())
    if salaire > 2000 : 
        riche = riche +1

print(riche)


################################################################################

print(colored("Nombre de personnes qui aiment les Drama :", 'yellow'))
# là il va falloir regarder si le chaine de charactères "Drama" se trouve dans "pref_movie"
aime_drama = 0
for person in people : 
    if "Drama" in person["pref_movie"]:
        aime_drama = aime_drama +1
print(aime_drama)
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Nombre de femmes qui aiment la science-fiction :", 'yellow'))
# si j'ai déjà un tableau avec toutes les femmes, je peux chercher directement dedans ;)
"""femme = []
for person in people : 
    if person["gender"] == "Female":
        femme.append(person)
femme_sf = 0
for person in femme : 
    if 'Sci-Fi' in femme : 
        femme_sf = femme_sf+1

print(femme_sf)"""
femme_sf = 0
for person in people: 
    if 'Sci-Fi' in person["pref_movie"] : 
        if person["gender"] == "Female" :
            femme_sf = femme_sf+1

print(femme_sf)



################################################################################

print(colored('LEVEL 2' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))

################################################################################

print(colored("Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$", 'yellow'))
#salaire_smic= []
"""for person in people:
    salaire  = float(person["income"].replace("$", "").strip())
    if salaire > 1483: 
        salaire_smic.append(person)
riche_docu =0
for person in salaire_smic:
    if "Documentary" in salaire_smic :
        riche_docu = riche_docu + 1"""
riche_docu =0
for person in people:
    salaire  = float(person["income"].replace("$", "").strip())
    if salaire > 1482: 
        if "Documentary" in person["pref_movie"]:
            riche_docu = riche_docu + 1


print(riche_docu)



print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Liste des noms, prénoms, id et revenus des personnes qui gagnent plus de 4000$", 'yellow'))
list_par_salaire =0
for person in people:
    salaire  = float(person["income"].replace("$", "").strip())
    if salaire > 4000: 
        print(person["id"], person["first_name"], person["last_name"] )
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Homme le plus riche (nom et id) :", 'yellow'))


"""
croissant = sorted(people, float(person["income"].replace("$", "").strip()))

    #print(person["id"], person["first_name"], person["last_name"])"""
"""croissant = []
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Male":  # si c'est un homme
        croissant = max(
            people,
            key=lambda person: float(person["income"].replace("$", "").strip())
        )"""

#premier = croissant[0]

#print(premier["id"], premier["first_name"], premier["last_name"])

max = 0
riche_man = 0
for person in hommes2:               # pour chaque persone du tableau
    if person["gender"] == "Male": 
        salaire  = float(person["income"].replace("$", "").strip())
        if salaire > max : 
            max = salaire
            riche_man = person

print(riche_man["id"], riche_man["first_name"], riche_man["last_name"])




print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Salaire moyen :", 'yellow'))

total_salaire = 0

for person in people:
    salaire = float(person["income"].replace("$", "").strip())
    total_salaire += salaire

moyenne_salaire = total_salaire / len(people)
print(moyenne_salaire)
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Salaire médian :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Nombre de personnes qui habitent dans l'hémisphère nord :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Salaire moyen des personnes qui habitent dans l'hémisphère sud :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored('LEVEL 3' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))

################################################################################

print(colored("Personne qui habite le plus près de Bérénice Cawt (nom et id) :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Personne qui habite le plus près de Ruì Brach (nom et id) :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("les 10 personnes qui habitent les plus près de Josée Boshard (nom et id) :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Les noms et ids des 23 personnes qui travaillent chez google :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Personne la plus agée :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Personne la plus jeune :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))
print(colored("Moyenne des différences d'age :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored('LEVEL 4' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))
print(colored("Genre de film le plus populaire :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Genres de film par ordre de popularité :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Liste des genres de film et nombre de personnes qui les préfèrent :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Age moyen des hommes qui aiment les films noirs :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Age moyen des femmes qui aiment les drames et habitent sur le fuseau horaire, de Paris : ", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("""Homme qui cherche un homme et habite le plus proche d'un homme qui a au moins une
préférence de film en commun (afficher les deux et la distance entre les deux):""", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Liste des couples femmes / hommes qui ont les même préférences de films :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored('MATCH' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))
"""
    On match les gens avec ce qu'ils cherchent (homme ou femme).
    On prend en priorité ceux qui ont le plus de gouts en commun.
    Puis ceux qui sont les plus proches.
    Les gens qui travaillent chez google ne peuvent qu'être en couple entre eux.
    Quelqu'un qui n'aime pas les Drama ne peux pas être en couple avec quelqu'un qui les aime.
    Quelqu'un qui aime les films d'aventure doit forcement être en couple avec quelqu'un qui aime aussi 
    les films d'aventure.
    La différences d'age dans un couple doit être inférieure à 25% (de l'age du plus agé des deux)
    ߷    ߷    ߷    Créer le plus de couples possibles.                  ߷    ߷    ߷    
    ߷    ߷    ߷    Mesurez le temps de calcul de votre fonction         ߷    ߷    ߷    
    ߷    ߷    ߷    Essayez de réduire le temps de calcul au maximum     ߷    ߷    ߷    

"""
print(colored("liste de couples à matcher (nom et id pour chaque membre du couple) :", 'yellow'))
print(colored('Exemple :', 'green'))
print(colored('1 Alice A.\t2 Bob B.'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))
