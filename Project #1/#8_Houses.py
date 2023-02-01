
while True:
    try:
        houses = int(input("Enter number of houses: "))
        if houses <= 0:
            print("Access denied! Enter higher number.")
            continue
        else:
            break
    except ValueError:
        print("Access denied! Not a number!")
        continue

while True:
    try:
        stories = int(input("Enter number of stories: "))
        if stories <= 0:
            print("Access denied! Enter higher number.")
            continue
        else:
            break
    except ValueError:
        print("Access denied! Not a number!")
        continue

while True:
    try:
        windows = int(input("Enter number of windows: "))
        if windows <= 0:
            print("Access denied! Enter higher number.")
            continue
        else:
            break
    except ValueError:
        print("Access denied! Not a number!")
        continue

i = 0
j = windows // 2
k = windows // 2
m = 0
n = windows
o = 0
p = 0

if windows % 2 == 0:
    n -= 1
while m < houses:
    print((k + 1) * " " + (n + 2) * "=" + (k + 1) * " ", end=" ")
    m += 1
m = 0
print()
while i < (windows // 2 + 1):
    while m < houses:
        print(k * " " + "/" + " " + n * "u" + " \\" + k * " ", end=" ")
        m += 1
    k -= 1
    i += 1
    n += 2
    print()
    m = 0
while m < houses:
    print((windows * 2 + 3) * "=", end="")
    print(" ", end="")
    m += 1
print()
m = 0
while p < stories:
    m = 0
    while m < houses:
        print("|", end="")
        while o < windows:
            print(" #", end="")
            o += 1
        print(" | ", end="")
        o = 0
        m += 1
    p += 1
    print()
m = 0
while m < houses:
    print((windows * 2 + 3) * "=", end="")
    print(" ", end="")
    m += 1
