# Créé par Morphée, le 09/09/2022 en Python 3.7
n=int(input('Choisir un nombre'))
L=[]

for i in range (1, n+1):
    if n%i==0:
        L.append(i)
print (L)

