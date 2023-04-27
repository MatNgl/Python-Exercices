# Créé par Morphée, le 15/12/2022 en Python 3.7

def occurence_lettre(phrase, lettre):

    cpt=0
    for i in range(0,len(phrase)):
        if phrase[i]==lettre:
            cpt=cpt+1
    return cpt

def occurence_phrase(phrase):
    occ=dict()
    for i in range(0,len(phrase)):
        cpt=occurence_lettre(phrase,phrase[i])
        occ[phrase[i]]=cpt
    return occ
