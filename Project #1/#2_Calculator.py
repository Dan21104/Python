try:
    x = float(input("Insert value for number\033[49;36m x\033[m: "))
except ValueError:
    print("\033[49;31mAccess denied! Insert eligible number value for x.\033[m")
    print("\033[49;31mEnd of programme.\033[m")
    exit()
try:
    y = float(input("Insert value for number\033[49;36m y\033[m: "))
except ValueError:
    print("\033[49;31mAccess denied! Insert eligible number value for y.\033[m")
    print("\033[49;31mEnd of programme.\033[m")
    exit()
print("\033[49;36mChoose operation:\033[m")
print("     +   for summing,")
print("     -   for subtracting,")
print("     *   for multiplying,")
print("     **  for exponentiation,")
print("     /   for dividing,")
print("     //  for integer dividing,")
print("     %   for dividing with a remainder,")
print("     */  for root extraction.")
operation = input("\033[49;36mInsert operation: \033[m")
if operation == "+" or operation == " +":
    print("\033[49;32mResult is: \033[m" + str(x + y))
elif operation == "-" or operation == " -":
    print("\033[49;32mResult is: \033[m" + str(x - y))
elif operation == "*" or operation == " *":
    print("\033[49;32mResult is: \033[m" + str(x * y))
elif operation == "**" or operation == " **":
    print("\033[49;32mResult is: \033[m" + str(x ** y))
elif operation == "/" or operation == " /":
    print("\033[49;32mResult is: \033[ m" + str(x / y))
elif operation == "//" or operation == " //":
    ("\033[49;32mResult is: \033[m" + str(x // y))
elif operation == "%" or operation == " %":
    print("\033[49;32mResult is: \033[m" + str(x % y))
elif operation == "*/" or operation == " */":
    print("\033[49;32mResult is: \033[m" + str(x ** (1 / y)))
else:
    print("\033[49;31mAccess denied! Insert eligible operation type from selection.\033[m")
print("\033[49;31mEnd of programme.\033[m")
