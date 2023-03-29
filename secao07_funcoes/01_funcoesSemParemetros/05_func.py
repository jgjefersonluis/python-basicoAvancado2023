#Função com retorno
def operacao():
    contador = 60 #Isso é uma variavel local ou global?? Local
    contador += 2
    print(f'Contador = {contador}')
    return contador

print(operacao()) #Agora o valor retornado foi de 62
