try:
    x = float(input("Insert value of number x: "))
except:
    print("Access denied! Insert eligible number.")
    print("End of programme.")
    exit()
try:
    y = float(input("Insert value of number y: "))
except:
    print("Access denied! Insert eligible number.")
    print("End of programme.")
    exit()
if x > y:
    print(str(x) + " is bigger than " + str(y))
elif x < y:
    print(str(y) + " is bigger than " + str(x))
else:
    print(str(x) + " is same as " + str(y))
print("End of programme.")
