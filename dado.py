
import random

class Dado(object):
	def __init__(self):
		self.tipo = None

	def rolarDadoCombate(self):
		resultado = random.randint(1, 6)

		valor = 0

		if self.tipo == 1 or self.tipo == 2:
			if resultado <= 3:
				self.exibirVazio()
			elif resultado <= 5:
				self.exibirNormal()
				valor = 1
			elif resultado == 6:
				self.exibirCritico()
				valor = 2
		elif self.tipo == 3:
			if resultado <= 3:
				valor = resultado
				self.exibirNumero(resultado)
			else:
				self.exibirVazio()

		return valor

	def exibirVazio(self):
		print("Face Vazia (v = 0).")

	def exibirNumero(self, n):
		print("+{}.".format(n))

	def exibirNormal(self):
		if self.tipo == 1:
			print("Golpe Normal (v = 1).")
		else:
			print("Escudo Normal (v = 1).")

	def exibirCritico(self):
		if self.tipo == 1:
			print("Golpe Crítico (v = 2).")
		else:
			print("Escudo Fortalecido (v = 2).")

dado = Dado()

while True:
	tipoDados = int(input("Insira o tipo dos dados (1 = ataque, 2 = defesa e 3 = números): "))
	if tipoDados < 3:
		numeroDadosTotal = int(input("Insira a quantidade de dados: "))
		numeroDadosPegar = int(input("Insira a quantidade de dados para somar: "))
	else:
		numeroDadosTotal = 1
		numeroDadosPegar = 1

	dado.tipo = tipoDados

	resultados = []

	print()
	for i in range(numeroDadosTotal):
		resultados.append(dado.rolarDadoCombate())
	print()

	resultados = sorted(resultados, reverse = True)

	totalRolagem = 0
	for i in range(numeroDadosPegar):
		totalRolagem += resultados[i]

	if tipoDados == 1 or tipoDados == 2:
		print("Total da Rolagem: {}".format(totalRolagem))

	print("------------------------------------")
