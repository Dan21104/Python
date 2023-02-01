name = input("Enter your name: ")
print("Your name is: " + name + ".")
try:
    birth = int(input("Enter year of birth: "))
except:
    print("\033[49;31mAccess denied! Insert eligible year of your birth.\033[m")
    print("End of programme.")
    exit()
age = (2022 - birth)
print("You are " + str(age) + " years old.")
if age < 0:
    print("\033[49;31mAccess denied! Insert eligible year of your birth.\033[m")
    print("End of programme.")
    exit()
elif age <= 14:
    print("You belong to category: CHILD.")
    category = "child"
elif age <= 17:
    print("You belong to category: JUNIOR.")
    category = "junior"
elif age <= 26:
    print("You belong to category: STUDENT.")
    category = "student"
elif age <= 65:
    print("You belong to category: ADULT.")
    category = "adult"
elif age <= 125:
    print("You belong to category: SENIOR.")
    category = "senior"
elif age >= 125:
    print("\033[49;31mAccess denied! Insert eligible year of your birth.\033[m")
    print("End of programme.")
    exit()
print("Choose travel type: ")
print("     - bus")
print("     - train")
print("     - plane")
travel = input()
if travel == "bus":
    if category == "child":
        print("You can travel for free.")
    if category == "junior":
        print("The ticket is 5 $.")
    if category == "student":
        print("The ticket is 7 $.")
    if category == "adult":
        print("The ticket is 10 $.")
    if category == "senior":
        print("The ticket is 7 $.")
    print("Have a good ride.")
elif travel == "train":
    if category == "child":
        print("You can travel for free.")
    if category == "junior":
        print("The ticket is 12 $,")
    if category == "student":
        print("The ticket is 15 $.")
    if category == "adult":
        print("The ticket is 25 $.")
    if category == "senior":
        print("The ticket is 15 $.")
    print("Have a good ride.")
elif travel == "plane":
    if category == "child":
        print("You can travel for free.")
    if category == "junior":
        print("The ticket is 25 $.")
    if category == "student":
        print("The ticket is 35 $.")
    if category == "adult":
        print("The ticket is 50 $.")
    if category == "senior":
        print("The ticket is 35 $.")
    print("Have a good flight.")
else:
    print("\033[49;31mAccess denied! Insert eligible travel type.\033[m")
    print("End of programme.")
    exit()
print("End of programme.")
