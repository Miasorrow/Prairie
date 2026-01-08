import pandas as pd 
import numpy as np
import random
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
import random
from numpy import mean


# ashGen
import random
import pandas as pd


def generate(n):
    ash_keys = ['a', 'b', 'c', 'd', 'v', '1', '2', '3', 'ref']  # les colonnes de mon df
    df = pd.DataFrame(columns=ash_keys)  # créer le df

    for i in range(n):  # n fois
        bars = set()  # un set, c'est (presque) comme un tableau, mais sans doublon
        while len(bars) < 3:  # je crée les 3 barres.
            bars.add(random.randrange(1, 11))  # Comme c'est un set, il ne peut pas y avoir deux barres de la même
                                                            # taille,
            # je mets un while car je dois créer des barres jusqu'à ce que j'en aie 3

        bars = list(bars)  # je transforme en list c'est plus pratique qu'un set
        bonne_reponse = random.randrange(1, 4)  # choisir au hasard une barre
        ref = bars[bonne_reponse - 1]  # mettre la même taille à la ref

        choix_des_complices = random.randrange(1,
                                               4)  # pour les complices il ne faut pas qu'ils choisissent la bonne
                                                        # réponse !
        while bars[choix_des_complices - 1] == ref:  # donc, je choisi au hasard jusqu'à ce que ce soit faux
            choix_des_complices = random.randrange(1, 3)

        ligne = [
            choix_des_complices,  # a
            choix_des_complices,  # b
            choix_des_complices,  # c
            choix_des_complices,  # d,
            None,  # v
            bars[0],  # 1
            bars[1],  # 2
            bars[2],  # 3
            ref  # ref
        ]
        autre_df = pd.DataFrame([ligne], columns=ash_keys)

        df = pd.concat([df, autre_df])

    return df


if __name__ == "__main__":
    df = generate(1000)
    print(df)
"""
ref = 2
v = 0"""
"""def valeurV(): 
        if ref == 1:
            v = 1
        elif ref == 2:
            v = 2
        else:
            v = 3
        print(v)
valeurV()
"""
# main

# solver
def solve(line):
    if line['1'] == line['ref']: return 1
    if line['2'] == line['ref']: return 2
    return 3


def solveDf(df):
    df['v'] = df.apply(solve, axis=1)
    return df

df = generate(1)
result = solve(df.loc[0])

df = generate(10)

solved = solveDf(df)


"""df_train = generate(500)
df_train = solveDf(df_train)

inputs = df_train[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']]
output = df_train[['v']]"""



inputs = df[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']]
output = df[['v']]
arbre = tree.DecisionTreeClassifier()

arbre = arbre.fit(inputs, output)
tree.plot_tree(arbre)
compteur  =0
faux = 0
for i in range(100):
    dfTest = generate(1)
    print(dfTest)

    repArbre = arbre.predict(dfTest[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']])
    repSolver = solve(dfTest.loc[0])

    print(repArbre, repSolver)

    if repArbre == repSolver :
        compteur = compteur+1
    else : 
        faux = faux +1

print("vrai",compteur)
print("faux",faux)



#! version mieux 

df_train = generate(500)  # 500 pour l'entrainement
df_test = generate(50)   # 50 pour tester
df_test = df_test[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']] # pas besoin de v on le calculera au fur et a mesure

# resoudre (remplir v) pour les data d'entrainement
df_train = solveDf(df_train)

# séparer in et out
inputs = df_train[['a', 'b', 'c', 'd', '1', '2', '3', 'ref']]
output = df_train[['v']]

# créer l'arbre
arbre = tree.DecisionTreeClassifier()

# entrainer l'arbre
arbre = arbre.fit(inputs, output)

# ... pour voir l'arbre
# tree.plot_tree(arbre)
# plt.show()

# Test et stat
stat = []
# pour chaque ligne du df de test
for i in range(len(df_test)):
    # récupérer la ligne
    row = df_test.iloc[[i]]
    # faire la prédiction à partir de la ligne (sans v)
    prediction = arbre.predict(row)
    # faire la prédiction avec le solver
    solution = solve(row.loc[0])
    # stocker 0 (erreur de l'arbre) ou 1 (réussite de l'arbre)
    stat.append(int(prediction[0] == solution))

# affichage des résultats
print("moyenne: ", mean(stat))