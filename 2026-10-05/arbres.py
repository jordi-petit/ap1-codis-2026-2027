import yogi
import turtle


def arbre(n: int, a: float, α: float, b: int) -> None:
    """
    Pinta un arbre fractal amb n nivells, b branques, alçada a i angle α entre
    les seves branques externes. Deixa la tortuga al punt on ha començat.
    Prec: n>=0, a>=0, α>=0, b>0.
    """

    if n == 0:
        turtle.forward(a)
        turtle.backward(a)
    else:
        turtle.forward(a)
        turtle.left(α / 2)
        arbre(n - 1, a / 2, α, b)
        for _ in range(b - 1):
            turtle.right(α / (b - 1))
            arbre(n - 1, a / 2, α, b)
        turtle.left(α / 2)
        turtle.backward(a)


def main() -> None:
    n = yogi.read(int)
    a = yogi.read(float)
    α = yogi.read(float)
    b = yogi.read(int)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.left(90)  # deixa els arbres drets
    arbre(n, a, α, b)
    turtle.done()


if __name__ == "__main__":
    main()
