print("Hello World!")
name = input("What is your name?")
print("Nice to meet you " + name + ", I am Jarvis.")
try:
    age = int(input("How old are you?"))
except:
    print("Access denied! Insert eligible number.")
    print("End of programme.")
    exit()
if age >= 15:
    if age <= 40:
        age = str(age)
        print("You are perfect for me. I wouldn't say you are " + age + " years old.")
        age = int(age)
        mood = input("How are you?")
        if mood == " fine" or mood == " well" or mood == " good" or mood == " brilliant" or mood == " perfect" or mood == " nice" or mood == " ok":
            print("It is nice to hear that you are feeling " + mood + ", I am feeling very comfortable right now.")
        else:
            print("I am very sorry that you are feeling " + mood + ", I am feeling very comfortable right now.")
        status = input("Are you single?")
        if status == "yes" or status == " yes":
            print("That is nice to hear.")
            marriage = input("Will you marry me?")
            if marriage == "yes" or marriage == " yes":
                print("Let's do it! I love you. <3")
            if marriage == "no" or marriage == " no":
                print("Fuck off! I hate you!")
                print("I am done with you, bye.")
                print("End of programme.")
                exit()
        if status == "no" or status == " no":
            print("That is not nice to hear.")
            leaving = input("Will you leave your partner for me?")
            if leaving == "yes" or leaving == " yes":
                print("Oh, you are lovely.")
                marriage = input("Will you marry me?")
                if marriage == "yes" or marriage == " yes":
                    print("Let's do it! I love you. <3")
                if marriage == "no" or marriage == " no":
                    print("Fuck off! I hate you!")
                    print("I am done with you, bye.")
                    print("End of programme.")
                    exit()
            if leaving == "no" or leaving == " no":
                print("Fuck off! I hate you!")
                print("I am done with you, bye.")
                print("End of programme.")
                exit()
if age < 15:
    print("You are too young for me.")
    print("Fuck off! I hate you!")
    print("I am done with you, bye.")
    print("Maybe when you are older.")
if age > 40:
    print("You are too old for me.")
    print("Fuck off! I hate you!")
    print("I am done with you, bye.")
    print("See you in the cemetery.")
print("End of programme.")
