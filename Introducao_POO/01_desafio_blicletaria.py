class Bicicleta:
    # Bloco vazio
    # pass

    # construtor 
    def __init__(self, cor, modelo, ano, valor):
        # Self é uma definição para o objeto
        self.cor = cor
        self.modelo = modelo
        self.ano = ano  # Atributos da classe
        self.valor = valor
    
    # Metodos são funções dentro uma classe
    def buzina(self):
        print("plim plim")

    def parar(self):
        print("Parando bicicleta..")
        print("Correr")

    def correr(self):
        print("Vrumm")

    #def __str__(self):
    #    return f"Bicicleta: Cor={self.cor}, Modelo={self.modelo}, Ano={self.ano}, Valor={self.valor}"            

    def __str__(self):
       return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

        

b2 = Bicicleta("verde", "monaik", 2000, 600)    
print(b2)
