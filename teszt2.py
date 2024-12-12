import random


def veletlen():
    Rszamok = []
    for _ in range(20):
        Rszamok.append(random.randrange(1,51))
    return Rszamok

def kiir():
    for item in veletlen():
        print(item, end=" ")

def osszead():
    osszeg = 0
    for item in veletlen():
        osszeg += item
    return osszeg



veletlen()
kiir()
print()
print(f"A lista elemei összesen {osszead()}")