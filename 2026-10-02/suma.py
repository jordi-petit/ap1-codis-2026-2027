# programa que calcula la suma d'una seqüència d'elements reals

from yogi import tokens

s = 0.0
for x in tokens(float):
    s = s + x
print(s)
