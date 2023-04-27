# Créé par Morphée, le 13/12/2022 en Python 3.7
## calculs ##

#Fonction mystère# Renvoie le nombre de nombre pairs de la liste

def mystere(tab):
    c=0
    long=len(tab)
    for i in range (0, long-1):
        if tab[i]%2==0:
            c=c+1
    return c

#Fonction produit# Fait le produit des nombres de la liste
def produit(tab):
    produit=1
    for i in range (0,len(tab)):
        produit= tab[i]*produit
    return produit

#Fonction création de tableau#
# Crée un tableau n= première valeur / t= longueur tableau
def creation_tableau(n,t):
    cpt=0
    tableau=[n]
    while cpt!=t-1:
        n=n+3
        tableau.append(n)
        cpt=cpt+1
    return tableau


n = int(input("Saisir un nombre de départ"))
t = int(input("Saisir la longueur du tableau"))
tab= creation_tableau(n,t)
print(tab)
print("Les valeurs choisies sont n=",n," et t=",t,"le tableau obtenu est",tab,"et le produit de ses valeurs vaut", produit(tab))

