# programa que suma els enters en una seqüència.
# s'utilitza tokens per anar llegint tots els elements.

from yogi import tokens

s = 0
for x in tokens(int):
    s = s + x
print(s)
