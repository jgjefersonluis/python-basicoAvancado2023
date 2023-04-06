def funcao_geradora():
    auxiliar = 0
    while auxiliar < 5:
        auxiliar += 1
        palavra = input('Fale: ')
        yield palavra

resultado = funcao_geradora()
print(resultado)

for item in resultado:
    print(item)

#Observação:
print(set(resultado)) #Podemos manipular geradores e transforma-los no que quisermos(set,list,tuple,dict)
