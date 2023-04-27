# Créé par Morphée, le 15/12/2022 en Python 3.7
def palindrome(mot):
    reponse= True
    i=0
    j=len(mot)-1
    while i<=len(mot)//2 and reponse == True:
        if mot[i]==mot[j]:
            i=i+1
            j=j-1
        else:
            reponse=False
    return reponse