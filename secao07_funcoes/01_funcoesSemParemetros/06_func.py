def operacao():
    contador = 59
    if contador < 60:
        contador += 2
        return contador
    print(f'Contador = {contador}')
    return contador

print(operacao())
