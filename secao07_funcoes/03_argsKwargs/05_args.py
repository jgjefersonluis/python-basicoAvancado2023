def jogadas(nome, **kwargs):
    print(kwargs)
    for jogada in kwargs:
        print(kwargs[jogada])
        if kwargs[jogada] == 10:
            return f'{nome} ganhou!'
    return f'{nome} perdeu!'

#print(jogadas('Marcelo', j1=9, j2=8, j3=8, j4=9, j5=6))
print(jogadas('Marcelo', j1=9, j2=8, j3=10, j4=9, j5=6))
