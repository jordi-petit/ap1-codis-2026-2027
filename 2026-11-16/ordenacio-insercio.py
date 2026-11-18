def ordenacio_insercio(L: list[int]) -> None:
    """
    Ordena una llista d'enters en ordre creixent utilitzant l'algoritme d'ordenació per inserció.
    Temps: sigui n = |L|,
        O(n^2) en el cas pitjor,
        O(n^2) en mitjana,
        O(n) en el cas millor.
    """

    n = len(L)
    for i in range(1, n):
        insereix_ordenadament(L, i)


def insereix_ordenadament(L: list[int], i: int) -> None:
    """
    Prec: L[:i] està ordenada creixentment
    Post: L[:i+1] està ordenada creixentment
    """

    x = L[i]
    j = i - 1
    while j >= 0 and L[j] > x:
        L[j + 1] = L[j]
        j -= 1
    L[j + 1] = x


if __name__ == "__main__":
    A = [5, 2, 4, 2, 3, 1, 7]
    print(A)
    ordenacio_insercio(A)
    print(A)
