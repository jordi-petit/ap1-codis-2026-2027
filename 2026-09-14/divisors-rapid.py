# programa que mostra tots els divisors d'un nombre n >= 1
# de manera més ràpida que el programa divisors-lent.py
# però sense ordre creixent.

# idea clau: dos divisors pel preu d'un! 
#            si i és un divisor de n, llavors n//i també és un divisor de n

import yogi

n = yogi.read(int)

i = 1
while i * i <= n:
    if n % i == 0:  # i és un divisor de n
        print(i)
        if i != n // i: # no mostrar el mateix divisor dues vegades per quadrats perfectes
            print(n // i)
    i = i + 1
