total = 0

while True:
    entry = input("Insert value for number\033[49;36m x\033[m: ")
    if entry == "":
        break
    number = int(entry)
    total += number

print("Sum is: " + str(total))
