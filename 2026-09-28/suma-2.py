# programa que suma els enters en una seqüència.
# un valor especial -1 marca el final de la seq.

from yogi import read

s = 0
x = read(int)
while x != -1:
    s = s + x
    x = read(int)
print(s)
