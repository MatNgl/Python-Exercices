# Créé par Morphée, le 09/09/2022 en Python 3.7

def diviseur(t):
    a=1
    om=[]
    while a<=t:
        if t%a==0:
            om.append(a)
        a=a+1
    return om