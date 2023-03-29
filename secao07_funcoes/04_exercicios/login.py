login = False
cadastroFeito = False
op = 0
username = ' '
senha = ' '

def intro():
    global op
    global cadastroFeito
    global login
    while op != 5:
        print('1 - Cadastro\n2 - Login\n3 - Mudar senha\n4 - Logout\n5 - Sair')
        op = int(input('______Opção: '))

        if op == 1:
            if not cadastroFeito: #Se não exitir nenhum cadastro anteriror
                cadastro()
            else: #Caso já foi feito um cadastro antes:
                print('__________Cadastro já feito anteriormente_________')

        elif op == 2:
            if cadastroFeito:
                loginSistema()
            else:
                print('__________Faça o cadastro antes de fazer login__________')

        elif op == 3:
            if cadastroFeito:
                mudarSenha()
            else:
                print('__________Faça o cadastro antes de alterar a senha_________')

        elif op == 4:
            if login:
                logout()
            else:
                print('__________Para dar logout primeiro tem que fazer login né')

        elif op == 5:
            return 0

def cadastro():
    global username
    global senha
    global cadastroFeito
    username = input('__________Digite seu nome de usuário: ')
    senha = input('__________Digite sua senha: ')
    cadastroFeito = True
    return intro() #Chama a função intro() de novo

def loginSistema():
    global username
    global senha
    global login
    if not login:
        testeUsuario = input('__________Username: ')
        testeSenha = input('__________Senha: ')

        if testeUsuario == username and testeSenha == senha: #Teste se usuario e senha
    # estão corretos
            login = True

    if login:
        print('_________Você está logado!__________')
    else:
        print('__________Username ou senha incorretos__________')

    return intro()

def mudarSenha():
    global login
    global senha
    if login:
        testeSenha = input('__________Senha atual: ')
        if testeSenha == senha:
            senha = input('__________Digite sua nova senha: ')
        else:
            print('__________Senha atual incorreta__________')
    else:
        print('___________Faça login antes__________')

    return intro()

def logout():
    global login
    login = False
    print('__________Deslogado!__________')
    return intro()

intro() #Chama a função intro() pela primeira vez, iniciando o sistema.