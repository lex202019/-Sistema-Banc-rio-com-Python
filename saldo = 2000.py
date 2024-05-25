menu = '''
[d]  Depositar
[s]  Sacar
[e]  Extrato
[q]  Sair
>'''

saldo = 0
limite = 500
extrato = ""
total_saque = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("digite o valor que queira depositar >"))

        if valor > 0:
            saldo += valor

        else:
            print("operação falhou! o valor informado é invalido")


    elif opcao == 's':
        valor = float(input("digete o valor que vai sacar >"))

        excedeu_saldo =  valor > saldo  
           
        excedeu_limite =  valor > limite 

        excedeu_saques =  limite_saques <=  total_saque  

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")


        elif excedeu_limite:
            print("Operação falhou! O valo do saque excede o limite")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor :.2f}\n"
            total_saque += 1

        else:
            print("Operação invalida! o valor informado é invalidor")
           
    elif opcao == 'e':
        print('\n================ EXTRATO ================')
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('===========================================')
    
    elif opcao == 'q':
        break

    else:
        print("Operação invalida! o valor informado é invalidor")