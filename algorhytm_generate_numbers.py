def generate_number(N: int, M: int, prefix=None):
    """Генерирует все числа (с лидирующими незначащами нулями
       в N-ричной системе счисления (N <= 10)
       длины M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M - 1, prefix)
        prefix.pop()


def gen_bin(M, prefix=""):
    """ Только для двоичной системы"""
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M - 1, prefix + digit)


generate_number(4, 3)
gen_bin(5)
