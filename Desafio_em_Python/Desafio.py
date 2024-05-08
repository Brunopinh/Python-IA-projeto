# desafio 2 







def depositar(valor, saldo_conta, saldo_inicial, extrato, entradas = [],  /):
    if valor > 0:
        saldo_inicial += valor
        saldo_conta += saldo_inicial
        entradas.append(valor) 
        extrato = f'Valor na Conta:  {saldo_conta:.2f}\n'
        print(extrato)   
        return saldo_conta, saldo_inicial, entradas

def sacar(*, valor, saldo_conta, extrato, saidas = [], excedeu_saldo,
    excedeu_limite, excedeu_saques, valor_limite_saque,numero_de_saques,
    LIMITE_SAQUES):

    # verificar se o valor de saque é maior que o valor de que tem
    excedeu_saldo = valor > saldo_conta
    # Verificar se tem limite por saque igual a 500
    excedeu_limite = valor > valor_limite_saque
    # verificar se ultrapassou a quantidade de saque
    excedeu_saques = numero_de_saques >= LIMITE_SAQUES
        
    if excedeu_saldo:
        print('Saldo Indisponivel!\n'
            f'Valor: R$ {saldo_conta}')
            
    elif excedeu_limite:
        print('Valor do saque não poderá ser maior que R$ 500,00')

    elif excedeu_saques:
        print('Você excedeu o numero de saques!!')
        
    elif valor > 0:
        saldo_conta -= valor
        saidas.append(valor)
        extrato = f'Valor: {saldo_conta}'
        print(extrato)
        numero_de_saques += 1

    return saidas, saldo_conta, numero_de_saques,    

def exibir_extratos(extrato, entradas, saidas):
    print("------Extrato------")
    print(f'Valor Depositado: R$ {sum(entradas)},00\n'
          f'Valor de Saque: R$ {sum(saidas)},00\n'
          f'Saldo Atual R$ {extrato:.2f}')    
    

# main        
def main():

    # Variaveis
    saldo_inicial = 0 
    saldo_conta = 0
    valor = 0
    extrato = ""
    
    # Variaveis para tratamento
    excedeu_saldo = 0
    excedeu_limite = 0
    excedeu_saques = 0
    
    # limite de saque que o usuario pode fazer
    LIMITE_SAQUES = 3
    valor_limite_saque = 500
    numero_de_saques = 0

    entradas = []
    saidas = []

    while True:
        print(entradas)
        print(saidas)
        opcao =  int(input("""
        ======= Sistema =======
            [1] - Depositar
            [2] - Sacar
            [3] - Extrato
            [4] - Sair do Sistema!       
        =======================

        :"""))
         
        
        if opcao == 1:

            valor = float(input("Informe o valor de deposito: "))
            saldo_conta, extrato, entradas = depositar(valor,saldo_conta, saldo_inicial ,extrato, entradas )

        elif opcao == 2:
            valor= float(input("Digite o valor de saque: "))
            saldo_conta, numero_de_saques, saidas = sacar(
                valor = valor,
                saldo_conta = saldo_conta,
                extrato = extrato,
                excedeu_saldo = excedeu_saldo,
                excedeu_limite = excedeu_limite,
                excedeu_saques = excedeu_saques,
                LIMITE_SAQUES = LIMITE_SAQUES,
                valor_limite_saque = valor_limite_saque,
                numero_de_saques = numero_de_saques,
                saidas = saidas    
            )
        elif opcao == 3:
           exibir_extratos(extrato, entradas = entradas, saidas = saidas)        
         
   

main()


    


     

