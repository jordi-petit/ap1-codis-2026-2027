# programa que suma els enters en una seqüència.
# s'utilitza scan per llegir mentre quedin elements.

from yogi import scan

s = 0
x = scan(int)
while x != None:
    s = s + x
    x = scan(int)
print(s)
