def khalil(nombres):
    resultat = 0
    for chiffre in nombres:
        resultat = resultat + chiffre
    return resultat


nombres = [10000000000, 10000000000]
print(khalil(nombres))


def meriem(nombres):
    resultat = 0
    for chiffre in nombres:
        resultat = chiffre - resultat
    return resultat


nombres = [30000000000, 40000000000]
print(meriem(nombres))


print("hello, world! we are children too funny khalil and meriem, they are our calcul")



