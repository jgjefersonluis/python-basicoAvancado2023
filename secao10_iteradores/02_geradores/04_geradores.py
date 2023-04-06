def fibonacci(max):
    x,y,contador = 0,1,0
    while contador < max:
        x,y = y, x+y
        yield x
        contador = contador + 1

for x in fibonacci(100000):
    print(x)
    