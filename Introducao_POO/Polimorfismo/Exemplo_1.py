class Passaro:
    def voar(self):
        print("Voando")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

# não utilziar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando")


# utilizando conceito de Polimorfismo
def plano_voo(obj):
    obj.voar()



plano_voo(Pardal())    
