names = []
heights = []

while True:
    command = input("> ")
    if command == "a":
        name = input("name: ")
        height = int(input("height: "))
        if height > 0:
            names.append(name)
            heights.append(height)
    if command == "d":
        while True:
            try:
                name = input("name: ")
                index = names.index(name)
                names.pop(index)
                heights.pop(index)
                break
            except ValueError:
                print("Name not found.")
                continue
    if command == "f":
        ...
    if command == "l":
        for i in range(0, len(names)):
            print(names[i] + " " + str(heights[i]) + " cm")
    if command == "avg":
        total = 0
        for height in heights:
            total += height
        average = round(total / len(heights), 1)
        print("Average is: " + str(average) + " cm")
    if command == "var":
        total = 0
        for height in heights:
            total += height
        average = (total / len(heights))
        for height in heights:
            total += (height - average) ** 2
        variance = round(total / (len(heights) - 1), 1)
        print("Var is: " + str(variance) + " cm")
    if command == "min":
        name = names[0]
        minimum = heights[0]
        for i in range(0, len(names)):
            if heights[i] < minimum:
                name = names[i]
                minimum = heights[i]
        print(name + " " + str(minimum) + " cm")
    if command == "max":
        name = names[0]
        maximum = heights[0]
        for i in range(0, len(names)):
            if heights[i] > maximum:
                name = names[i]
                maximum = heights[i]
        print(str(maximum) + " cm")
    if command == "q":
        break
    if command == "?":
        print("a = add new student")
        print("d = delete student")
        print("l = list students")
        print("q = quit program")
