class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo o objeto ... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O saldo da conta {self.__numero} é: {self.__saldo}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if self.__pode_sacar():
            self.__saldo -= valor
        else:
            print(f'O valor:{valor}, excede o seu limite!')

    def __pode_sacar(self, valor_a_sacar):
        limite_total = self.__saldo + self.__limite
        return valor_a_sacar <= limite_total

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # essa anotação define o método como sendo getter, no paradigma OO
    @property
    def numero(self):
       return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    # definir getters e setters somente se necessário.
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # métodos estáticos são úteis quando se têm atributos que são comuns a todos os métodos de uma
    # classe e também sejam valores padrão. Em python eles não vão possuir atributo de referência ao objeto(self)
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}