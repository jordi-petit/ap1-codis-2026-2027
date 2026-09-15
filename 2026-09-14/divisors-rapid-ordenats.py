# programa que mostra tots els divisors d'un nombre n >= 1
# de manera més ràpida que el programa divisors-lent.py
# i en ordre creixent.
# idea clau: buscar els divisor fins a √n i després mostrar els divisors en ordre invers.

import yogi

# precondició: n >= 1
n = yogi.read(int)

i = 1
while i * i < n:  # divisors estrictament menors que √n
    if n % i == 0:  # i és un divisor de n
        print(i)
    i = i + 1

if i * i == n:  # si n és un quadrat perfecte, √n és un divisor
    print(i)

i = i - 1
while i >= 1:
    if n % i == 0:  # i és un divisor de n (i, per tant, n//i també és un divisor de n)
        print(n // i)
    i = i - 1
