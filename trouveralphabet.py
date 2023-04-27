# Créé par Morphée, le 08/12/2022 en Python 3.7



def trouveLettre(lettre):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    rang =0
    for i in range(0,len(alphabet)):
        if lettre == alphabet[i]:
            rang = i+1
    return rang