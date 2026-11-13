import random
import time


def ordena_seleccio(L: list[int]) -> None:
    """Ordena L en ordre creixent. Temps: O(n^2)."""

    n = len(L)
    for i in range(n - 1):
        m = pos_minim(L, i)
        L[i], L[m] = L[m], L[i]


def pos_minim(L: list[int], i: int) -> int:
    "Retorna min(L[i:])"

    m = i
    n = len(L)
    for j in range(i + 1, n):
        if L[j] < L[m]:
            m = j
    return m


if __name__ == "__main__":
    for n in range(1000, 10000, 1000):
        A = [random.randint(0, n) for _ in range(n)]
        t1 = time.time()
        ordena_seleccio(A)
        t2 = time.time()
        print(n, t2 - t1)
