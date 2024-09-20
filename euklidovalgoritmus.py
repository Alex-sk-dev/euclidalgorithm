trueend= False
def functionalblock():
    endblock = False
    a = int(input("zadaj prvé číslo... "))
    b = int(input("zadaj druhé číslo... "))
    oldtest = int(-1)
    while endblock == False:
        if a > b:
            test = a%b
            if test <= 0:
                endblock = True
                break
            oldtest = test
            a = b
            b = test
        elif b>a:
            test = b%a
            if test <= 0:
                endblock = True
                break
            oldtest=test
            b = a
            a = test
    if oldtest == 1:
        print("tieto čísla sú nesúdelitelné")
    if oldtest == -1:
        print("tieto čísla sú nesúdelitelné")
    if oldtest != 1:
        print(oldtest)
    if oldtest != -1:
        print(oldtest)
functionalblock()
while trueend == False:
    ask = str(input("chceš pokračovať? [y/n]... "))
    ask.lower()
    if ask == "y":
        functionalblock()
    if ask == "n":
        trueend = True
    