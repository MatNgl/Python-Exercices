# Je remplis une tirelire de la manière suivante, je commence par déposer 1 € dans la tirelire (un lundi),puis j'y dépose 2,01 euros le  jour suivant (un mardi),
#puis 3,02 E le jour suivant (un mercredi),  puis 4,03 euros le jour suivant (un jeudi), etc. (chaque jour j y dépose 1,01 euros de plus que la veille).

#Par exemple :
#le huitième jour (un lundi), j y dépose 8,07 euros et le contenu total de la tirelire est:
#1 +2,01+3,02 +4,03+5,04 +6,05+7,06+8,07 = 36,28 euros.
#Lorsque le contenu total de la tirelire dépasse 1 500 euros, je casse cette tirelire.
#Le but du sujet est de déterminer le contenu de la tirelire lorsque je la casserai,
#ainsi que le jour de la semaine correspondant (lundi, mardi, mercredi, jeudi, vendredi, samedi ou dimanche).


def depot(n):
        base = 1
        for i in range (1,n):
            base = base +1.01
            rounded_num = round(base,2)
        return base



s=0
for n in range (1,7):
    s = s+ depot(n)
    m  = s/7
print(m)


def contenu(n):
    somme=0
    for i in range (1,n):
        somme = somme + depot(n)
    return somme



