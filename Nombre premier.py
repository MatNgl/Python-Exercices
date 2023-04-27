# Créé par Morphée, le 13/09/2022 en Python 3.7
def diviseur(n):  #retourne la liste des diviseurs d'un nombre
    L = []
    for i in range(1,n+1):
        if(n%i ==0):
            L.append(i)

    return L


n = int(input("Nombre ?"))

if(diviseur(n) == [1,n]):
    print("premier")
else:
    print("pas premier")


def premier(n): #fonction qui annonce si le nombre est premier ou non
    if (diviseur(n) == [1,n]):
        resultat = "Le nombre saisi est premier"
    else:
        resultat = "Le nombre saisi n'est pas premier"

    return resultat