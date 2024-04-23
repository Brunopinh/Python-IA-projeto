deposito = int(input("Digite o valor do deposito: "))

def sacar(valor):
    
    if valor > deposito:
        print(f'seu saldo é insuficiente: {valor}')
    
    else:
        registro = deposito - valor
        print(f'Valor sacado: {registro}')

sacar(90)


