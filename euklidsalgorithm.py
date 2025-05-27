trueend= False
def functionalblock():
    endblock = False
    a = int(input("input first (1st) numner\n"))
    b = int(input("\ninput second (2nd) number\n "))
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
        
        print(f"\nnumbers {startA} and {startB} don't have a common divider")
    else:
        print(f"\nLargest common divider of the numbers {startA} and {startB} is the number {oldtest}")
functionalblock()
while trueend == False:
    ask = str(input("\n\ncontinue? [y/n]\n"))
    ask.lower()
    if ask == "y":
        functionalblock()
    elif ask == "n":
        trueend = True
    elif ask != "y" or ask != "n":
        functionalblock()
