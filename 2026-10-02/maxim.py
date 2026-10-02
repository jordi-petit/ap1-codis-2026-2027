# programa que calcula la màxim d'una seqüència (no buida) d'elements reals

from yogi import tokens, read

m = read(float)
for x in tokens(float):
    if x > m:
        m = x
print(m)
