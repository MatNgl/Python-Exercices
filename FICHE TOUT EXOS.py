# Créé par Morphée, le 14/12/2022 en Python 3.7
from random import randint
def mystere(tab):
    c=0
    long=len(tab)
    for i in range(0,long-1):
        if tab[i]%2==0:
            c=c+1
    return c

def produit(tab):
    resultat=1
    for i in range(0,len(tab)):
        resultat = resultat*tab[i]
    return resultat

def creation_tab(n,t):
    tableau=[n]
    for i in range(0,t-1):
        n=n+3
        tableau.append(n)
    return tableau





def melange():
    paquet=[1,2,3,4,5,6,7,8,9,10]
    k=0
    while k<49:
        i=randint(0,9)
        j=randint(0,9)
        temp=paquet[i]
        paquet[i]=paquet[j]
        paquet[j]=temp
        k=k+1
    return paquet

def distribution(paquet):
    paquetA=[]
    paquetB=[]
    paquetA_paquetB=[]
    for i in range(0,len(paquet)):
        if i%2==0:
            paquetA.append(paquet[i])
        else:
            paquetB.append(paquet[i])

    paquetA_paquetB.append(paquetA)
    paquetA_paquetB.append(paquetB)
    return paquetA_paquetB


def bataille(paquet_melange):
    paquetA=paquet_melange[0]
    paquetB=paquet_melange[1]
    cptA=0
    cptB=0

    for i in range(0,len(paquetA)):
        if paquetA[i] > paquetB[i]:
            print('Pli',i,":",paquetA[i],'>',paquetB[i],'joueur A gagne un point')
            cptA=cptA+1
        else:
            cptB=cptB+1
            print('Pli',i,":",paquetA[i],'<',paquetB[i],'joueur B gagne un point')
    print('Le score est, A :', cptA,', B :', cptB)




