file = open("text/babicka.txt", encoding="utf-8")

letters = {}

data = file.read()
for letter in data:
    if letter not in letters:
        letters[letter] = 0
    letters[letter] += 1

maximum = None
minimum = None
for letter in letters:
    count = letters[letter]
    if maximum is None or count > letters[maximum]:
        maximum = letter
    if minimum is None or count < letters[minimum]:
        minimum = letter

print("maximum is: " + maximum + " " + str((letters[maximum])))
print("minimum is: " + minimum + " " + str((letters[minimum])))
