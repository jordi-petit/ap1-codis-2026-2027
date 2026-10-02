"""
Programa que, donada una seqüència de naturals, diu
si hi ha algun nombre primer.
"""

from yogi import tokens, scan


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


def main1() -> None:
    algun_primer = False
    numero = scan(int)
    while numero is not None and not algun_primer:
        if es_primer(numero):
            algun_primer = True
        numero = scan(int)
    if algun_primer:
        print("hi ha algun primer")
    else:
        print("no hi ha cap primer")


def main2() -> None:
    for numero in tokens(int):
        if es_primer(numero):
            print("hi ha algun primer")
            return
    print("no hi ha cap primer")


def hi_ha_algun_primer() -> bool:
    """Llegeix una seqüència i indica si té algun nombre primer. Deixa de llegir quan sap la resposta."""

    for numero in tokens(int):
        if es_primer(numero):
            return True
    return False


def main3() -> None:
    if hi_ha_algun_primer():
        print("hi ha algun primer")
    else:
        print("no hi ha cap primer")


if __name__ == "__main__":
    main1()  # o main2 o main3
