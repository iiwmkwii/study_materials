def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


m = int(input())
n = int(input())
print(gcd(m, n))