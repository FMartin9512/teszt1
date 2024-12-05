def halmazAllapot():
    Homerseklet = int(input("Adj meg egy celsius értéket!"))
    if Homerseklet <= 0:
        eredmeny = print("Ezen az értéken szilárd halmazállapotú! ")
    elif Homerseklet > 0 and Homerseklet < 100:
        eredmeny = print("Ezen az értéken folyékony halmazállapotú! ")
    else:
        eredmeny = print("Ezen az értéken légnemű! ")
    return eredmeny


halmazAllapot()
