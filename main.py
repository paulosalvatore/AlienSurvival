
import pygame as pg, os, sys, random

config = {
	"janela": {
		"titulo": "Jogo",
		"tamanho": [0, 0],
		"corFundo": (255, 255, 255),
		"cores": [
			(117, 117, 117), # Cinza
			(0, 0, 0), # Preto
			(232, 230, 83), # Amarelo
			(27, 122, 27), # Verde
			(221, 30, 30), # Vermelho
			(0, 0, 255) # Azul
		]
	},
	"jogo": {
		"area": (11, 11),
		"areaJanela": (11, 11),
		"areaJanelaExtra": (4, 0),
		"borda": 64,
		"limiteTurnos": 20
	},
	"tiles": {
		"tamanho": 64,
		"tipos": {
			0: {
				"nomeArquivo": "Tile1",
				"block": False,
				"quantidade": 22,
				"rotacao": [1, 1],
				"arquivos": []
			},
			1: {
				"nomeArquivo": "Tile2",
				"block": False,
				"quantidade": 29,
				"rotacao": [1, 1, 1, 1],
				"arquivos": []
			},
			2: {
				"nomeArquivo": "Tile3",
				"block": False,
				"quantidade": 29,
				"rotacao": [1, 1, 1, 1],
				"arquivos": []
			},
			3: {
				"nomeArquivo": "Tile4",
				"block": False,
				"quantidade": 6,
				"rotacao": [1],
				"arquivos": []
			}
		}
	},
	"jogadores": {
		"margem": 16,
		"quantidade": 4,
		"posicoes": [],
		"arquivos": [],
		"nomes": ("Amarelo", "Azul", "Vermelho", "Verde")
	},
	"mapa": [
		[[1, 2, 3], -1, [2, 1, 4], -1, [1, 1, 6], -1, [1, 2, 3], -1, [2, 1, 5], -1, [1, 1, 6]],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[[2, 2, 5], -1, [2, 4, 4], -1, [3, 1, 3], -1, [3, 1, 6], -1, [2, 3, 5], -1, [2, 4, 4]],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[[1, 3, 3], -1, [3, 1, 6], -1, [2, 2, 5], -1, [2, 1, 4], -1, [3, 1, 3], -1, [1, 4, 6]],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[[1, 2, 4], -1, [3, 1, 5], -1, [2, 3, 6], -1, [2, 4, 3], -1, [3, 1, 4], -1, [1, 1, 5]],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[[2, 2, 6], -1, [2, 1, 3], -1, [3, 1, 4], -1, [3, 1, 5], -1, [2, 2, 6], -1, [2, 4, 3]],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[[1, 3, 4], -1, [2, 3, 3], -1, [1, 4, 5], -1, [1, 3, 4], -1, [2, 3, 6], -1, [1, 4, 5]]
	],
	"mapaAtual": [],
	"sobressalente": {
		"posicao": [13, 5],
		"valor": [-1, 1, 1]
	},
	"armadilhas": {
		"margem": 16,
		"quantidade": 16,
		"arquivo": [],
		"mapa": [],
		"sobressalente": 0
	},
	"setaRotacionar": {
		"posicao": [896 + 8, 448 + 8],
		"tamanho": [48, 48],
		"arquivos": []
	},
	"avancarTurno": {
		"posicao": [832 + 8, 640 + 8],
		"tamanho": [192, 64],
		"arquivos": []
	},
	"movimentoProibido": {
		"posicao": [0, 0],
		"tamanho": 32,
		"margem": [
			[-36, 16], # Esquerda para Direita
			[16, -36], # Cima para Baixo
			[68, 16], # Direita para Esquerda
			[16, 68] # Baixo para Cima
		],
		"arquivo": ""
	},
	"textoTela": {
		"posicao": [32, 16],
		"cor": (0, 0, 0)
	},
	"cursores": [
		{
			"esquema": "default",
			"cursor": ""
		},
		{
			"esquema": (
				"     XX         ",
				"    X..X        ",
				"    X..X        ",
				"    X..X        ",
				"    X..XXXXX    ",
				"    X..X..X.XX  ",
				" XX X..X..X.X.X ",
				"X..XX.........X ",
				"X...X.........X ",
				" X.....X.X.X..X ",
				"  X....X.X.X..X ",
				"  X....X.X.X.X  ",
				"   X...X.X.X.X  ",
				"    X.......X   ",
				"     X....X.X   ",
				"     XXXXX XX   "
			),
			"cursor": ""
		}
	]
}

def carregarCursores():
	for i in range(len(config["cursores"])):
		esquema = config["cursores"][i]["esquema"]
		if esquema == "default":
			cursor = pg.mouse.get_cursor()
		else:
			curs, mask = pg.cursors.compile(esquema, ".", "X")
			cursor = ((16, 16), (5, 1), curs, mask)
		config["cursores"][i]["cursor"] = cursor

def definirTamanhoJanela():
	configJogo = config["jogo"]
	areaJanela = configJogo["areaJanela"]
	areaJanelaExtra = configJogo["areaJanelaExtra"]
	borda = configJogo["borda"]
	tamanhoTile = config["tiles"]["tamanho"]
	config["janela"]["tamanho"][0] = borda * 2 + (areaJanela[0] + areaJanelaExtra[0]) * tamanhoTile
	config["janela"]["tamanho"][1] = borda * 2 + (areaJanela[1] + areaJanelaExtra[1]) * tamanhoTile

def calcularPosicao(x, y):
	tamanhoTile = config["tiles"]["tamanho"]
	borda = config["jogo"]["borda"]
	posicaoX = x * tamanhoTile + borda
	posicaoY = y * tamanhoTile + borda
	return (posicaoX, posicaoY)

def calcularCoordenadas(tamanho, limitar = False):
	borda = config["jogo"]["borda"]
	tamanho = [tamanho[0] - borda, tamanho[1] - borda]
	tamanhoTile = config["tiles"]["tamanho"]
	tamanhoMax = config["jogo"]["area"]

	posicao = (
		int((tamanho[0] - tamanho[0] % tamanhoTile) / tamanhoTile),
		int((tamanho[1] - tamanho[1] % tamanhoTile) / tamanhoTile)
	)

	if limitar:
		posicao = (
			max(min(tamanhoMax[0] - 1, posicao[0]), 0),
			max(min(tamanhoMax[1] - 1, posicao[1]), 0)
		)

	if	((posicao[0] < 0 or posicao[0] > tamanhoMax[0] - 1) or
		(posicao[1] < 0 or posicao[1] > tamanhoMax[1] - 1)):
		return False

	return posicao

def validarCoordenadasInsercaoTile(posicao):
	if (posicao[0] + 1) % 2 == 0 or (posicao[1] + 1) % 2 == 0:
		return True
	return False

def carregarImagem(arquivo):
	tamanhoTile = config["tiles"]["tamanho"]
	imagem = pg.image.load(os.path.join(sys.path[0], "imagens/"+arquivo+".png")).convert_alpha()
	return pg.transform.scale(imagem, (tamanhoTile, tamanhoTile))

def carregarImagensTiles():
	for i in range(len(config["tiles"]["tipos"])):
		nomeArquivo = config["tiles"]["tipos"][i]["nomeArquivo"]
		rotacao = config["tiles"]["tipos"][i]["rotacao"]

		for j in range(len(rotacao)):
			angulo = rotacao[j] * j * 90
			arquivo = pg.transform.rotate(carregarImagem(nomeArquivo), angulo)
			config["tiles"]["tipos"][i]["arquivos"].insert(j, arquivo)

def carregarSetaRotacionar():
	nomeArquivoBase = "setaRotacionar"
	for i in range(2):
		nomeArquivo = nomeArquivoBase + str(i + 1)
		tamanho = config["setaRotacionar"]["tamanho"]
		imagem = pg.image.load(os.path.join(sys.path[0], "imagens/"+nomeArquivo+".png")).convert_alpha()
		config["setaRotacionar"]["arquivos"].append(pg.transform.scale(imagem, (tamanho[0], tamanho[1])))

def carregarAvancarTurno():
	nomeArquivoBase = "avancarTurno"
	for i in range(2):
		nomeArquivo = nomeArquivoBase + str(i + 1)
		config["avancarTurno"]["arquivos"].append(pg.image.load(os.path.join(sys.path[0], "imagens/"+nomeArquivo+".png")).convert_alpha())

def carregarMovimentoProibido():
	nomeArquivo = "movimentoProibido"
	config["movimentoProibido"]["arquivo"] = pg.image.load(os.path.join(sys.path[0], "imagens/"+nomeArquivo+".png")).convert_alpha()

def carregarArmadilha():
	nomeArquivo = "armadilha"
	config["armadilhas"]["arquivo"] = pg.image.load(os.path.join(sys.path[0], "imagens/"+nomeArquivo+".png")).convert_alpha()

def carregarJogadores():
	jogadores = config["jogadores"]
	quantidade = jogadores["quantidade"]

	for i in range(quantidade):
		nomeArquivo = str(i + 1)
		imagem = pg.image.load(os.path.join(sys.path[0], "imagens/"+nomeArquivo+".png")).convert_alpha()

		x = 0 if i == 0 or i == 3 else config["jogo"]["area"][0] - 1
		y = 0 if i < 2 else config["jogo"]["area"][1] - 1

		config["jogadores"]["arquivos"].append(imagem)
		config["jogadores"]["posicoes"].insert(i, (x, y))

def verificarJogadoresPosicao(x, y):
	jogadores = config["jogadores"]
	quantidade = jogadores["quantidade"]
	posicoes = jogadores["posicoes"]

	jogadoresPosicao = []

	for i in range(quantidade):
		posicao = posicoes[i]
		if posicao[0] == x and posicao[1] == y:
			jogadoresPosicao.append(i)

	if len(jogadoresPosicao) > 0:
		return jogadoresPosicao

	return False

class Jogadores(pg.sprite.Sprite):
	def __init__(self, id, posicao):
		pg.sprite.Sprite.__init__(self)
		self.image = config["jogadores"]["arquivos"][id]
		self.rect = self.image.get_rect(topleft = posicao)
		self.mask = pg.mask.from_surface(self.image)

class Tiles(pg.sprite.Sprite):
	def __init__(self, posicao, id, rotacao, cor):
		pg.sprite.Sprite.__init__(self)
		tamanhoTile = config["tiles"]["tamanho"]
		imagem = pg.Surface((tamanhoTile, tamanhoTile)).convert_alpha()
		imagem.fill(config["janela"]["cores"][cor])
		imagem.blit(config["tiles"]["tipos"][id]["arquivos"][rotacao - 1], (0, 0))
		self.image = imagem
		self.rect = self.image.get_rect(topleft = posicao)
		self.mask = pg.mask.from_surface(self.image)

class SetaRotacionar(pg.sprite.Sprite):
	def __init__(self, img):
		pg.sprite.Sprite.__init__(self)
		setaRotacionar = config["setaRotacionar"]
		tamanho = setaRotacionar["tamanho"]
		posicao = setaRotacionar["posicao"]
		imagem = pg.Surface((tamanho[0], tamanho[1])).convert_alpha()
		imagem.fill(config["janela"]["corFundo"])
		imagem.blit(setaRotacionar["arquivos"][img], (0, 0))
		self.image = imagem
		self.rect = self.image.get_rect(topleft = posicao)
		self.mask = pg.mask.from_surface(self.image)

class AvancarTurno(pg.sprite.Sprite):
	def __init__(self, img):
		pg.sprite.Sprite.__init__(self)
		avancarTurno = config["avancarTurno"]
		tamanho = avancarTurno["tamanho"]
		posicao = avancarTurno["posicao"]
		imagem = pg.Surface((tamanho[0], tamanho[1])).convert_alpha()
		imagem.fill(config["janela"]["corFundo"])
		imagem.blit(avancarTurno["arquivos"][img], (0, 0))
		self.image = imagem
		self.rect = self.image.get_rect(topleft = posicao)
		self.mask = pg.mask.from_surface(self.image)

class MovimentoProibido(pg.sprite.Sprite):
	def __init__(self, posicao):
		pg.sprite.Sprite.__init__(self)
		self.image = config["movimentoProibido"]["arquivo"]
		self.rect = self.image.get_rect(topleft = posicao)
		self.mask = pg.mask.from_surface(self.image)

class Armadilhas(pg.sprite.Sprite):
	def __init__(self, posicao):
		pg.sprite.Sprite.__init__(self)
		armadilhas = config["armadilhas"]
		margem = armadilhas["margem"]
		self.image = armadilhas["arquivo"]
		self.rect = self.image.get_rect(topleft = posicao)
		self.mask = pg.mask.from_surface(self.image)

class Control(object):
	def __init__(self):
		self.screen = pg.display.get_surface()
		self.clock = pg.time.Clock()
		self.fps = 60.0
		self.done = False
		self.jogoFinalizado = False
		self.ultimoEvento = 0

		self.keys = pg.key.get_pressed()
		self.mouse = pg.mouse.get_pressed()
		self.posicaoMouse = pg.mouse.get_pos()

		self.aplicarDelay = False
		self.tempoDelay = 500

		self.jogadorAtual = 0
		self.turnoAtual = 1
		self.limiteTurnos = config["jogo"]["limiteTurnos"]

		self.imgSetaRotacionar = 1
		self.imgAvancarTurno = 1

		self.definirCenario()

		self.definirJogadores()

		tamanhoJanela = config["janela"]["tamanho"]
		self.level = pg.Surface((tamanhoJanela[0], tamanhoJanela[1])).convert()
		self.level_rect = self.level.get_rect()
		self.viewport = self.screen.get_rect(top = self.level_rect.top)

	def finalizarJogo(self):
		self.jogoFinalizado = True

	def carregarTextoTela(self):
		fonte = pg.font.SysFont("verdana", 32)

		if self.jogoFinalizado:
			texto = "Jogo Finalizado."
		else:
			texto = "Turno: {} - Jogador Atual: {}".format(self.turnoAtual, config["jogadores"]["nomes"][self.jogadorAtual])

		self.textoTela = fonte.render(texto, 1, config["textoTela"]["cor"])
		self.posicaoTextoTela = self.textoTela.get_rect()
		self.posicaoTextoTela.topleft = config["textoTela"]["posicao"]

	def mudarCorTile(self):
		posicao = calcularCoordenadas(self.posicaoMouse)

		if posicao:
			tile = config["mapaAtual"][posicao[1]][posicao[0]]

			if not (type(tile) is int) and len(tile) >= 2:
				cor = 1 if len(tile) == 2 else tile[2]
				novaCor = cor if len(tile) == 4 and tile[3] == 2 else 2

				config["mapaAtual"][posicao[1]][posicao[0]] = [tile[0], tile[1], cor, novaCor]
				self.cenario = self.criarCenario()

		return posicao

	def mudarTurnoAtual(self):
		if self.jogadorAtual < config["jogadores"]["quantidade"] - 1:
			self.jogadorAtual = self.jogadorAtual + 1
		else:
			self.jogadorAtual = 0
			self.turnoAtual = self.turnoAtual + 1
			if self.turnoAtual > self.limiteTurnos:
				self.finalizarJogo()
		self.carregarTextoTela()

	def movimentarJogador(self):
		posicao = calcularCoordenadas(self.posicaoMouse)

		if posicao:
			config["jogadores"]["posicoes"][self.jogadorAtual] = posicao

			self.definirJogadores()

		return posicao

	def definirJogadores(self):
		jogadores = []

		for i in range(config["jogadores"]["quantidade"]):
			posicao = config["jogadores"]["posicoes"][i]
			posicaoCalculada = calcularPosicao(posicao[0], posicao[1])
			margem = config["jogadores"]["margem"]
			jogador = Jogadores(i, (posicaoCalculada[0] + margem, posicaoCalculada[1] + margem))
			jogadores.append(jogador)

		self.jogadores = pg.sprite.Group(jogadores)

	def definirCenario(self):
		self.movimentoProibido = None
		self.jogadorAtual = 0
		self.turnoAtual = 1
		config["mapaAtual"] = []
		self.tilesDisponiveis = self.carregarTilesDisponiveis()
		self.cenario = self.criarCenario()
		self.definirTileSobressalente()
		self.definirSetaRotacionar()
		self.definirAvancarTurno()
		self.definirMapaArmadilhas()
		self.criarArmadilhas()
		carregarJogadores()
		self.jogadores = []
		self.definirJogadores()
		self.carregarTextoTela()

	def criarCenario(self):
		cenario = []

		if len(config["mapaAtual"]) > 0:
			mapa = config["mapaAtual"]
			mapaAtual = config["mapaAtual"]
		else:
			mapa = config["mapa"]
			mapaAtual = []

		for i in range(len(mapa)):
			if len(config["mapaAtual"]) == 0:
				mapaAtual.append([])
			for j in range(len(mapa[i])):
				x = i
				y = j
				valor = mapa[x][y]
				cor = 2
				rotacao = 0
				if not (type(valor) is int) and len(valor) >= 2:
					tipo, rotacao = valor[0], valor[1]
					if len(valor) >= 3:
						cor = valor[len(valor) - 1]
				elif valor == -1:
					tipo = self.tilesDisponiveis[random.randint(0, len(self.tilesDisponiveis) - 1)]
					self.tilesDisponiveis.remove(tipo)
					cor = 1
				tile = config["tiles"]["tipos"][tipo]
				rotacao = random.randint(1, len(tile["rotacao"])) if rotacao == 0 else rotacao
				tileCarregado = Tiles(calcularPosicao(y, x), tipo, rotacao, cor - 1)

				if len(config["mapaAtual"]) == 0:
					mapaAtual[i].append([tipo, rotacao, cor])

				cenario.append(tileCarregado)

		if len(config["mapaAtual"]) == 0:
			config["mapaAtual"] = mapaAtual
		return pg.sprite.Group(cenario)

	def carregarTilesDisponiveis(self):
		tilesDisponiveis = []
		tipos = config["tiles"]["tipos"]

		for i in range(len(tipos)):
			quantidade = tipos[i]["quantidade"]
			for j in range(quantidade):
				tilesDisponiveis.append(i)

		return tilesDisponiveis

	def definirTileSobressalente(self):
		if config["sobressalente"]["valor"][0] == -1:
			config["sobressalente"]["valor"][0] = self.tilesDisponiveis[0]
		sobressalente = config["sobressalente"]
		valor = sobressalente["valor"]
		posicao = sobressalente["posicao"]
		tipo = valor[0]
		rotacao = valor[1]
		cor = valor[2]

		tile = Tiles(calcularPosicao(posicao[0], posicao[1]), tipo, rotacao, cor - 1)

		self.tileSobressalente = pg.sprite.Group([tile])

	def mudarRotacaoTileSobressalente(self):
		sobressalente = config["sobressalente"]
		valor = sobressalente["valor"]
		posicao = sobressalente["posicao"]
		tipo = valor[0]
		rotacao = valor[1]
		cor = valor[2]
		rotacaoTile = config["tiles"]["tipos"][tipo]["rotacao"]
		novaRotacao = rotacao + 1 if rotacao < len(rotacaoTile) else 1
		config["sobressalente"]["valor"][1] = novaRotacao

		tile = Tiles(calcularPosicao(posicao[0], posicao[1]), tipo, novaRotacao, cor - 1)

		self.tileSobressalente = pg.sprite.Group([tile])

	def inserirTile(self):
		posicao = calcularCoordenadas(self.posicaoMouse, True)
		checarInsercaoTile = validarCoordenadasInsercaoTile(posicao)

		if checarInsercaoTile:
			tamanhoMax = config["jogo"]["area"]

			varrerColuna = False
			varrerLinha = False
			coluna = range(len(config["mapaAtual"]))
			reverter = False

			x, y = posicao
			posicaoMovimentoProibido = list(calcularPosicao(x, y))
			movimentoProibido = config["movimentoProibido"]
			tamanho = movimentoProibido["tamanho"]
			margem = movimentoProibido["margem"]

			if posicao[0] == 0: # Esquerda para Direita
				x, y = posicao[1], tamanhoMax[1] - 1
				varrerLinha = True
				linha = range(len(config["mapaAtual"][x]))
				posicaoMovimentoProibido[0] += margem[0][0]
				posicaoMovimentoProibido[1] += margem[0][1]
			elif posicao[1] == 0: # Cima para Baixo
				x, y = tamanhoMax[0] - 1, posicao[0]
				varrerColuna = True
				posicaoMovimentoProibido[0] += margem[1][0]
				posicaoMovimentoProibido[1] += margem[1][1]
			elif posicao[0] == tamanhoMax[0] - 1: # Direita para Esquerda
				x, y = posicao[1], 0
				linha = reversed(range(len(config["mapaAtual"][x])))
				reverter = True
				varrerLinha = True
				posicaoMovimentoProibido[0] += margem[2][0]
				posicaoMovimentoProibido[1] += margem[2][1]
			elif posicao[1] == tamanhoMax[1] - 1: # Baixo para Cima
				x, y = 0, posicao[0]
				varrerColuna = True
				reverter = True
				posicaoMovimentoProibido[0] += margem[3][0]
				posicaoMovimentoProibido[1] += margem[3][1]

			self.definirMovimentoProibido(posicaoMovimentoProibido)

			mapaArmadilhas = config["armadilhas"]["mapa"]

			sobressalente = []
			for i in config["sobressalente"]["valor"]:
				sobressalente.append(i)

			armadilhaSobressalente = config["armadilhas"]["sobressalente"]

			novasPosicoes = []

			if varrerLinha:
				proximoTile = -1

				for i in linha:
					if proximoTile == -1:
						proximoTile = sobressalente
						tileArmadilha = armadilhaSobressalente

					proximoTileArmadilha = mapaArmadilhas[x][i]

					novoProximoTile = []
					for j in config["mapaAtual"][x][i]:
						novoProximoTile.append(j)

					config["mapaAtual"][x][i] = proximoTile
					config["armadilhas"]["mapa"][x][i] = tileArmadilha

					proximoTile = novoProximoTile
					tileArmadilha = proximoTileArmadilha

					jogadores = verificarJogadoresPosicao(i, x)
					if jogadores:
						for jogador in jogadores:
							if reverter:
								novaPosicao = i - 1 if i > 0 else 0
							else:
								novaPosicao = i + 1 if i < config["jogo"]["area"][0] - 1 else config["jogo"]["area"][1] - 1
							novasPosicoes.append([jogador, novaPosicao, x])

					if i == y:
						config["sobressalente"]["valor"] = novoProximoTile
						config["armadilhas"]["sobressalente"] = proximoTileArmadilha
			elif varrerColuna:
				proximoTile = -1

				if reverter:
					coluna = reversed(coluna)

				for i in coluna:
					linha = range(len(config["mapaAtual"][i]))
					for j in linha:
						if j == y:
							if proximoTile == -1:
								proximoTile = sobressalente
								tileArmadilha = armadilhaSobressalente

							proximoTileArmadilha = mapaArmadilhas[i][j]

							novoProximoTile = []
							for k in config["mapaAtual"][i][j]:
								novoProximoTile.append(k)

							config["mapaAtual"][i][j] = proximoTile
							config["armadilhas"]["mapa"][i][j] = tileArmadilha

							proximoTile = novoProximoTile
							tileArmadilha = proximoTileArmadilha

							jogadores = verificarJogadoresPosicao(j, i)
							if jogadores:
								for jogador in jogadores:
									if reverter:
										novaPosicao = i - 1 if i > 0 else 0
									else:
										novaPosicao = i + 1 if i < config["jogo"]["area"][1] - 1 else config["jogo"]["area"][1] - 1
									novasPosicoes.append([jogador, j, novaPosicao])

							if i == x:
								config["sobressalente"]["valor"] = novoProximoTile
								config["armadilhas"]["sobressalente"] = proximoTileArmadilha

			for i in novasPosicoes:
				config["jogadores"]["posicoes"][i[0]] = [i[1], i[2]]

			self.cenario = self.criarCenario()
			self.definirTileSobressalente()
			self.criarArmadilhas()
			self.definirJogadores()

	def definirSetaRotacionar(self):
		self.setaRotacionar = SetaRotacionar(self.imgSetaRotacionar - 1)
		self.setaRotacionarGroup = pg.sprite.Group([self.setaRotacionar])

	def definirAvancarTurno(self):
		self.avancarTurno = AvancarTurno(self.imgAvancarTurno - 1)
		self.avancarTurnoGroup = pg.sprite.Group([self.avancarTurno])

	def definirMovimentoProibido(self, posicao):
		self.movimentoProibido = pg.sprite.Group([MovimentoProibido(posicao)])

	def definirMapaArmadilhas(self):

		area = config["jogo"]["area"]

		mapa = []

		tilesDisponiveis = []

		config["armadilhas"]["sobressalente"] = 0

		for i in range(area[0]):
			mapa.append([])
			for j in range(area[1]):
				mapa[i].append(0)
				if i > 0 and j > 0 and i < area[0] - 1 and j < area[1] - 1 and ((i + 1) % 2 == 0 or (j + 1) % 2 == 0):
					tilesDisponiveis.append([i, j])

		for i in range(config["armadilhas"]["quantidade"]):
			tile = random.choice(tilesDisponiveis)
			tilesDisponiveis.remove(tile)
			x, y = tile
			mapa[x][y] = 1

		config["armadilhas"]["mapa"] = mapa

	def criarArmadilhas(self):
		armadilhas = []

		mapaArmadilhas = config["armadilhas"]["mapa"]

		for i in range(len(mapaArmadilhas)):
			for j in range(len(mapaArmadilhas[i])):
				if mapaArmadilhas[j][i] == 1:
					posicao = list(calcularPosicao(i, j))
					margem = config["armadilhas"]["margem"]
					posicao[0] += margem
					posicao[1] += margem
					armadilhas.append(Armadilhas(posicao))

		armadilhaSobressalente = config["armadilhas"]["sobressalente"]

		if armadilhaSobressalente == 1:
			x, y = config["sobressalente"]["posicao"]
			posicao = list(calcularPosicao(x, y))
			margem = config["armadilhas"]["margem"]
			posicao[0] += margem
			posicao[1] += margem
			armadilhas.append(Armadilhas(posicao))

		self.armadilhas = pg.sprite.Group(armadilhas)

	def mudarImgSetaRotacionar(self):
		self.imgSetaRotacionar = 2 if self.imgSetaRotacionar == 1 else 1
		self.definirSetaRotacionar()

	def mudarImgAvancarTurno(self):
		self.imgAvancarTurno = 2 if self.imgAvancarTurno == 1 else 1
		self.definirAvancarTurno()

	def event_loop(self):
		for event in pg.event.get():
			self.keys = pg.key.get_pressed()
			self.mouse = pg.mouse.get_pressed()
			self.posicaoMouse = pg.mouse.get_pos()
			x, y = self.posicaoMouse
			tempoAtual = pg.time.get_ticks()
			eventosLiberados = tempoAtual >= self.ultimoEvento

			checarPosicaoSetaRotacionar = self.setaRotacionar.rect.collidepoint(x, y)
			checarPosicaoAvancarTurno = self.avancarTurno.rect.collidepoint(x, y)

			if self.imgSetaRotacionar == 1 and checarPosicaoSetaRotacionar == 1:
				self.mudarImgSetaRotacionar()
				pg.mouse.set_cursor(*config["cursores"][1]["cursor"])
			elif self.imgSetaRotacionar == 2 and checarPosicaoSetaRotacionar == 0:
				self.mudarImgSetaRotacionar()
				pg.mouse.set_cursor(*config["cursores"][0]["cursor"])

			if self.imgAvancarTurno == 1 and checarPosicaoAvancarTurno == 1:
				self.mudarImgAvancarTurno()
				pg.mouse.set_cursor(*config["cursores"][1]["cursor"])
			elif self.imgAvancarTurno == 2 and checarPosicaoAvancarTurno == 0:
				self.mudarImgAvancarTurno()
				pg.mouse.set_cursor(*config["cursores"][0]["cursor"])

			if eventosLiberados:
				if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
					self.done = True
				elif event.type == pg.KEYDOWN and self.keys[pg.K_F5]:
					self.definirCenario()
					self.aplicarDelay = True
				elif not self.jogoFinalizado and self.mouse[0] == 1:
					if checarPosicaoSetaRotacionar == 1:
						self.mudarRotacaoTileSobressalente()
						self.aplicarDelay = True
						self.tempoDelay = 300
					elif checarPosicaoAvancarTurno == 1:
						self.mudarTurnoAtual()
						self.aplicarDelay = True
						self.tempoDelay = 300
					elif self.movimentarJogador():
						self.aplicarDelay = True
						self.tempoDelay = 500
					else:
						self.inserirTile()
						self.aplicarDelay = True
						self.tempoDelay = 500
				elif not self.jogoFinalizado and self.mouse[2] == 1:
					if self.mudarCorTile():
						self.aplicarDelay = True
						self.tempoDelay = 300

	def draw(self):
		self.level.fill(config["janela"]["corFundo"], self.viewport)
		self.cenario.draw(self.level)
		self.tileSobressalente.draw(self.level)
		self.setaRotacionarGroup.draw(self.level)
		self.avancarTurnoGroup.draw(self.level)
		if self.movimentoProibido:
			self.movimentoProibido.draw(self.level)
		self.armadilhas.draw(self.level)
		self.level.blit(self.textoTela, self.posicaoTextoTela)
		self.jogadores.draw(self.level)
		self.screen.blit(self.level, (0, 0), self.viewport)

	def display_fps(self):
		tituloJanela = "{} - FPS: {:.2f} - Jogador: {} - Turno: {}".format(config["janela"]["titulo"], self.clock.get_fps(), config["jogadores"]["nomes"][self.jogadorAtual], self.turnoAtual)
		pg.display.set_caption(tituloJanela)

	def main_loop(self):
		while not self.done:
			self.event_loop()
			self.draw()
			pg.display.update()
			self.clock.tick(self.fps)
			self.display_fps()
			if self.aplicarDelay:
				self.ultimoEvento = pg.time.get_ticks() + self.tempoDelay
				self.aplicarDelay = False

def main():
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pg.init()
	pg.display.set_caption(config["janela"]["titulo"])
	definirTamanhoJanela()
	pg.display.set_mode(config["janela"]["tamanho"])
	carregarCursores()
	carregarImagensTiles()
	carregarSetaRotacionar()
	carregarAvancarTurno()
	carregarMovimentoProibido()
	carregarArmadilha()
	Control().main_loop()
	pg.quit()
	os._exit(1)

if __name__ == "__main__":
	main()
