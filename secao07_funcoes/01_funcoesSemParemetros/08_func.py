def celsius_kelvin():
    celsius = int(input('Digite o valor em Celsius: '))
    kelvin = celsius + 273
    print(f'{kelvin}')
    sair =input('Deseja sair? ')
    if sair == 's' or 'sim':
        return 'Acabou'
    else:
        return celsius_kelvin() #Retornando para ela mesma, lembrando de usar os parenteses.

print(celsius_kelvin())
