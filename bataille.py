# Créé par Morphée, le 10/12/2022 en Python 3.7
from random import *

# Fonction melange #

def melange():
        paquet = [1,2,3,4,5,6,7,8,9,10]
        k=0
        while k<49:
            i= randint(0,9)
            j=randint (0,9)
            temp = paquet[i]
            paquet[i] = paquet[j]
            paquet[j] = temp
            k = k+1
        return paquet

# Fonction distribution #

def distribution():
    paquet = melange()
    paquetA= []
    paquetB= []
    paquetA_paquetB=[]

    for i in range (len(paquet)):
        if i%2 == 0:
            paquetA.append(paquet[i])

        else:
            paquetB.append(paquet[i])

    paquetA_paquetB.append(paquetA)
    paquetA_paquetB.append(paquetB)
    return paquetA_paquetB





#Algorithme de la Bataille#

def bataille(paquetA_paquetB):

    paquetA = paquetA_paquetB[0]
    paquetB = paquetA_paquetB[1]
    cptA = 0
    cptB = 0

    for i in range(len(paquetA)):
        if paquetA[i] > paquetB[i]:
            print("Pli", i+1, ":", paquetA[i],">",paquetB[i], "donc A gagne 1 point")
            cptA = cptA+1
        else:
            print("Pli", i+1, ":", paquetA[i],"<",paquetB[i], "donc B gagne 1 point")
            cptB = cptB+1
    print("Score : A :", cptA, "et B :", cptB)









