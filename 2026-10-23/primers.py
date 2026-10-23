"""
Programa que calcula tots els primers fins a n
utilitzant el mètode de divisions i el mètode d'Eratòstenes.
"""

import time
import math


def és_primer(n: int) -> bool:
    """Indica si n és primer o no. Prec n>=0."""
    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True


def primers_fins_a_1(n: int) -> list[int]:
    """Retorna els primers que hi ha en [1..n]. Prec n>=0."""
    L: list[int] = []
    for i in range(2, n + 1):
        if és_primer(i):
            L.append(i)
    return L


def primers_fins_a(n: int) -> list[int]:
    """Retorna els primers que hi ha en [1..n]. Prec n>=1."""
    # usant l'algorismne d'Eratostenes

    L = [False] * (n + 1)
    L[0] = L[1] = False
    for i in range(2, int(math.sqrt(n + 1)) + 1):
        if not L[i]:
            # i és primer
            for j in range(2 * i, n + 1, i):
                L[j] = True
    return [i for i in range(len(L)) if not L[i]]


def main():
    n = 1_000_000
    start_time = time.time()
    c = len(primers_fins_a(n))
    end_time = time.time()
    print(c, end_time - start_time)


if __name__ == "__main__":
    main()
