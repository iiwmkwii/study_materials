def matryoshka(n):
    if n == 1:
        print('Матрёшечка')
    else:
        print('Верх матрешки n=', n)
        matryoshka(n-1)
        print('Низ матрешки n=', n)

a = int(input())
matryoshka(a)