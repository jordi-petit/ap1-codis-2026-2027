# programa que suma els enters en una seqüència.
# el nombre d'elements es dóna al principi.

from yogi import read

n = read(int)
s = 0
for i in range(n):
    x = read(int)
    s = s + x
print(s)
