# Neste exemplo iremos mostrar o conceito de publico e privado

class Conta:
    def __init__(self,nro_agencia,saldo=0):
        # _ siginifica que meu saldo é do tipo privado....
        self._saldo = saldo
        self.nro_agencia = nro_agencia


    def deposita(self,valor):
        self._saldo += valor


    def sacar(self, valor):
        self._saldo -= valor

    def mostar_saldo(self):
        return self._saldo




conta = Conta("0001")
conta.deposita(100)
conta.sacar(10)
print(conta.mostar_saldo())

  