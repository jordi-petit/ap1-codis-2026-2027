from turtle import forward, done, right


def quadrat(mida: float) -> None:
    """dibuixa un quadrat de mida donada"""

    for _ in range(4):
        forward(mida)
        right(90)


def quadrats_rotats(mida: int, quants: int) -> None:
    """..."""
    for _ in range(quants):
        quadrat(mida)
        right(360 / quants)


def main() -> None:
    quadrats_rotats(100, 12)
    done()


if __name__ == "__main__":
    main()
