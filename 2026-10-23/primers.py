"""
Programa que calcula el nombre de primers menors que un nombre n
utilitzant el mètode de divisions i el mètode d'Eratòstenes.
"""


import time


def és_primer(n: int) -> bool:
    if n <= 1:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
    return True


def main():
    n = 10_000_000
    start_time = time.time()
    L: list[int] = []
    for i in range(2, n):
        if és_primer(i):
            L.append(i)
    print(len(L))
    end_time = time.time()
    print(end_time - start_time)


if __name__ == "__main__":
    main()