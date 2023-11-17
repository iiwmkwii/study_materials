def sieve_eratosthenes():
    """ Сито Эратосфена,
    функция получает на вход натрульное число N
    выводит все числа от 0 до N с указанием простое
    или составное"""
    n = int(input())
    a = [True] * n
    a[0] = a[1] = False
    for k in range(2, n):
        if a[k]:
            for m in range(2 * k, n, k):
                a[m] = False
    for k in range(n):
        print(k, '-', 'простое' if a[k] else 'составное')


sieve_eratosthenes()
