
def lista_equipamentos(itens = []):
    print('Lista de Equipamentos:')
    for iten in itens:
        print(f'- {iten}')



itens = []

valor = str(input("Digite o nome dos objetos: "))
itens.append(valor)
lista_equipamentos(itens)


