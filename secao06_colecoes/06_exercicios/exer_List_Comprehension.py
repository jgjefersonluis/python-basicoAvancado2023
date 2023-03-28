animais = ['Cachorro', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Carneiro', 'Cabra', 'Cobra', 'Coelho',
'Mosquito', 'Peixe', 'Macaco']

listaAnimais = [animal for animal in animais if animal[0] ==  'C' and len(animal) <= 7]

#O comprehension executa o seguinte: para cada animal na lista 'animais', se o nome do animal
# tiver até 7 letras e a primeira letra for 'C', então armazene este animal na lista 'listaAnimais'

print(listaAnimais)

