# Créé par Morphée, le 15/12/2022 en Python 3.7
from random import*
tab=[randint(0,1) for i in range(10)]
liste=[]
cpt=1
for i in range(1,len(tab)):
    if tab[i]==tab[i-1]:
        cpt=cpt+1
    else:
        liste.append(cpt)
        cpt=1
liste.append(cpt)
print(tab, liste)










