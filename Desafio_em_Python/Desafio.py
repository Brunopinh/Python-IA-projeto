# desafio 2 




# criando usuarios

def criar_usuario(*,id,nome, sobrenome, idade, cadastro = [] ):
    if id in cadastro:
        print("Usuario já existente")

    else:
        cadastro.append(id)
        cadastro.append(nome)
        cadastro.append(sobrenome)
        cadastro.append(idade)
        print()
        print("cadastro realizado com sucesso!!")

    return id, nome, sobrenome, idade, cadastro

def listar_usuarios(cadastro):
    for dados in enumerate(cadastro):
        print(dados)
        
    
def deletar_usuario(criar_usuario(cadastro)):
        if id in cadastro:
            
        return criar_usuario
    
    

def criar_conta(numero_conta, cadastro = []):
    if numero_conta in cadastro:
        print("Cadastro já Existe!! ")

    else:
        print()    
    return cadastro.append(numero_conta)


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

    return saldo_conta, numero_de_saques, saidas    

def exibir_extratos(extrato, entradas, saidas):
    print("------Extrato------")
    print(f'Valores Depositados: R$ {entradas}\n'
          f'Totais Depositos: R$ {sum(entradas)}\n'
          f'Valores de Saques: R$ {saidas}\n'
          f'Total de Saques: R$ {sum(saidas)}\n'
          f'Saldo Atual em Conta: R$ {extrato:.2f}')    
    

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
    
    #Variaveis para cadastro de conta
    id = 0
    nome = "",
    sobrenome = "",
    idade = "",
    cadastro = []
    validar = 0

    while True:
       
        opcao =  str(input("""
        ======= Sistema =======
            [C] - Criar Usuario
            [L] - Listar Usuario
            [D] - Deletar usuario
                                                                        
            [1] - Depositar
            [2] - Sacar
            [3] - Extrato
            [4] - Sair do Sistema!       
        =======================

        :"""))
         
        
        if opcao == '1':

            valor = float(input("Informe o valor de deposito: "))
            saldo_conta, extrato, entradas = depositar(valor,saldo_conta, saldo_inicial ,extrato, entradas )

        elif opcao == '2':
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
        elif opcao == '3':
           exibir_extratos(extrato, entradas = entradas, saidas = saidas)        

        elif opcao == 'c':
           id =  int(input("Digite o id do usuario: "))
           nome = str(input("Nome: "))
           sobrenome = str(input("Sobrenome: "))
           idade = str(input("idade: "))
           id,nome, sobrenome, idade,cadastro = criar_usuario(id = id, nome = nome, sobrenome = sobrenome, idade=idade, cadastro=cadastro)


        elif opcao == 'l':
            listar_usuarios(cadastro)

       # elif opcao == 'd':
        #     print("id: ", listar_usuarios(cadastro[id]))
             
         #    validar =  int(input("Digite o id do usuario: "))
            # if validar in cadastro:
               #  pop.criar_usuario()
        elif opcao == 4:
            break

main()


    


     

