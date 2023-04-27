# Créé par Morphée, le 15/12/2022 en Python 3.7
def syracuse(nombre):
    cpt=0
    liste=[]
    while cpt<10:
        if nombre%2==0:
            nombre=nombre//2
            liste.append(nombre)
            cpt=cpt+1
        else:
            nombre=nombre*3+1
            liste.append(nombre)
            cpt=cpt+1
    return liste


def tempsdevol(liste):
    liste_tdv=[]
    i=0
    while liste[i]>1:
        liste_tdv.append(liste[i])
        i=i+1
    return liste_tdv, i
