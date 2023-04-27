# Créé par Morphée, le 15/12/2022 en Python 3.7
from random import*
#ALGORITHME SI UN NOMBRE EST PARFAIT#
nombre=randint(1,500)
liste=[]
somme=0
for i in range(1, nombre):
    if nombre%i==0:
        liste.append(i)
        somme= somme+i

if somme==nombre:
    print('Le nombre',nombre,'dont les diviseurs sont', liste,' est un nombre parfait')
else:
    print('Le nombre',nombre,'dont les diviseurs sont', liste,' n\'est pas un nombre parfait')


#ALGORITHME LA LISTE DES NOMBRE PARFAIT < 10 000#
liste_parfait=[]
for j in range(1,10000): # j = divisé
    liste=[]
    somme=0
    for i in range(1, j): # i = diviseur
        if j%i==0:
            liste.append(i)
            somme= somme+i
    if somme==j:
        liste_parfait.append(j)
print(liste_parfait)




