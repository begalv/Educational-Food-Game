import pygame
import random
import time

class alimento:

    def __init__(self, nome, x):
        listaAli = [['banana', pygame.image.load('imagens/banana.png')], ['cenoura', pygame.image.load('imagens/cenoura.png')], ['ovo', pygame.image.load('imagens/ovo.png')], ['frango', pygame.image.load('imagens/coxa.png')], ['pão', pygame.image.load('imagens/pão.png')], ['cerveja', pygame.image.load('imagens/breja.png')], ['refrigerante', pygame.image.load('imagens/coca.png')], ['leite', pygame.image.load('imagens/leite.png')], ['salada', pygame.image.load('imagens/salada.png')], ['chocolate', pygame.image.load('imagens/chocolate.png')], ['cereal', pygame.image.load('imagens/cereal.png')], ['amendoim', pygame.image.load('imagens/amendoim.png')], ['avelã', pygame.image.load('imagens/avelã.png')], ['azeite', pygame.image.load('imagens/azeite.png')], ['batata', pygame.image.load('imagens/batata.png')], ['beringela', pygame.image.load('imagens/berinjela.png')], ['carnes', pygame.image.load('imagens/bife.png')], ['cebola', pygame.image.load('imagens/cebola.png')], ['farinha', pygame.image.load('imagens/farinha.png')], ['feijão', pygame.image.load('imagens/feijão.png')], ['laranja', pygame.image.load('imagens/laranja.png')], ['limão', pygame.image.load('imagens/limão.png')], ['maçã', pygame.image.load('imagens/maçã.png')], ['manteiga', pygame.image.load('imagens/mantega.png')], ['nozes', pygame.image.load('imagens/nozes.png')], ['peixes', pygame.image.load('imagens/peixe.png')], ['pimentão', pygame.image.load('imagens/pimentão.png')], ['queijo', pygame.image.load('imagens/queijo.png')], ['uva', pygame.image.load('imagens/uva.png')]]
        self.nome, self.img = nome(listaAli)
        self.x = x()
        self.w = 64
        self.h = 64


    def getAli(lista):
        ali = random.choice(lista)
        nomeAli = ali[0]
        imgAli = ali[1]
        return nomeAli, imgAli

    def getX():
        x = random.randint(64 , (700 - 64))
        return x

    def draw(window, img, x, y, scale):
        img1 = pygame.transform.scale(img, (scale,scale))
        window.blit(img1, (x, y))

    def getQuestion(tipoP, tipoR):
        perg = open("perguntas/{}.txt".format(tipoP), "r")
        resp = open("perguntas/{}.txt".format(tipoR), "r")
        listaPerg = perg.readlines()
        listaResp = resp.readlines()
        listaPR = []

        for p,r in zip(listaPerg, listaResp):
            listaPR.append((p.strip()+r.strip()).split(";"))
        x = random.choice(listaPR)
        question = x[0]
        answer = x[1:len(x)]
        return question, answer


    class construtores:

        def __init__(self, nome, x):
            listaConstru = [['ovo', pygame.image.load('imagens/ovo.png')], ['leite', pygame.image.load('imagens/leite.png')], ['frango', pygame.image.load('imagens/coxa.png')], ['amendoim', pygame.image.load('imagens/amendoim.png')], ['avelã', pygame.image.load('imagens/avelã.png')], ['carnes', pygame.image.load('imagens/bife.png')], ['feijão', pygame.image.load('imagens/feijão.png')], ['nozes', pygame.image.load('imagens/nozes.png')], ['peixes', pygame.image.load('imagens/peixe.png')], ['queijo', pygame.image.load('imagens/queijo.png')]]
            self.nome, self.img = nome(listaConstru)
            self.x = x()
            self.w = 64
            self.h = 64

    class reguladores:

        def __init__(self, nome, x):
            listaRegu = [['salada', pygame.image.load('imagens/salada.png')], ['banana', pygame.image.load('imagens/banana.png')], ['cenoura', pygame.image.load('imagens/cenoura.png')], ['beringela', pygame.image.load('imagens/berinjela.png')], ['cebola', pygame.image.load('imagens/cebola.png')], ['laranja', pygame.image.load('imagens/laranja.png')], ['limão', pygame.image.load('imagens/limão.png')], ['maçã', pygame.image.load('imagens/maçã.png')], ['imagens/pimentão.png'], ['uva', pygame.image.load('imagens/uva.png')]]
            self.nome, self.img = nome(listaRegu)
            self.x = x()
            self.w = 64
            self.h = 64


    class energeticos:

        def __init__(self, nome, x):
            listaEnerg = [['pão', pygame.image.load('imagens/pão.png')], ['cerveja', pygame.image.load('imagens/breja.png')], ['refrigerante', pygame.image.load('imagens/coca.png')], ['cereal', pygame.image.load('imagens/cereal.png')], ['chocolate', pygame.image.load('imagens/chocolate.png')], ['azeite', pygame.image.load('imagens/azeite.png')], ['batata', pygame.image.load('imagens/batata.png')], ['farinha', pygame.image.load('imagens/farinha.png')], ['manteiga', pygame.image.load('imagens/mantega.png')]]
            self.nome, self.img = nome(listaEnerg)
            self.x = x()
            self.w = 64
            self.h = 64
