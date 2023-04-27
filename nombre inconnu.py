# Créé par Morphée, le 06/12/2022 en Python 3.7
from random import randint

nombre_mystere = randint(100,999)
print(nombre_mystere)
cpt = 0
nombre=0

while nombre!=nombre_mystere:
    cpt_nombre=0

    nombre=int(input('Saisir un nombre'))
    if (nombre//100)== (nombre_mystere//100):
        #print('Le nombre des centaines est bien placé')
        cpt_nombre=cpt_nombre+1
    if (nombre%100//10) == (nombre_mystere%100//10):
        #print('Le nombre des dizaines est bien placé')
        cpt_nombre=cpt_nombre+1
    if (nombre%10)==(nombre_mystere%10):
        #print('Le nombre des unités est bien placé')
        cpt_nombre=cpt_nombre+1

    print('Il y a', cpt_nombre, 'nombre(s) bien placé(s)')
    cpt=cpt+1

print ("Vous avez trouvé le nomnbre exact en", cpt,"essais !")






