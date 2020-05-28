# listas são mutáveis
# se é preciso uma sequencia sem tipos definidos, nem posições, usam-se listas
# caso seja necessário uma sequência com elementos definidos em posições definidas, usam-se tuplas

class ContaCorrente:

	def __init__(self, numero):
		self.numero = numero
		self.saldo = 0

	def deposita(self, valor):
		self.saldo += valor

	def __str__(self):
		return f'[>>Conta Corrente {self.numero} Saldo {self.saldo}<<]'


conta_do_henrique = ContaCorrente(1234)
conta_da_camily = ContaCorrente(4321)
print(conta_do_henrique)
print(conta_da_camily)

contas = [conta_da_camily, conta_do_henrique]

conta_do_henrique.deposita(200)
conta_da_camily.deposita(500)

[print(conta) for conta in contas if conta != None]

contas.extend([conta_do_henrique, conta_da_camily])

[(conta) for conta in contas if conta != None]