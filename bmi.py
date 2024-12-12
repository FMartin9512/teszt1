def szamol(Suly,Magassag):
    meter = Magassag/100
    bmi = Suly / pow(meter,2)
    return bmi

def beker():
    suly = float(input("Add meg a testsúlyod(kg): "))
    magassag = float(input("Add meg a magasságod(cm): "))
    ertek = szamol(suly,magassag)
    return ertek

def kiir():
    eredmeny = beker()
    if eredmeny < 18.5:
        print("Alultáplált")
    elif eredmeny >= 18.5 and eredmeny <= 24.9:
        print("Normál testsúly")
    elif eredmeny >= 25 and eredmeny <= 29.9:
        print("Túlsúlyos")
    else:
        print("Elhízott")
    print(eredmeny)

kiir()