def factorial(n: int) -> int:
    """
    Donat un enter n >= 0, retorna n!
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
