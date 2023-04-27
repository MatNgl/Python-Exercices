#retourne le nombre d'espace dans une phrase
def mystere(phrase):

    c=0

    lng = len(phrase)
    for i in range (0, lng-1):
        if ord(phrase[i])==32:
            c=c+1
    return c;

# retourne une lettre en majuscule si elle est en minuscule
def majuscule (lettre):

    if 97<=ord(lettre)<=122:
        uniMaj = ord(lettre)-32
        lettre = chr(uniMaj)
    return lettre;

#affiche une phrase minuscule ne majuscule
nouvellePhrase =""
phrase = input('Saisir une phrase')
for lettre in phrase:
    nouvellePhrase = nouvellePhrase + majuscule((lettre))
print (nouvellePhrase)


#ne fonctionne pas
phrase = input('Saisir une phrase')
mot =""
for i in phrase :
    while ord(phrase[i] != 32):
        mot = mot + phrase[i]
    print (mot)


#ne fonctionne pas

mot=""
phrase = input('Saisir une phrase')
for i in phrase:
    if ord(phrase[i]) == 32:
        print(mot)
    else:
        mot = mot + phrase[i]
