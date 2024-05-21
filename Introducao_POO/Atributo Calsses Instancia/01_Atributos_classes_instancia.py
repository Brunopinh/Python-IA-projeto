class Estudante:
    # variaveis de classe
    escola = 'Dio'


    # observação "self" é uma instância
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'    
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

#Estudante.escola = 'teste'

# Passo os valores 
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)

# chamdo o mostrar valor
mostrar_valores(aluno_1, aluno_2)





