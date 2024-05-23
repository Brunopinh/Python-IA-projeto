from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod

    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    # Dessa forma eu obrigo ele a passar o metodo e toda classe dependente
    @property
    @abstractproperty   
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV....")

    def desligar(self):
        print("Desligando a TV....")
        print("DEsligado.")

    @property
    def marca(self):
        print("hplint")    

class Controle_AR(ControleRemoto):
    def ligar(self):
        print("ligando o Ar condicionado")

    def desligar(self):
        print("Desligando o Ar condicionado")   
    
 
    def marca(self):
        print("consul")


controle =  ControleTV()
controle.ligar()
controle.desligar()

controle =  Controle_AR()
controle.desligar()
controle.marca()