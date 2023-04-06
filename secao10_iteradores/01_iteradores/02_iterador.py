lista = [1, 'oi', True]  # Listas são iteráveis

seg_iterador = iter(lista)
iteradorfinal = iter(seg_iterador)  # Comprovando que ao aplicar iter() em um iterador ele se mantem iterador

print(iteradorfinal)  # Retorna uma lista iteradora
for item in seg_iterador:  # O loop continua a funcionar pois ao aplicar o método iter() em um iterador, ele se mantem
    # iterador
    print(item)

