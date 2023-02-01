file = open("../text/babicka.txt", encoding="utf-8")

data = file.read()

words = data.split(" ")
print("words: " + str(len(words)))

parts = data.split("\n")
print("parts: " + str(len(parts)))

file.close()
