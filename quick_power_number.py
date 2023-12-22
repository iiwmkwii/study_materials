def pow(a:float, n:int):
    if n == 0:
        return 1
    elif n % 2 == 1: # n - нечетн
        return pow(a, n - 1) * a
    else: # n - четн
        return pow(a ** 2, n // 2)