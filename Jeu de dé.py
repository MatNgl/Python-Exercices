# Créé par Morphée, le 22/11/2022 en Python 3.7
from random import*
#Algorithme 1

def mystere():
    liste=[0,0,0,0,0]
    for i in range(5):
        liste[i]=randint(1,6)
    return liste



#Algorithme 2

def minimum(partie):
    min=6
    for i in partie:
        if i<min:
            min = i
    return min


#Algorithme 3

def nbre_6(partie):
    cpt=0
    for i in partie:
        if i ==6:
            cpt=cpt+1
    return cpt


#Algorithme 4

cpt = 0
partie=[]
while nbre_6(partie)<2:
    partie = mystere()


    cpt=cpt+1

if cpt > 5:
    print( "Le joueur a perdu", minimum(partie), "€.", "Il a joué", cpt,"partie(s)")
else :
    print ('Le joueur a gagné 10€.', "Il a joué", cpt,"partie(s)")






