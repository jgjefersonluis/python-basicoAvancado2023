listaAnimais = ['Cachorro', 'Avestruz', 'Alce', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Abelhas',
'Carneiro', 'Cabra', 'Cobra', 'Coelho', 'Mosquito', 'Peixe', 'Macaco', 'Aranha']

GenAnimais = (animal for animal in listaAnimais if (animal[0] == 'C'or animal[0] == 'A') and len(animal) > 5)

print(GenAnimais)
for animal in GenAnimais:
    print(animal, end = '')


