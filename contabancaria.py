class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        
        else:
            print("valor inválido")

conta = ContaBancaria("Maria", 23000)
print(conta.get_saldo())
conta.set_saldo(-30000)
print(conta.get_saldo())
