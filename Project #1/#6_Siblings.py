try:
    age = int(input("Kolik ti je let? "))
except ValueError:
    print("Zadej platné číslo.")
    exit()
sibling = input("Máš nějakého sourozence? ")
if sibling == "NE" or sibling == "Ne" or sibling == "ne":
    print("Takže jsi jedináček. ")
    exit()
elif sibling == "ANO" or sibling == "Ano" or sibling == "ano":
    try:
        sage = int(input("Kolik je mu let? "))
    except ValueError:
        print("Zadej platné číslo.")
        exit()
else:
    print("Napiš správnou hodnotu. Buď ANO nebo NE.")
    exit()
if sage > age:
    X = (sage - age)
    if X == 1:
        print("Takže je o " + str(X) + " rok starší než ty.")
    if X > 1:
        if X < 5:
            print("Takže je o " + str(X) + " roky starší než ty.")
        else:
            print("Takže je o " + str(X) + " let starší než ty.")
elif sage < age:
    X = (age - sage)
    if X == 1:
        print("Takže je o " + str(X) + " rok mladší než ty.")
    if X > 1:
        if X < 5:
            print("Takže je o " + str(X) + " roky mladší než ty.")
        else:
            print("Takže je o " + str(X) + " let mladší než ty.")
else:
    print("Takže jste stejně staří - nejste náhodou dvojčata?")
