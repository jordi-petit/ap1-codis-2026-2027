# programa que mostra tots els divisors d'un nombre n >= 1

import yogi

n = yogi.read(int)

i = 1
while i <= n:
    if n % i == 0:  # i és un divisor de n
        print(i)
    i = i + 1
