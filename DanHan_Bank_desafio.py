menu = """

============== DANHAN BANK ==============
|    Selecione a operação desejada:     |
|                                       |
|           [D] - Depositar             |
|           [S] - Sacar                 |
|           [E] - Extrato               |
|           [Q] - Sair                  |
|                                       |
=========================================
=> """

saldo = 0
limite = 500
extrato = ''

numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.lower() == 'd':
        print("\nVocê selecionou a opção \"Depósito!\"")
        print('Depósito')
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao.lower() == 's':
        print("\nVocê selecionou a opção \"Saque!\"")
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')

        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao.lower() == 'e':
        opcao_e = 'EXTRATO'
        print(opcao_e.center(25, '='))
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('=========================')


    elif opcao.lower() == 'q':
        print("\nObrigado por ser nosso cliente! DanHanBank agradece.\n\n")
        break

    else:
        print('\nOperação inválida, por favor, selecione novamente a operação desejada.')
