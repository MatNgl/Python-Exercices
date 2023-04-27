# Créé par Morphée, le 08/12/2022 en Python 3.7
liste = [8,38,41,37,0,45,17,33,23]

def Min (liste):

    nbr = liste[0]
    for i in liste:
        if i < nbr:
            nbr = i

    return nbr


def Max():


    nbr = liste[0]
    for i in liste:
        if i > nbr:
            nbr = i

    return nbr


def Somme():
    somme=0

    for i in liste:
        somme= i+somme
    return somme

def SommePairs():
    somme=0

    for i in liste:
        if i%2==0:
            somme = somme+i

    return somme

def SommeImpairs():
    somme=0

    for i in liste:
        if i%2==1:
            somme = somme+i

    return somme


def listage (liste):

    listecomplete=[]
    listecomplete.append('Min :' + str(Min()))
    listecomplete.append('Max :' + str(Max()))
    listecomplete.append('Somme :' + str(Somme()))
    listecomplete.append('Somme pairs :' + str(SommePairs()))
    listecomplete.append('Somme impairs :'+ str(SommeImpairs()))

    return listecomplete


