# Metodo contrutor
class Cachorro:
    # Contrutor de inicialização
    def __init__(self, nome, cor, acordado=True):
        print("Inicializamos a classe......")
        self.nome =nome
        self.cor= cor
        self.acordado= acordado
    
    def __del__(self):
        print("Removendo a instância da classe......")

    def falar(self):
        print("auau")


c = Cachorro("dog", "Amarelo") 
c.falar()        