trueend= False
def functionalblock():
    endblock = False
    a = int(input("zadaj prvé číslo... "))
    b = int(input("zadaj druhé číslo... "))
    startA = a
    startB = b
    oldtest = int(-1)
    while endblock == False:
        if a > b:
            test = a%b
            if test <= 0:
                c = a/b
                if c!=0:
                    oldtest = int(b)
                    endblock = True
                    break
                else:
                    endblock=True
                    break
            oldtest = test
            a = b
            b = test
        elif b>a:
            test = b%a
            if test <= 0:
                c = b/a
                if c!=0:
                    oldtest = int(a)
                    endblock = True
                    break
                else:
                    endblock=True
                    break
            oldtest=test
            b = a
            a = test
    if oldtest == 1 or oldtest == -1:
        
        print(f"\nčísla {startA} a {startB} sú nesúdelitelné")
    else:
        print(f"\nNajväčší Spoločný Delitel čísel {startA} a {startB} je číslo {oldtest}")
functionalblock()
while trueend == False:
    ask = str(input("\n\nchceš pokračovať? [y/n]... "))
    ask.lower()
    if ask == "y":
        functionalblock()
    elif ask == "n":
        trueend = True
    elif ask != "y" or ask != "n":
        functionalblock()
