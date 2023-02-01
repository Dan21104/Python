maximum = 0

file = open("text/Advent_Day1.txt")
content = file.read()
lines = content.splitlines()

total = 0

for line in lines:
    if line != "":
        number = int(line)
        total += number
    if line == "":
        total = 0
    if total > maximum:
        maximum = total

lines.sort(reverse=True)
print(lines)
