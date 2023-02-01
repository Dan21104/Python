names = []
grades = []
counter = 0

print("Insert (?) for help")

while True:
    command = input("> ")
    if command == "a":
        name = input("name: ")
        if name in names:
            name = name + str(counter + 1)
            counter += 1
        while True:
            try:
                grade = int(input("grade: "))
            except ValueError:
                print("Insert eligible number.")
                continue
            if 0 < grade < 6:
                names.append(name)
                grades.append(grade)
                break
            else:
                print("Insert number in interval (1 - 5).")
                continue
    if command == "d":
        while True:
            name = input("name: ")
            if name in names:
                def order(item, names, n=0):
                    if not names:
                        return None
                    elif names[0] == item:
                        return n
                    else:
                        return order(item, names[1:], n + 1)
                x = order(name, names)
                names.remove(name)
                grades.remove(x)
                break
            else:
                print("Name was not found.")
                continue
    if command == "l":
        print(names)
        print(grades)
    if command == "e":
        print("End of programme.")
        exit()
    if command == "?":
        print("a = add new student")
        print("d = delete student")
        print("l = list students")
        print("e = exit programme")
