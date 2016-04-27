
import random

class Dado(object):
	def __init__(self):
		self.tipo = None

	def rolarDadoCombate(self):

		min = 1
		max = 8 if self.tipo == 5 else 6
		max = 12 if self.tipo == 7 else max

		resultados = []

		for i in range(10000):
			resultados.append(random.randint(min, max))

		resultado = random.choice(resultados)

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
				self.exibirNumero(resultado, True)
			else:
				self.exibirVazio()
		elif self.tipo == 4 or self.tipo == 5 or self.tipo == 7:
			valor = resultado
			self.exibirNumero(resultado, False)
		elif self.tipo == 6:
			valor = 1
			if resultado <= 2:
				self.exibirVazio()
			elif resultado == 3:
				print("+1 HP")
			elif resultado == 4:
				print("+2 HP")
			elif resultado == 5:
				print("Teleport")
			elif resultado == 6:
				print("1 PC = 1 Stats")
				

		return valor

	def exibirVazio(self):
		print("Face Vazia (v = 0).")

	def exibirNumero(self, n, exibirSinal):
		print("{}{}.".format("+" if exibirSinal else "", n))

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

def inputInteiro(mensagem, min = 0, max = 0):
	valor = 0

	while valor == 0:
		valor = input(mensagem)

		try:
			valor = int(valor)

			if min > 0:
				if valor < min or valor > max:
					valor = 0
		except ValueError:
			valor = 0

	return valor

while True:
	tipoDados = inputInteiro("Insira o tipo dos dados:\n1 = ATK\n2 = DEF\n3 = Auxílio\n4 = D6\n5 = D8\n6 = Dado Personagem\n7 = D12\n", 1, 7)

	if tipoDados == 3 or tipoDados == 5 or tipoDados == 6 or tipoDados == 7:
		numeroDadosTotal = 1
		numeroDadosPegar = 1
	else:
		numeroDadosTotal = inputInteiro("Insira a quantidade de dados: ")
		if tipoDados == 1 or tipoDados == 2:
			numeroDadosPegar = inputInteiro("Insira a quantidade de dados para somar: ")

	dado.tipo = tipoDados

	resultados = []

	print("Resultado:")
	for i in range(numeroDadosTotal):
		resultados.append(dado.rolarDadoCombate())

	resultados = sorted(resultados, reverse = True)

	totalRolagem = 0
	for i in range(numeroDadosPegar):
		totalRolagem += resultados[i]

	if tipoDados == 1 or tipoDados == 2:
		print("Total da Rolagem: {}".format(totalRolagem))
