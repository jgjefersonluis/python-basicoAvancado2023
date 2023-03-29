nome = ['Bianca', 'Vitor', 'Ariel', 'José']
idade = (18, 82, 71, 9, 12)
cidade = {'São Paulo', 'Vitória', 'São Luís'}
estado = {1:'RS', 2:'PR', 3:'ES', 4:'AM'}

print(list(zip(nome, idade, cidade, estado.values())))

#Exemplo 3 de zip
lugares = [('RS', 'São Paulo'), ('PR', 'Vitória'), ('AM', 'São Luís')]

#*lugares -> ('RS', 'São Paulo') ; ('PR', 'Vitória') ; ('AM', 'São Luís')
#zip ->  RS, PR, AM

print(list(zip(*lugares)))
