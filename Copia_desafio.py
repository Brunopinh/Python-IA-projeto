# desafio 2 






def saldo_atual(saldo_inicial, entradas, saidas):
    return saldo_inicial + sum(entradas) - sum(saidas)


def depositar(valor, entradas):
    entradas.append(valor) 
       

def sacar(valor,saida):

    saida.append(valor)

   
     
def exibir_extratos(saldo_inicial,entradas, saidas):
    print("------Extrato------")
    print(f'Saldo incial R$ {saldo_inicial}'
          f'Valor Depositado: R$ {sum(entradas)}\n'
          f'Valor de Saque: R$ {sum(saidas)}\n'
          f'Saldo Atual R$ {saldo_atual(saldo_inicial,entradas,saidas):.2f}')    
    

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
     
        opcao =  int(input("""
        ======= Sistema =======
            [1] - Depositar
            [2] - Sacar
            [3] - Extrato
            [4] - Sair do Sistema!       
        =======================

        :"""))
         
        saldo_conta = saldo_atual(saldo_inicial,entradas,saidas) 
        
        if opcao == 1:

            valor = float(input("Informe o valor de deposito: "))
            if valor > 0:
                depositar(valor, entradas)

            else:
                print("favor digitar numero maior que zero 0")    

        elif opcao == 2:

            valor = float(input("Digite o valor de saque: "))
            if valor > saldo_conta:
                print(f'Valor maior que {saldo_conta}')
            else:
                sacar(valor,saidas)

        elif opcao == 3:
           exibir_extratos(saldo_inicial,entradas = entradas, saidas = saidas)        
         
   

main()


    


     

