import yogi


def maxim2(a: int, b: int) -> int:
    """Retorna el màxim de dos nombres."""

    if a >= b:
        return a
    else:
        return b


def minim2(a: int, b: int) -> int:
    """Retorna el mínim de dos nombres."""

    if a <= b:
        return a
    else:
        return b


def maxim3(a: int, b: int, c: int) -> int:
    """Retorna el màxim de dos nombres"""

    return maxim2(a, maxim2(b, c))


def factorial(n: int) -> int:
    """
    Retorna el factorial d'un número.
    És a dir, retorna n! = n * (n-1) * (n-2) * ... 1
    Fixeu-vos que 0! = 1.

    Precondició: n >= 0
    """

    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f


def es_primer(n: int) -> bool:
    """Retorna True si n és primer, False altrament. Prec: n >= 0"""

    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def mcd(a: int, b: int) -> int:
    """
    Retorna el màxim comú divisor de a i b.
    Precondició: a >= 0 i b >= 0 i no a == b == 0
    """

    if a == 0 or b == 0:
        return a + b
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def max_i_min(a: int, b: int) -> tuple[int, int]:
    """Retorna el màxim i el mínim de dos nombres."""

    if a >= b:
        return a, b
    else:
        return b, a


def sumar_un_segon(h: int, m: int, s: int) -> tuple[int, int, int]:
    """
    Retorna la hora, minut i segon després d'incrementar un segon.
    Precondició: 0 <= h < 24, 0 <= m < 60, 0 <= s < 60.
    """

    s = s + 1
    if s == 60:
        s = 0
        m = m + 1
        if m == 60:
            m = 0
            h = h + 1
            if h == 24:
                h = 0
    return h, m, s


# exemples

h, m, s = 23, 59, 59
h_despres, m_despres, s_despres = sumar_un_segon(h, m, s)
print(h_despres, m_despres, s_despres)
print(h, m, s)
