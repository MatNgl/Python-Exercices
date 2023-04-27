# Créé par Morphée, le 06/12/2022 en Python 3.7

def gratification(moy):
    if moy >= 16:
        return "Félicitations"
    elif moy >= 14:
        return "Bien"
    else:
        return "Continuez vos efforts"


def listage (listeClasse):
    cpt=0
    nb_eleve = int(input('Combien d\'élèves dans la classe ?'))
    while cpt<nb_eleve:
        listeEleve=[]
        listeEleve.append(input('Saisir le nom'))
        listeEleve.append(input('Saisir le prénom'))
        listeEleve.append(gratification(float(input('Saisir le moyenne'))))
    #gratification = float(input('Saisir le moyenne'))
    #listeEleve.append(gratification)


        listeClasse.append(listeEleve)
        cpt=cpt+1

    return listeClasse




