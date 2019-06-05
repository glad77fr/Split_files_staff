toto = r'c:\toto\mini.csv'

toto = toto[:-4]
mot = ""

for val in toto[::-1]:
    if val != "\\":
        mot = mot + str(val)
    else:
        break

print(mot[::-1])