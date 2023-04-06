nome = 'Programando Ideias' #Strings são iteráveis como já vimos
lista = [1,'oi',True] #Listas são iteráveis

prim_iterador = iter(nome) #Transformação de iterável para iterador
seg_iterador = iter(lista)
print(prim_iterador) #Retorna uma string iteradora
print(seg_iterador) #Retorna uma lista iteradora
print(type(prim_iterador))


print(next(prim_iterador)) #retorna um dado, 'P'
print(next(prim_iterador)) #retorna um dado, 'r'
print(next(prim_iterador)) #retorna um dado, 'o'
print(next(prim_iterador)) #retorna um dado, 'g'
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador))
print(next(prim_iterador)) #Acusa StopIteration pois voce já obteve todos os dados desmembrados da sequencia
