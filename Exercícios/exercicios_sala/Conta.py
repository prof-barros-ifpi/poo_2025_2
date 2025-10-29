class Conta:
    def __init__(self, saldo, numero):
        self.saldo = saldo
        self.numero = numero
    
    def sacar(self, valor):
        if self.saldo <= 0:
            print("Erro. Saldo insuficiente.")
        elif self.saldo < valor:
            print("Erro. Valor maior que saldo.")
        else:
            self.saldo -= valor

    def depositar(self, valor):
        if valor <= 0:
            print("Erro. Valor de depósito inválido")
        else:
            self.saldo += valor

    def transferir(self, conta, valor):
        self.sacar(valor)
        conta.depositar(valor)

    def exibir_informacoes(self):
        print('--------------------------------')
        print(f"Conta número: {self.numero}")
        print(f"Saldo R$:{self.saldo}")
        print('--------------------------------')