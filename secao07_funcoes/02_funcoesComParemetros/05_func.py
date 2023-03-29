# Variáveis locais e globais para funções
# Comando global
nome = 'arroz'

def comida():
    global nome
    nome = nome + ' e miojo'
    print(nome)

comida()
