from yogi import tokens, read


def trobar_iesim(i: int) -> int | None:
    actual = read(int)
    valor = None
    pos = 1
    while actual != -1:
        if pos == i:
            valor = actual
        pos += 1
        actual = read(int)
    return valor


def main() -> None:
    for i in tokens(int):
        valor = trobar_iesim(i)
        if valor is None:
            print("no hi és")
        else:
            print(valor)


if __name__ == "__main__":
    main()
