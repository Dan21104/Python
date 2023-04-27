operations = 1
price = 0

print("Vítejte v zoologické zahradě! \n")

while True:

    print("Stiskněte \033[49;36mD\033[m pro výběr denní vstupenky,"
          " nebo \033[49;36mR\033[m pro výběr roční vstupenky.")
    ticket_duration = input("> ")
    if ticket_duration == "D" or ticket_duration == "R":
        break
    else:
        print("Vyberte platnou vstupenku.")
        continue

while True:

    try:
        print("Pro kolik osob si přejete zakoupit vstupenky?")
        tickets_count = int(input("> "))
        if tickets_count < 1:
            print("Vyberte platný počet vstupenek (více než 0).")
            continue
        else:
            break
    except ValueError:
        print("Vyberte platný počet vstupenek.")
        continue

while operations < tickets_count + 1:

    while True:

        try:
            print("Zadejte věk " + str(operations) + ". osoby.")
            age = int(input("> "))
            if age < 3 or age > 101:
                print("Zadejte platný věk. (více než 2 a méně než 101).")
                continue
            else:
                if ticket_duration == "D":
                    if 2 < age < 16:
                        print(str(operations) + ". OSOBA\n" + "Vstupenka: Denní\nKategorie: Dítě\nCena: 200 Kč")
                        price += 200
                    elif 15 < age < 65:
                        print(str(operations) + ". OSOBA\n" + "Vstupenka: Denní\nKategorie: Dospělý\nCena: 300 Kč")
                        price += 300
                    elif 64 < age < 101:
                        print(str(operations) + ". OSOBA\n" + "Vstupenka: Denní\nKategorie: Důchodce\nCena: 150 Kč")
                        price += 150
                elif ticket_duration == "R":
                    if 2 < age < 16:
                        print(str(operations) + ". OSOBA\n" + "Vstupenka: Roční\nKategorie: Dítě\nCena: 900 Kč")
                        price += 900
                    elif 15 < age < 65:
                        print(str(operations) + ". OSOBA\n" + "Vstupenka: Roční\nKategorie: Dospělý\nCena: 1800 Kč")
                        price += 1800
                    elif 64 < age < 101:
                        print(str(operations) + ". OSOBA\n" + "Vstupenka: Roční\nKategorie: Důchodce\nCena: 600 Kč")
                        price += 600
                operations += 1
                break
        except ValueError:
            print("Zadejte platný věk.")
            continue

print("\nCelková cena je: " + str(price) + " Kč.")
print("Děkujeme za vaši návštěvu!")
