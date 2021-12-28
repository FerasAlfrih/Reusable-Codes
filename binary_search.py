import random


def binSearch(lista: list, y):
    lista = sorted(lista)
    print(lista)
    N = len(lista)
    if len(lista) > 1:
        n = random.randrange(0, N)
        x = lista[n]
        if x == y:
            return lista, print("Done")
        elif x < y:
            lista = lista[n:]
            binSearch(lista, y)
        elif x > y:
            lista = lista[0:x]
            binSearch(lista, y)

    else:
        x = lista[0]
        if x == y:
            return lista, print("Done")
        else:
            return print(f"{y} is not in lista")


lista = [5, 6, 7, 8, 9, 15, 16, 17, 0, 1, 2, 3, 4, 18, 19, 20, 10, 11, 12, 13, 14]
listaa = binSearch(lista, 0)
