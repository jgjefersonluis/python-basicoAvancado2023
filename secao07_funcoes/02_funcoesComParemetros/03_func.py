# Exemplo 3
def separar(lista):
    for num in lista:
        if num > 10:
            print(num, end=' ')

listaCriada = [21, 3, 213, 543, 54, 65, 12, 0, 21, 24, 432.121, 532]
separar(listaCriada)

# Nomear argumentos
def cidade(parte1, parte2):
    print(parte1 + ' ' + parte2)

cidade('São', 'Paulo')
cidade('Paulo', 'São')

cidade(parte1='São', parte2='Paulo')
cidade(parte2='Paulo', parte1='São')




