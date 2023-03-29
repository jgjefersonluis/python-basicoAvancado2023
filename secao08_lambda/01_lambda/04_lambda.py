def quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

segGrau = quadratica(1, 5, 8)
print(segGrau(3))
