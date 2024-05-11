
# o que tiver depois da barra está com parametro e valor e amtes somente valor

def criar_carro_1(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


def criar_carro_2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)



criar_carro_1("palio",2000,"ABC-1234", marca="fiat", motor="1.0",combustivel="gasolina")

criar_carro_2(modelo="corolla",ano=2000,placa="ABC-1234", marca="fiat", motor="1.0",combustivel="gasolina")



