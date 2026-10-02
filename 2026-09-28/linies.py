from typing import Optional


def escriure_fila(car: str, cops: int) -> None:
    for i in range(cops):
        print(car, end="")
    print()


def escriure_rectangle(car: str, files: int, columnes: int) -> None:
    for i in range(files):
        escriure_fila(car, columnes)


def main() -> None:
    f = 3
    c = 5
    car = "*"
    escriure_rectangle(car, f, c)


def f(x: int) -> Optional[int]:
    if x == 1:
        return 55
    if x == 2:
        return 66


if __name__ == "__main__":
    main()
