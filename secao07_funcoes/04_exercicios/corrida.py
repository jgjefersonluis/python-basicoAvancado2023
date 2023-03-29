def classParcial(primeiro, segundo, terceiro, **outros):
    op = input('Houve trapaça? s/n: ')
    quarto = ''
    quinto = ''
    ultimo = ''
    if op == 'n':
        for posicao, corredor in outros.items():
            if posicao == '4':
                quarto = corredor
            elif posicao == '5':
                quinto = corredor
            elif posicao == '6':
                ultimo = corredor

        classFinal(primeiro, segundo, terceiro, quarto, quinto, ultimo)
    elif op == 's':
        colocacao = [primeiro, segundo, terceiro]
        colocacao.extend(outros.values()) #Adiciona à lista os valores do dicionário

        babaca = input('Quem trapaceou? : ')
        vitima = input('Quem foi prejudicado? : ')

        posBabaca = colocacao.index(babaca) #Retorna os indices dos corredores na lista 'colocacao'
        posVitima = colocacao.index(vitima)

        colocacao[posBabaca] = vitima
        colocacao[posVitima] = babaca

        classFinal(*colocacao) #Desempacota a lista para ser enviada à função 'classFinal'

    else:
        print('Digite uma opção válida!')


def classFinal(primeiro, segundo, terceiro, quarto, quinto, ultimo):
    print('Classificação Final: ')
    print(f'Primeiro: {primeiro}')
    print(f'Segundo: {segundo}')
    print(f'Terceiro: {terceiro}')
    print(f'Quarto: {quarto}')
    print(f'Quinto: {quinto}')
    print(f'Último: {ultimo}')

print('Corredores: ')
print('Mercúrio (MC), Papa-Léguas (PL), Sonic (SN), Flash (FS), Ligeirinho (LG) e Super Homem (SH)')

pri = input('Vencedor: ')
seg = input('Segundo: ')
ter = input('Terceiro: ')
qua = input('Quarto: ')
qui = input('Quinto: ')
ult = input('Ultimo: ')

outros = {'4':qua, '5':qui, '6':ult} #Gera um dicionário com os 3 ultimos dados informados

classParcial(pri, seg, ter, **outros)
