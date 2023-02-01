number = 1
a = 0
b = 0
z = 1

while True:
    try:
        num1 = int(input("Kolik máš známek? "))
    except ValueError:
        print("\033[49;31mChyba! Zadej platné číslo.\033[m")
        continue
    if num1 <= 0:
        print("\033[49;31mChyba! Zadej platné číslo.\033[m")
        continue
    else:
        break

while number <= num1:
    try:
        gr = int(input("Zadej " + str(number) + ". známku: "))
    except ValueError:
        print("\033[49;31mChyba! Zadej platné číslo.\033[m")
        continue
    if gr < 1 or gr > 5:
        print("\033[49;31mChyba! Zadej platné číslo.\033[m")
        continue

    while True:
        try:
            weight = int(input("Zadej váhu " + str(number) + ". známky: "))
        except ValueError:
            print("\033[49;31mChyba! Zadej platnou váhu.\033[m")
            continue
        if weight < 1 or weight > 5:
            print("\033[49;31mChyba! Zadej platné číslo.\033[m")
            continue
        else:
            break
    number += 1
    x = gr * weight
    a += x
    b += weight
print("Vážený průměr: " + str(round(a / b, 2)))
print("Známka na vysvědčení: " + str(round(a / b)))
while True:
    try:
        o = int(input("Zadej váhu příští známky: "))
        break
    except ValueError:
        print("\033[49;31mChyba! Zadej platné číslo.\033[m")
        continue
while z <= 5:
    a += o*z
    b += o
    print("Pro známku " + str(z) + " je výsledek " + str(round(a / b, 2)))
    z += 1
