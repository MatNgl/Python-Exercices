# Créé par Morphée, le 13/09/2022 en Python 3.7
age=int(input('Quel est votre âge ?'))



if age >= 18:
        vote= True
        conducteur = "pouvez conduire seul(e)"
else:
        vote = False
        if age>=16:
            conducteur = "pouvez conduire accompagné(e)"
        else:
            conducteur = "ne pouvez pas conduire"

print ("vous pouvez voter :", vote)
print ("vous", conducteur)


