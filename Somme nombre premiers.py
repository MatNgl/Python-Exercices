# Créé par Morphée, le 14/12/2022 en Python 3.7

def testons(nbre):
    test = True
    if nbre==1:
        test= False
    k=2
    while k<nbre:
        if nbre%k==0 and test== True:
            test = False
        k=k+1
    return test


liste=[]

def liste_premiers(nbr):
    k=1
    liste=[]
    while k<nbr:
        if testons(k)== True:
            liste.append(k)
        k=k+1
    return liste

def decomposition(nbr):





