# Créé par Morphée, le 15/09/2022 en Python 3.7
n = int(input("Choisir un nombre"))

if n > 1:
    for i in range(2, int(n/2)+1):
         if (n % i) == 0:
            print(n,"=", i, 'x', ": False")
            break
    else:
        print(n, ": True")


