def cerca_lineal_1(L: list[int], x: int) -> bool:
    """Diu si x es troba en L. Temps: O(n) on n = |L|."""

    for element in L:
        if element == x:
            return True
    return False


def cerca_lineal_2(L: list[int], x: int) -> bool:
    """Diu si x es troba en L. Temps: O(n) on n = |L|."""

    return x in L


def cerca_binaria_1(L: list[int], x: int) -> bool:
    """Diu si x es troba en L. Prec: L està ordenada. Temps: O(log n) on n = |L|."""

    n = len(L)
    e, d = 0, n - 1
    while e <= d:
        m = (e + d) // 2
        if L[m] < x:
            e = m + 1
        elif L[m] > x:
            d = m - 1
        else:
            return True
    return False


def cerca_binaria_2(L: list[int], x: int) -> bool:
    """Diu si x es troba en L. Prec: L està ordenada. Temps: O(log n) on n = |L|."""

    return cerca_binaria_rec(L, x, 0, len(L) - 1)


def cerca_binaria_rec(L: list[int], x: int, e: int, d: int) -> bool:
    """
    Diu si x es troba en L.
    Prec:
        - L està ordenada.
        - L[:e] < x
        - L[d+1:] > x
    """

    if e > d:
        return False
    m = (e + d) // 2
    if L[m] < x:
        return cerca_binaria_rec(L, x, m + 1, d)
    elif L[m] > x:
        return cerca_binaria_rec(L, x, e, m - 1)
    else:
        return True
