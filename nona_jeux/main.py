# main.py
from partie import partie
from strategies import rand, plusGrande, plusPetite, smart

n_parties = 10_000
victoires_robot = 0
for i in range(n_parties):
    gagnant = partie(
        strategy_humain=smart,
        strategy_robot=smart)
    if gagnant.name == "Robot":
        victoires_robot += 1

print("% victoire robot: ", victoires_robot / n_parties)