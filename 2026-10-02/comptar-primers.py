"""
Programa que, donada una seqüència de naturals, compta
quants nombres primers hi ha.
"""

from yogi import tokens


def es_primer(n: int) -> bool:
    """
    Indica si n és primer. Prec: n >= 0.
    """
    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True


def main() -> None:
    primers = 0
    for numero in tokens(int):
        if es_primer(numero):
            primers = primers + 1
    print(primers)


if __name__ == "__main__":
    main()
