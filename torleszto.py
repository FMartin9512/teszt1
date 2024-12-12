def beker():
    p = float(input("Add meg a hitelösszeget(Ft): "))
    r = float(input("Add meg az éves kamatlábat(%): "))
    n = float(input("Add meg a futamidőt(hónapokban): "))
    eredmeny = szamol(p,r,n)
    return eredmeny

def szamol(P,R,N):
    kamatlab = R/100/12
    return (P * kamatlab * (1 + kamatlab)**N) / ((1 + kamatlab) ** N - 1)

def main():
    print(beker())

main()