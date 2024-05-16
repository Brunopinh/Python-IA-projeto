
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    

    def ligar_motor(self):
        print("ligando o motor")

class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    
    def __init__(self, cor, placa, numero_rodas, carregado):
        #
        super().__init__(cor,placa,numero_rodas)
        self.carregado = carregado
    

    # metodo da minha classe
    def esta_carregado(self):
        print(f"{'sim' if self.carregado else 'Não'}, Estou Carregado")


caminhao = Caminhao("roxo", "gfh-9087", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)