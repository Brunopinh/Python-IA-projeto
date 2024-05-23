class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade =  idade
    
    # Utilização de decoretor
    @classmethod

    ########
    # Se eu precisar ter acesso ao contesto da classe
    # então eu irei utilizar um metodo de classe chamado
    # classmethod

    ######
    # com essa opção cls eu retiro o o objeto self
    def criar_de_data_nascimento(cls,ano, mes, dia, nome):
        #  verifico a idade e calculo
        idade = 2024 - ano
        return cls(nome, idade)    

    #####
    # ja se eu não de nenhum contesto de classe eu utilzo o metodo
    # staticmethod
    ######     
    @staticmethod
    def e_maior_idade(idade):
        return idade > 18



p = Pessoa.criar_de_data_nascimento(2001, 4, 21,"Bruno")
print(p.nome, p.idade)


print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(20))
