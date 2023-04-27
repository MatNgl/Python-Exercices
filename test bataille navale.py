# Créé par Morphée, le 04/10/2022 en Python 3.7
def Mystere():
    tab=24
    for i in range (1,5):

        j = input(int('veuillez saisir l\'emplacement du bateau n°', i))
        while tab[j] == 0:

        j = input(int('L\'emplacement est déjà pris, en saisir un autre'))