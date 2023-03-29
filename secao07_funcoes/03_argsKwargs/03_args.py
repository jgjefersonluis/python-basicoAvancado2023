notas = [8, 9.7, 2.3, 5, 10, 0, 0, 2, 6.9]

def somarNotas(*args):
    print(args)
    print(sum(args))

#somarNotas(notas) #TypeError
somarNotas(*notas)
#somarNotas()
