x = 24
y = 32

def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(x, y))