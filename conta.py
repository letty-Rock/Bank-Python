class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de R$ {} do titular {}".format(self.saldo, self.titular))

    def deposita(self,valor):
        self.saldo += valor
        print("Você depositou R$ {}".format(valor))
    def sacar(self,valor):
        self.saldo -= valor
        print("Você sacou R$ {}".format(valor))
    def transferir(self,valor,destino):
         self.sacar(valor)
         destino.deposita(valor)
<<<<<<< HEAD

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

=======
   
       @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
>>>>>>> 10779894925afc8fd17b452e032ae12426cd32e5
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    