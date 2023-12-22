def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else: # a < b
        return gcd(a, b - a)


m = int(input())
n = int(input())
print(gcd(m, n))