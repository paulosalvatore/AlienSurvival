
import random, time

cartas = {
	"Armadilhas": [
		"Buraco no Casco",
		"Buraco no Casco",
		"Cabos Faltando",
		"Cabos Faltando",
		"Propulsores Defeituosos",
		"Propulsores Defeituosos",
		"Curto-circuito",
		"Curto-circuito",
		"Incêndio",
		"Incêndio"
	],
	"Setor A": [
		"Placa de Metal",
		"Placa de Metal",
		"Solda",
		"Pistola Laser",
		"Cabo de Conexão",
		"Kit de Reparo: Energia",
		"Oxigênio",
		"Energia",
		"Kit Primeiros Socorros",
		"Kit Primeiros Socorros",
		"Kit Primeiros Socorros",
		"Equipamento Quebrado",
		"Equipamento Quebrado",
		"Lixo Espacial",
		"Lixo Espacial"
	],
	"Setor B": [
		"Solda",
		"Pistola Laser",
		"Cabo de Conexão",
		"Kit de Reparo: Energia",
		"Kit de Reparo: Energia",
		"Oxigênio",
		"Extintor",
		"Integridade",
		"Integridade",
		"Kit Primeiros Socorros",
		"Kit Primeiros Socorros",
		"Kit Primeiros Socorros",
		"Lixo Espacial",
		"Lixo Espacial",
		"Lixo Espacial"
	],
	"Setor C": [
		"Solda",
		"Pistola Laser",
		"Cabos de Conexão",
		"Cabos de Conexão",
		"Cabos de Conexão",
		"Kit de Reparo: Propulsores",
		"Extintor",
		"Energia",
		"Integridade",
		"Kit Primeiros Socorros",
		"Kit Primeiros Socorros",
		"Kit Primeiros Socorros",
		"Equipamento Quebrado",
		"Equipamento Quebrado",
		"Equipamento Quebrado"
	],
	"Setor D": [
		"Placa de Metal",
		"Pistola Laser",
		"Cabo de Conexão",
		"Kit de Reparo: Propulsores",
		"Kit de Reparo: Propulsores",
		"Oxigênio",
		"Extintor",
		"Energia",
		"Kit Primeiros Socorros",
		"Kit Primeiros Socorros",
		"Kit Primeiros Socorros",
		"Equipamento Quebrado",
		"Equipamento Quebrado",
		"Lixo Espacial",
		"Lixo Espacial"
	],
	"Monstros 1": [
		# [Rank, Ameaça, HP]
		["A", 2, 2],
		["A", 2, 2],
		["A", 3, 2],
		["B", 2, 2],
		["B", 2, 2],
		["B", 3, 2],
		["C", 2, 2],
		["C", 2, 2],
		["C", 3, 2],
		["D", 2, 2],
		["D", 2, 2],
		["D", 3, 2]
	],
	"Monstros 2": [
		# [Rank, Ameaça, HP]
		["A", 3, 3],
		["A", 3, 3],
		["A", 4, 3],
		["B", 3, 3],
		["B", 3, 3],
		["B", 4, 3],
		["C", 3, 3],
		["C", 3, 3],
		["C", 4, 3],
		["D", 3, 3],
		["D", 3, 3],
		["D", 4, 3]
	],
	"Monstros 3": [
		# [Rank, Ameaça, HP]
		["A", 4, 5],
		["A", 4, 5],
		["A", 5, 5],
		["B", 4, 5],
		["B", 4, 5],
		["B", 5, 5],
		["C", 4, 5],
		["C", 4, 5],
		["C", 5, 5],
		["D", 4, 5],
		["D", 4, 5],
		["D", 5, 5]
	]
}

baralho = {}

def definirBaralho():
	for tipo in cartas:
		baralho[tipo] = []
		for carta in cartas[tipo]:
			baralho[tipo].append(carta)

def sacarCartas(tipo):
	reembaralhar = True
	if tipoCartas == "1":
		tipo = "Armadilhas"
		reembaralhar = False
	elif tipoCartas == "a":
		tipo = "Setor A"
	elif tipoCartas == "b":
		tipo = "Setor B"
	elif tipoCartas == "c":
		tipo = "Setor C"
	elif tipoCartas == "d":
		tipo = "Setor D"
	elif tipoCartas == "m1":
		tipo = "Monstros 1"
	elif tipoCartas == "m2":
		tipo = "Monstros 2"
	elif tipoCartas == "m3":
		tipo = "Monstros 3"
	else:
		print("Insira informações válidas.")
		return

	lista = baralho[tipo]

	if len(lista) == 0:
		if reembaralhar:
			definirBaralho()
			lista = baralho[tipo]
			print("Cartas acabaram. Reembaralhar.")
		else:
			print("Não há mais cartas desse tipo.")
			return

	carta = random.choice(lista)
	lista.remove(carta)
	print("{}: {}".format(tipo, carta))
	time.sleep(1)
	print()

definirBaralho()

while True:
	tipoCartas = input("1, A, B, C, D, m1, m2 ou m3:\n")

	sacarCartas(tipoCartas)
