# Créé par Morphée, le 14/12/2022 en Python 3.7
def hamming(mot1, mot2):

    mot1 = mot1.upper()
    mot2 = mot2.upper()
    nbr_commun=0
    for i in range(0, len(mot1)):
        if mot1[i] != mot2[i]:
            nbr_commun= nbr_commun+1
    return nbr_commun


def recherche(elt, tab):
    occ= -1
    for i in range(0,len(tab)):
        if elt == tab[i]:
            occ = i
    return occ


alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
mot = input('Saisir un mot')
chaine=''
somme= 0
for i in range(0, len(mot)):
    for j in range(0, len(alphabet)):
        if mot[i] == alphabet[j]:
            chaine = chaine + str(j+1)
            somme = somme + j+1
print(somme)
print(chaine)

if int(chaine)%somme != 0:
    print("Le mot",mot,"n'est pas parfait !")
else:
    print("Le mot", mot, "est parfait !")




