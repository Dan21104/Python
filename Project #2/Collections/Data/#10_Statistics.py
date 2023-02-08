file = open("../text/volby.csv", encoding="utf-8")

data = file.read()
file.close()

rows = data.split("\n")

names = []
counts = []

header = rows[0]
columns = header.split(";")

for column in columns[1:]:
    names.append(column.strip('"'))
    counts.append(0)

for row in rows[1:]:
    columns = row.split(";")
    district = columns[0].strip('"')
    for index in range(1, len(columns)):
        count = int(columns[index])
        counts[index - 1] += count

for index in range(0, len(names)):
    print(names[index] + "\t" + str(counts[index]))

file = open("../text/vysledek.csv", "w", encoding="utf-8")
for index in range(0, len(names)):
    print(names[index] + "\t" + str(counts[index]))
    file.write('"' + names[index] + '";' + str(counts[index]))
