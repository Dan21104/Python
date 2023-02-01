try:
    a = int(input("Insert value for number a:"))
except:
    print("Access denied! Insert eligible number value for a.")
    print("End of programme.")
    exit()
try:
    x = int(input("Insert value for first interval coordinate x:"))
except:
    print("Access denied! Insert eligible number value for first interval coordinate x.")
    print("End of programme.")
    exit()
try:
    y = int(input("Insert value for second interval coordinate y:"))
except:
    print("Access denied! Insert eligible number value for second interval coordinate y.")
    print("End of programme.")
    exit()
z = y + 1
if a in range(x, z):
    a = str(a)
    x = str(x)
    y = str(y)
    z = str(z)
    print("Number " + a + " is in interval (x, y).")
else:
    a = str(a)
    x = str(x)
    y = str(y)
    z = str(z)
    print("Number " + a + " is not in interval (x, y).")
print("End of programme.")
