# Sistema Bancario desafio dio.me 



valor = 0
saldo_inicial = 0
valor_limite_saque = 500
saldo_conta = saldo_inicial

saidas = []
entradas = []


# Validar
excedeu_saldo = 0
excedeu_limite = 0
excedeu_saques = 0
limite = 0
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao =  int(input("""
        ======= Sistema =======
            [1] - Depositar
            [2] - Sacar
            [3] - Extrato
            [4] - Sair do Sistema!       
        =======================

        :"""))

    # Depositar
    if opcao == 1:
        
        print("------Depositar-----")
        valor = int(input("Valor do Deposito: "))
        if valor > 0:
            saldo_conta += valor
            entradas.append(valor)
            print()
            print(f'Saldo: R$ {saldo_conta},00')




    # Sacar
    elif opcao == 2:
        print("------Sacar------")
        sacar = int(input("Valor do Saque: "))

        # verificar se o valor de saque é maior que o valor de que tem
        excedeu_saldo = valor > saldo_conta 

        excedeu_limite = valor > valor_limite_saque

        excedeu_saques = numero_de_saques >= LIMITE_SAQUES
        
        
        if excedeu_saldo:
            print('Saldo Indisponivel!\n'
                  f'Valor: R$ {saldo_conta},00')
        
        elif excedeu_limite:
            print("  valor de saque não podera ser maior que R$ 500,00  ")


        elif excedeu_saques:
            print("Você excedeu o numero de saques!!")

        elif valor > 0:
            saldo_conta -= sacar
            saidas.append(sacar)
            print()
            print(f'Saldo: R$ {saldo_conta},00')
            numero_de_saques += 1
            


    # Extrato
    elif opcao == 3:
        print("------Extrato------")
        print(f'Valor Depositado: R$ {sum(entradas)},00\n'
              f'Valor de Saque: R$ {sum(saidas)},00\n'
              f'Saldo Atual R$ {saldo_conta},00')        
    

    
    elif opcao == 4:
        break
    
    
    else:
        print("Favor digitar apenas as opções informadas!!")