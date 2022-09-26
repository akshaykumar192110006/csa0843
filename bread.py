f=int(input("ENTER THE NUMBER OF FRESH LOAVES PURCHASED----> "))
o=int(input("ENTER THE NUMBER OF DAY OLD LOAVES PURCHASED----> "))
if(f<0):
    print("NEGATIVE VALUE")
    exit()
else:
    reg=185
    print("REGULAR PRICE---> ",reg)
    nl=185*f
    ol=(185*0.6)*o
    tot=nl+ol
    print("AMOUNT OF NEW LOAVES---> ",nl)
    print("AMOUNT OF DAY OLD LOAVES---> ",ol)
    print("TOTAL AMOUNT---> ",tot)
