from time import sleep
end = False
a = int(input("zadaj prvé číslo... "))
b = int(input("zadaj druhé číslo... "))
oldtest = int(-1)
while end == False:
    if a > b:
        test = a%b
        if test <= 0:
            end = True
            break
        oldtest = test
        a = b
        b = test
    elif b>a:
        test = b%a
        if test <= 0:
            end = True
            break
        oldtest=test
        b = a
        a = test
print(f"{oldtest}")
sleep(1000)