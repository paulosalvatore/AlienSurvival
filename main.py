
import pygame as pg, os, sys, random

config = {
	"janela": {
		"titulo": "Jogo",
		"tamanho": [0, 0],
		"corFundo": (255, 255, 255),
		"cores": [
			(60, 85, 17),
			(232, 230, 83),
			(221, 30, 30),
			(255, 156, 0),
			(0, 0, 255),
			(112, 12, 162),
			(0, 0, 0)
		]
	},
	"jogo": {
		"area": (11, 11),
		"areaJanela": (11, 11),
		"areaJanelaExtra": (4, 0),
		"borda": 64
	},
	"tiles": {
		"tamanho": 64,
		"tipos": {
			0: {
				"nomeArquivo": "Tile1",
				"block": False,
				"quantidade": 27,
				"rotacao": [1, 1],
				"arquivos": []
			},
			1: {
				"nomeArquivo": "Tile2",
				"block": False,
				"quantidade": 27,
				"rotacao": [1, 1, 1, 1],
				"arquivos": []
			},
			2: {
				"nomeArquivo": "Tile3",
				"block": False,
				"quantidade": 27,
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
		"tamanho": 32,
		"margem": 16,
		"numero": 4,
		"posicoes": [],
		"arquivos": [],
		"cores": [
			(0, 0, 0),
			(111, 233, 234),
			(255, 78, 236),
			(159, 159, 159)
		],
		"nomes": ("Preto", "Azul", "Rosa", "Cinza")
	},
	"mapa": [
		[[1, 2, 3], -1, [2, 1, 4], -1, [1, 1], -1, [1, 2], -1, [2, 1, 4], -1, [1, 1, 3]],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[[2, 2, 4], -1, [2, 4, 6], -1, [2, 1, 5], -1, [2, 2, 5], -1, [2, 3, 6], -1, [2, 4, 4]],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[[1, 3], -1, [2, 3, 5], -1, [2, 2, 6], -1, [2, 1, 6], -1, [3, 1, 5], -1, [1, 4]],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[[1, 2], -1, [3, 1, 5], -1, [2, 3, 6], -1, [2, 4, 6], -1, [2, 1, 5], -1, [1, 1]],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[[2, 2, 4], -1, [2, 1, 6], -1, [2, 4, 5], -1, [2, 3, 5], -1, [2, 2, 6], -1, [2, 4, 4]],
		[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		[[1, 3, 3], -1, [2, 3, 4], -1, [1, 4], -1, [1, 3], -1, [2, 3, 4], -1, [1, 4, 3]]
	],
	"mapaAtual": [],
	"sobressalente": {
		"posicao": [13, 5],
		"valor": [-1, 1, 1]
	},
	"setaRotacionar": {
		"posicao": [896 + 8, 448 + 8],
		"tamanho": [48, 48],
		"arquivo": ""
	}
}

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
	nomeArquivo = "setaRotacionar"
	setaRotacionar = config["setaRotacionar"]
	tamanho = setaRotacionar["tamanho"]
	imagem = pg.image.load(os.path.join(sys.path[0], "imagens/"+nomeArquivo+".png")).convert_alpha()
	config["setaRotacionar"]["arquivo"] = pg.transform.scale(imagem, (tamanho[0], tamanho[1]))

def carregarJogadores():
	jogadores = config["jogadores"]
	tamanho = jogadores["tamanho"]
	numero = jogadores["numero"]

	for i in range(numero):
		imagem = pg.Surface((tamanho, tamanho)).convert_alpha()
		imagem.fill(config["jogadores"]["cores"][i])
		x = 0 if i % 2 == 0 else config["jogo"]["area"][0] - 1
		y = 0 if i < 2 else config["jogo"]["area"][1] - 1
		config["jogadores"]["arquivos"].append(imagem)
		config["jogadores"]["posicoes"].insert(i, (y, x))

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
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		setaRotacionar = config["setaRotacionar"]
		tamanho = setaRotacionar["tamanho"]
		posicao = setaRotacionar["posicao"]
		imagem = pg.Surface((tamanho[0], tamanho[1])).convert_alpha()
		imagem.fill(config["janela"]["corFundo"])
		imagem.blit(setaRotacionar["arquivo"], (0, 0))
		self.image = imagem
		self.rect = self.image.get_rect(topleft = posicao)
		self.mask = pg.mask.from_surface(self.image)

class Control(object):
	def __init__(self):
		self.screen = pg.display.get_surface()
		self.clock = pg.time.Clock()
		self.fps = 60.0
		self.done = False

		self.keys = pg.key.get_pressed()
		self.mouse = pg.mouse.get_pressed()
		self.posicaoMouse = pg.mouse.get_pos()

		self.aplicarDelay = False
		self.tempoDelay = 500

		self.definirJogadores()
		self.jogadorAtual = 0

		self.definirCenario()

		self.turnoAtual = 1

		tamanhoJanela = config["janela"]["tamanho"]
		self.level = pg.Surface((tamanhoJanela[0], tamanhoJanela[1])).convert()
		self.level_rect = self.level.get_rect()
		self.viewport = self.screen.get_rect(top = self.level_rect.top)

	def mudarCorTile(self):
		posicao = calcularCoordenadas(self.posicaoMouse)

		if posicao:
			tile = config["mapaAtual"][posicao[1]][posicao[0]]

			if not (type(tile) is int) and len(tile) >= 2:
				cor = 2 if len(tile) == 2 else tile[2]
				novaCor = cor if len(tile) == 4 and tile[3] == 7 else 7

				config["mapaAtual"][posicao[1]][posicao[0]] = [tile[0], tile[1], cor, novaCor]
				self.cenario = self.criarCenario()

		return posicao

	def movimentarJogador(self):
		posicao = calcularCoordenadas(self.posicaoMouse)

		if posicao:
			config["jogadores"]["posicoes"][self.jogadorAtual] = posicao

			if self.jogadorAtual < config["jogadores"]["numero"] - 1:
				self.jogadorAtual = self.jogadorAtual + 1
			else:
				self.jogadorAtual = 0
				self.turnoAtual = self.turnoAtual + 1

			self.definirJogadores()

		return posicao

	def definirJogadores(self):
		jogadores = []

		for i in range(config["jogadores"]["numero"]):
			posicao = config["jogadores"]["posicoes"][i]
			posicaoCalculada = calcularPosicao(posicao[0], posicao[1])
			margem = config["jogadores"]["margem"]
			jogador = Jogadores(i, (posicaoCalculada[0] + margem, posicaoCalculada[1] + margem))
			jogadores.append(jogador)

		self.jogadores = pg.sprite.Group(jogadores)

	def definirCenario(self):
		self.jogadorAtual = 0
		self.turnoAtual = 1
		config["mapaAtual"] = []
		self.tilesDisponiveis = self.carregarTilesDisponiveis()
		self.cenario = self.criarCenario()
		self.definirTileSobressalente()
		self.definirSetaRotacionar()
		carregarJogadores()
		self.jogadores = []
		self.definirJogadores()

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

			if posicao[0] == 0:
				x, y = posicao[1], tamanhoMax[1] - 1
				varrerLinha = True
				linha = range(len(config["mapaAtual"][x]))
			elif posicao[1] == 0:
				x, y = tamanhoMax[0] - 1, posicao[0]
				varrerColuna = True
			elif posicao[0] == tamanhoMax[0] - 1:
				x, y = posicao[1], 0
				linha = reversed(range(len(config["mapaAtual"][x])))
				varrerLinha = True
			elif posicao[1] == tamanhoMax[1] - 1:
				x, y = 0, posicao[0]
				varrerColuna = True
				reverter = True

			sobressalente = []
			for i in config["sobressalente"]["valor"]:
				sobressalente.append(i)

			if varrerLinha:
				proximoTile = -1
				for i in linha:
					if proximoTile == -1:
						proximoTile = sobressalente

					novoProximoTile = []
					for j in config["mapaAtual"][x][i]:
						novoProximoTile.append(j)

					config["mapaAtual"][x][i] = proximoTile

					proximoTile = novoProximoTile

					if i == y:
						config["sobressalente"]["valor"] = novoProximoTile
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

							novoProximoTile = []
							for k in config["mapaAtual"][i][j]:
								novoProximoTile.append(k)

							config["mapaAtual"][i][j] = proximoTile

							proximoTile = novoProximoTile

							if i == x:
								config["sobressalente"]["valor"] = novoProximoTile

			self.cenario = self.criarCenario()
			self.definirTileSobressalente()

	def definirSetaRotacionar(self):
		self.setaRotacionar = SetaRotacionar()
		self.setaRotacionarGroup = pg.sprite.Group([self.setaRotacionar])

	def event_loop(self):
		for event in pg.event.get():
			self.keys = pg.key.get_pressed()
			self.mouse = pg.mouse.get_pressed()
			self.posicaoMouse = pg.mouse.get_pos()
			if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
				self.done = True
			elif event.type == pg.KEYDOWN and self.keys[pg.K_F5]:
				self.definirCenario()
				self.aplicarDelay = True
			elif self.mouse[0] == 1:
				x, y = self.posicaoMouse
				checarPosicaoSetaRotacionar = self.setaRotacionar.rect.collidepoint(x, y)
				if checarPosicaoSetaRotacionar == 1:
					self.mudarRotacaoTileSobressalente()
					self.aplicarDelay = True
					self.tempoDelay = 300
				elif self.movimentarJogador():
					self.aplicarDelay = True
					self.tempoDelay = 500
				else:
					self.inserirTile()
					self.aplicarDelay = True
					self.tempoDelay = 500
			elif self.mouse[2] == 1:
				if self.mudarCorTile():
					self.aplicarDelay = True
					self.tempoDelay = 300

	def draw(self):
		self.level.fill(config["janela"]["corFundo"], self.viewport)
		self.cenario.draw(self.level)
		self.tileSobressalente.draw(self.level)
		self.setaRotacionarGroup.draw(self.level)
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
				pg.time.wait(self.tempoDelay)
				self.aplicarDelay = False

def main():
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pg.init()
	pg.display.set_caption(config["janela"]["titulo"])
	definirTamanhoJanela()
	pg.display.set_mode(config["janela"]["tamanho"])
	carregarImagensTiles()
	carregarSetaRotacionar()
	carregarJogadores()
	Control().main_loop()
	pg.quit()
	os._exit(1)

if __name__ == "__main__":
	main()
