# compta el nombre d'elements iguals al darrer

from yogi import tokens

# llegir tota la seqüència en una llista
elements: list[int] = []
for element in tokens(int):
    elements.append(element)

# recórrer la llista per comptar elements iguals al darrer
comptador = 0
for element in elements:
    if element == elements[-1]:
        comptador += 1

print(comptador)
