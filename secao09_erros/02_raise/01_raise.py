def cadastrar(login,senha):
    if type(login) is not str: #Não utilizei == pois estou fazendo uma comparação de tipos, não de valores
        raise TypeError('Login deve ser string')
    if type(senha) is not int:
        raise TypeError('Senha deve ser inteiro')
    print(f'Login:{login} e Senha{senha}')

cadastrar('123','123')
