menu = '''
[d] deposito
[s] saque
[e] extrato
[sa] saldo
[q] sair

Escolha uma opção: '''


saldo = 0
extrato = ''
limite = 500
num_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Digite um valor: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor}\n'
            print('Depósito efetuado com sucesso!')
        else:
            print('Valor incorreto, tente novamente!')

    elif opcao == "s":
        valor = float(input('Informe o valor do saque:  '))
        
        if valor > saldo:
            print('Saldo insuficiente!')

        elif valor > limite:
            print('O valor ultrapassa o limite de R${limite:.2f}.\n')

        elif num_saque >= LIMITE_SAQUE:
            print("Numero maximo de saques atingidos!") 
        
        elif valor <= 0:
            print('Valor inválido. Operação Cancelada')
            
        else:
            saldo -= valor
            extrato += f'SAque: R${valor:.2f}\n'
            num_saque += 1
        
    elif opcao == "e":
        print("\n===Extrato===")
        print(extrato if extrato else "Nenhuma movimentação feita")
        
        print(saldo)
        print("===========\n")

    elif opcao == 'sa':
        print(f'Saldo: R${saldo:.2f}\n')

    elif opcao == "q":
        print("Sistema encerrado!")
        break
    
    else:
        print("Opção inválida!")
    
