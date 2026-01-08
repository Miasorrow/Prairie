# J'ai pas d'idée de titre


1. je peux compter les femmes ou calculer : nombre d'élement dans people - nombre d'homme

```py
nb_femme = len(people) - nb_hommes
print(nb_femme)
```

2.Nombre de personnes qui cherchent un homme :

```py
nb_cherche_homme = 0
for person in people : 
    if person["looking_for"] == "M":
        nb_cherche_homme = nb_cherche_homme +1
print(nb_cherche_homme)
```

3. Nombre de personnes qui cherchent une femme :

```py
nb_cherche_femme= 0
for person in people : 
    if person["looking_for"] == "F":
        nb_cherche_femme = nb_cherche_femme +1
print(nb_cherche_femme)
```

4. Nombre de personnes qui gagnent plus de 2000$ :

```py
riche = 0
for person in people:
    salaire  = float(person["income"].replace("$", "").strip())
    if salaire > 2000 : 
        riche = riche +1

print(riche)
```

5. Nombre de personnes qui aiment les Drama :

```py
aime_drama = 0
for person in people : 
    if "Drama" in person["pref_movie"]:
        aime_drama = aime_drama +1
print(aime_drama)
```

6. Nombre de femmes qui aiment la science-fiction :

```py
femme_sf = 0
for person in people: 
    if 'Sci-Fi' in person["pref_movie"] : 
        if person["gender"] == "Female" :
            femme_sf = femme_sf+1

print(femme_sf)
```

7. Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$

```py
riche_docu =0
for person in people:
    salaire  = float(person["income"].replace("$", "").strip())
    if salaire > 1482: 
        if "Documentary" in person["pref_movie"]:
            riche_docu = riche_docu + 1


print(riche_docu)
```

8. Liste des noms, prénoms, id et revenus des personnes qui gagnent plus de 4000$

```py
list_par_salaire =0
for person in people:
    salaire  = float(person["income"].replace("$", "").strip())
    if salaire > 4000: 
        print(person["id"], person["first_name"], person["last_name"] )
```

9. Homme le plus riche (nom et id) :

```py

max = 0
riche_man = 0
for person in hommes2:               
    if person["gender"] == "Male": 
        salaire  = float(person["income"].replace("$", "").strip())
        if salaire > max : 
            max = salaire
            riche_man = person

print(riche_man["id"], riche_man["first_name"], riche_man["last_name"])
```

9. Salaire moyen :

```py
total_salaire = 0

for person in people:
    salaire = float(person["income"].replace("$", "").strip())
    total_salaire += salaire

moyenne_salaire = total_salaire / len(people)
print(moyenne_salaire)
```