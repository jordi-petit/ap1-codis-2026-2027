"""
Programa que llegeix una seqüència de paraules
i compta quants parells de paraules consecutives
repetides hi ha.
"""

from yogi import tokens, scan

repeticions = 0
primera = scan(str)
if primera is not None:
    for segona in tokens(str):
        if primera == segona:
            repeticions = repeticions + 1
        primera = segona
print(repeticions)
