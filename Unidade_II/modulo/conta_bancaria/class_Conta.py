class Conta:
        #função que cria uma conta
    def __init__(self, titular, num, saldo=0):#__init__ é o construtor equivalente a struct
            self.titular = titular
            self.num = num
            self.saldo = saldo


    def deposito(self, valor):
            self.saldo += valor

    
    def transferencia(self, conta2, valor):

        if valor <= self.saldo:
                self.saldo -= valor
                conta2.saldo += valor
        else: 
                print ('saldo insuficiente')

    def imprime(self):
             print(self.titular, self.num, self.saldo) 
