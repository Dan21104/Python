while True:
    try:
        num1 = float(input("Insert value for number\033[49;36m x\033[m: "))
        break
    except ValueError:
        print("\033[49;31mAccess denied! Insert eligible number value for x.\033[m")
        continue
text = str(num1)
while True:
    while True:
        print("\033[49;36mChoose operation:\033[m")
        print("     +   for summing,")
        print("     -   for subtracting,")
        print("     *   for multiplying,")
        print("     **  for exponentiation,")
        print("     /   for dividing,")
        print("     //  for integer dividing,")
        print("     %   for dividing with a remainder,")
        print("     */  for root extraction,")
        print("     =   for end of process.")
        op = input()
        if op == "+" or op == "-" or op == "*" or op == "**" or op == "/" or op == "//" or op == "%" or op == "*/":
            break
        elif op == "=" or op == " =":
            res = num1
            print(str(num1) + "=" + str(res))
            print("End of programme.")
            break
        else:
            print("\033[49;31mAccess denied! Insert eligible operation.\033[m")
            continue
    if op == "=" or op == " =":
        exit()
    while True:
        try:
            num2 = float(input("Insert value for number\033[49;36m y\033[m: "))
            break
        except ValueError:
            print("\033[49;31mAccess denied! Insert eligible number value for y.\033[m")
            continue
    if op == "+" or op == " +":
        res = num1 + num2
    elif op == "-" or op == " -":
        res = num1 - num2
    elif op == "*" or op == " *":
        res = num1 * num2
    elif op == "**" or op == " **":
        res = num1 ** num2
    elif op == "/" or op == " /":
        res = num1 / num2
    elif op == "//" or op == " //":
        res = num1 // num2
    elif op == "%" or op == " %":
        res = num1 % num2
    elif op == "*/" or op == " */":
        res = num1 ** (1 / num2)
    text = "(" + text + op + str(num2) + ")"
    print(text + "=" + str(res))
    num1 = res
