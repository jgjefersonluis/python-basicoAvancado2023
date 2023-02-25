print('----------Bem vindo a um  novo universo!----------')
print('--------------Crie o seu personagem.--------------')
corDoCabelo = input('Digite a cor do cabelo: ')
corDaPele = input('Digite a cor da pele: ')
classe = input('Escolha e digite a sua classe: Guerreiro\n'
               'Mago\n'
               'Feiticeiro\n'
               'Bruxo\n'
               'Arqueiro\n'
               'Elfo\n '
               'Ladrão\n'
               'Anão\n')
idadeDoPersonagem = int(input('Digite a idade do seu personagem: '))
alturaDoPersonagem = float(input('Digite a altura do seu personagem: '))
habilidadeEspecifica = input('Digite sua habilidade: ')
print('\n')
print('**************** Personagem Criado ****************')
print(f'Seu personagem tem as seguintes caracteristicas: \n'
      f'Cabelo de cor: {corDoCabelo}\n'
      f'Pele da cor: {corDaPele}\n'
      f'A classe escolhida foi: {classe}\n'
      f'Sua idade é de: {idadeDoPersonagem} anos.\n'
      f'Altura do personagem é de : {alturaDoPersonagem} metros.\n'
      f'Habilidade : {habilidadeEspecifica}')
