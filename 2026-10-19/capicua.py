# funció per saber si una llista és cap i cua


def capicua(L: list[int]) -> bool:
    n = len(L)
    for i in range(n // 2):
        if L[i] != L[-i - 1]:
            return False
    return True


def capicua2(L: list[int]) -> bool:
    return L == list(reversed(L))
