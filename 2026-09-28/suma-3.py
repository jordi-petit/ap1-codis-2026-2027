# programa que escriu la mitaja dels enters en una seqüència (no buida).
# s'utilitza scan per llegir mentre quedin elements.

from yogi import scan

s = 0
n = 0
x = scan(int)
while x is not None:
    s = s + x
    n = n + 1
    x = scan(int)
print(s / n)
