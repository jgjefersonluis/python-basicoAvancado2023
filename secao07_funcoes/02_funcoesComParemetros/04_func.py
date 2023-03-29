#Comando nonlocal (para funções dentro de funções)
def funFora():
    total = 0
    def funDentro():
        nonlocal total
        total = total + 1
        print(total)
    return funDentro()

funFora()
#funDentro() #NameError
