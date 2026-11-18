import random
import time


def ordenacio_fusio(L: list[int]) -> None:
    """
    Ordena una llista d'enters en ordre creixent utilitzant l'algoritme d'ordenació per fusió.
    Temps: O(n log n) on n = |L|.
    """

    ordenacio_fusio_rec(L, 0, len(L) - 1)


def ordenacio_fusio_rec(L: list[int], e: int, d: int) -> None:
    """
    Ordena els elements de L[e:d+1].
    """

    n = d - e + 1
    if n > 1:
        m = (e + d) // 2 + 1
        ordenacio_fusio_rec(L, e, m - 1)
        ordenacio_fusio_rec(L, m, d)
        fusio(L, e, m, d)


def fusio(L: list[int], e: int, m: int, d: int) -> None:
    """
    Prec: L[e:m] ordenada i L[m:d+1] ordenada
    Post: L[e:d+1] ordenada
    """

    R: list[int] = [] # llista auxiliar on desar la fusió
    i = e
    j = m
    while i < m and j <= d:
        if L[i] < L[j]:
            R.append(L[i])
            i += 1
        else:
            R.append(L[j])
            j += 1
    R.extend(L[i:m])
    R.extend(L[j : d + 1])
    L[e : d + 1] = R


if __name__ == "__main__":
    n = 2_000_000
    A = [random.randint(0, n) for _ in range(n)]
    t1 = time.time()
    ordenacio_fusio(A)
    t2 = time.time()
    print(t2 - t1)
    for i in range(1, n):
        if A[i] < A[i - 1]:
            print("kaka")
