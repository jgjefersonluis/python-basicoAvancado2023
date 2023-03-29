# Parâmetro padrão

#Função que nao exige parâmetros
print()
input()

#Função que exige parâmetros
def soma(num1, num2):
    print(num1 + num2)

soma(10, 18)

#Função com parãmetro padrão (default)
def medida(numero, referencia=60):
    if numero > referencia:
        print(f'{numero} é maior que {referencia}')
    else:
        print(f'{numero} é menor que {referencia}')

medida(70)
medida(30)
medida(40, 30)
medida(30, 40)

#Obs.: O parâmetro padrão deve ser sempre o último entre os parâmetros de uma função.

def medida(numero=75, referencia=60):
    if numero > referencia:
        print(f'{numero} é maior que {referencia}')
    else:
        print(f'{numero} é menor que {referencia}')

medida()
medida(40, 30)
medida(70)
