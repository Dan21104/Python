print("Zadejte první číslo:")
cis1 = int(input())
text = str(cis1)

while True:
    print("Zadejte zanménko:")
    zn = input()
    print("Zadejte druhé číslo:")
    cis2 = int(input())
    if zn == "+":
        vys = cis1 + cis2
    elif zn == "-":
        vys = cis1 - cis2
    elif zn == "*":
        vys = cis1 * cis2
    elif zn == "/":
        vys = cis1 / cis2

    text = f'({text}){zn} {cis2} '
    print(f'{text} = {vys}')
    cis1 = vys