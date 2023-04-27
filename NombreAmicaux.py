# Créé par Morphée, le 15/12/2022 en Python 3.7
from random import*

nombreA=220
nombreB=284
reponse= False
listeA=[]
listeB=[]
sommeA=0
sommeB=0
for i in range(1,nombreA):
    if nombreA%i==0:
        listeA.append(i)
        sommeA=sommeA+i

for i in range(1,nombreB):
    if nombreB%i==0:
        listeB.append(i)
        sommeB=sommeB+i
if sommeA == nombreB and sommeB == nombreA:
    reponse= True
    print(reponse)
else:
    print(reponse)


print(nombreA,listeA,sommeA)
print(nombreB,listeB,sommeB)


