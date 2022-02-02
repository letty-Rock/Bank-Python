class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R$ {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self,valor):
        self.__saldo += valor
        print("Você depositou R$ {}".format(valor))
    def sacar(self,valor):
        self.__saldo -= valor
        print("Você sacou R$ {}".format(valor))
    def transferir(self,valor,destino):
         self.sacar(valor)
         destino.deposita(valor)
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite
    def set_limite(self,limite):
        self.__limite = limite     