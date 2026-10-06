import yogi
import turtle


def fractal_koch(n: int, a: float) -> None:
    """
    Pinta un fractal de Koch de n nivells i amplada a,
    començant a la posició i orientació actual de la tortuga.
    La tortuga queda "al final" del fractal.
    Prec: n>=1, a>=0.
    """

    if n == 1:
        turtle.forward(a)
    else:
        fractal_koch(n - 1, a / 3)
        turtle.left(60)
        fractal_koch(n - 1, a / 3)
        turtle.right(120)
        fractal_koch(n - 1, a / 3)
        turtle.left(60)
        fractal_koch(n - 1, a / 3)


def floc_koch(n: int, a: float, c: int) -> None:
    """
    Pinta un floc de Koch de n nivells, amplada a, i c costats,
    començant a la posició i orientació actual de la tortuga.
    La tortuga queda com havia començat.
    Prec: n>=1, a>=0, c>=0.
    """
    for _ in range(4):
        fractal_koch(n, a)
        turtle.right(90)


def main() -> None:
    n = yogi.read(int)
    a = yogi.read(float)
    c = yogi.read(int)
    turtle.hideturtle()
    turtle.speed(0)
    floc_koch(n, a, c)
    turtle.done()


if __name__ == "__main__":
    main()
