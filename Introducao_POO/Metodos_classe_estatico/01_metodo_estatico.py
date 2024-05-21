class Pessoa:
    def __init__(self, nome=None, idade= None):
        self.nome = nome
        self.idade =  idade
    
    # Utilização de decoretor
    @classmethod
    def criar_de_data_nascimento(self, ano, mes, dia, nome):
        idade = 2024 - ano
        return (nome, idade)    
         
    @staticmethod
    def e_maior_idade(idade):
        return idade > 18



p = Pessoa.criar_de_data_nascimento(2001,3,21, "Bruno")
print(p.nome, p.idade)

