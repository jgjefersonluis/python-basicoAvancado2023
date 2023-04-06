def fibonacci(max):
    sequencia = []
    x,y = 0,1
    while len(sequencia) < max:
        sequencia.append(y)
        x,y = y, x+y
    return sequencia

for x in fibonacci(100000):
    print(x)
    