from cliente import Cliente

class Conta(Cliente):
    def __init__(self, nome, saldo, limite):
        self.nome = nome
        self.saldo = saldo
        self.limite = limite

    def sacar(self, saque):
        self.saldo -= saque

    def depositar(self, deposito):
        self.saldo += deposito

