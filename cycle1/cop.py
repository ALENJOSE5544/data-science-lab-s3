def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1
print(is_coprime(4, 7))
print(is_coprime(17, 21))
print(is_coprime(5, 9))
print(is_coprime(25, 45))