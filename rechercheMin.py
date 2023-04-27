# Créé par Morphée, le 15/12/2022 en Python 3.7
def rechecherMin(tab):
    min=tab[0]
    for i in range(1,len(tab)):
        if tab[i]<min:
            min = tab[i]
    return min


def separe(tab):
    i=0
    j=len(tab)-1
    while i<j:
        if tab[i] == 0:
            i=i+1
        else:
            tab[i], tab[j]= (0,1)
            j= j-1
    return tab