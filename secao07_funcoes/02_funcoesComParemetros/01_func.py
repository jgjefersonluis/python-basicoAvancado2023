# Exemplos de funções com parâmetros

# Exemplo 1
def imparPar(numero):
    if numero % 2 == 0:
        print(f'{numero} é par')
        #return f'{numero} é par'
    else:
        print(f'{numero} é impar')
        #return f'{numero} é impar'

imparPar(10)
imparPar(27)

#imparPar() #TypeError

