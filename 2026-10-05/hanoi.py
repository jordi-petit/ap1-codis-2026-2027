from yogi import read


def hanoi(n: int, ori: str, dst: str, aux: str) -> None:
    """
    Acció que escriu com moure n discos de les torres de Hanoi
    d'un piu d'orígen (ori) a un piu de destí (dst) utilitzant
    un piu auxiliar (aux). Prec: n >= 0.
    """
    if n > 0:
        hanoi(n - 1, ori, aux, dst)
        print(ori, "->", dst)
        hanoi(n - 1, aux, dst, ori)


def main() -> None:
    n = read(int)
    hanoi(n, "A", "B", "C")


if __name__ == "__main__":
    main()
