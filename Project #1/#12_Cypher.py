while True:

    print("\033[49;36mChoose operation:\033[m\n   E for encrypting,\n   D for decrypting.")
    operation = input("\033[49;36mInsert operation: \033[m")
    if operation == "D" or operation == "d" or operation == "E" or operation == "e":
        break
    else:
        print("\033[49;31mError! Insert eligible operation type.\033[m")
        continue

message = input("Enter secret message: ")

while True:

    try:
        key = int(input("Enter key: "))
        if 0 < key < 26:
            break
        else:
            print("\033[49;31mAccess denied! Insert eligible number! (1 - 25)\033[m")
            continue
    except ValueError:
        print("\033[49;31mError! Not a number.\033[m")
        continue

i = 0

while i < len(message):

    letter = message[i]
    code = ord(letter)

    if operation == "E" or operation == "e":
        code_2 = code + key
        if 64 < code < 91:
            if 65 < code_2 < 91:
                word = chr(code_2)
            elif 90 < code_2 < 116:
                word = chr(code_2 - 26)
        elif 96 < code < 123:
            if 97 < code_2 < 123:
                word = chr(code_2)
            elif 122 < code_2 < 148:
                word = chr(code_2 - 26)
        else:
            word = chr(code)
        print(word, end="")

    elif operation == "D" or operation == "d":
        code_2 = code - key
        if 64 < code < 91:
            if 64 < code_2 < 91:
                word = chr(code_2)
            elif 39 < code_2 < 65:
                word = chr(code_2 + 26)
        elif 96 < code < 123:
            if 96 < code_2 < 123:
                word = chr(code_2)
            elif 71 < code_2 < 97:
                word = chr(code_2 + 26)
        else:
            word = chr(code)
        print(word, end="")

    i += 1
