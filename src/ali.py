import pygame
import random
import time

class alimento(object):

    def __init__(self, nome, x, w=64, h=64):
        self.lista = [['banana', pygame.image.load('imagens/banana.png')], ['cenoura', pygame.image.load('imagens/cenoura.png')], ['ovo', pygame.image.load('imagens/ovo.png')], ['frango', pygame.image.load('imagens/coxa.png')], ['pão', pygame.image.load('imagens/pão.png')], ['cerveja', pygame.image.load('imagens/breja.png')], ['refrigerante', pygame.image.load('imagens/coca.png')], ['leite', pygame.image.load('imagens/leite.png')], ['salada', pygame.image.load('imagens/salada.png')], ['chocolate', pygame.image.load('imagens/chocolate.png')], ['cereal', pygame.image.load('imagens/cereal.png')], ['amendoim', pygame.image.load('imagens/amendoim.png')], ['avelã', pygame.image.load('imagens/avelã.png')], ['azeite', pygame.image.load('imagens/azeite.png')], ['batata', pygame.image.load('imagens/batata.png')], ['beringela', pygame.image.load('imagens/berinjela.png')], ['carnes', pygame.image.load('imagens/bife.png')], ['cebola', pygame.image.load('imagens/cebola.png')], ['farinha', pygame.image.load('imagens/farinha.png')], ['feijão', pygame.image.load('imagens/feijão.png')], ['laranja', pygame.image.load('imagens/laranja.png')], ['limão', pygame.image.load('imagens/limão.png')], ['maçã', pygame.image.load('imagens/maçã.png')], ['manteiga', pygame.image.load('imagens/mantega.png')], ['nozes', pygame.image.load('imagens/nozes.png')], ['peixes', pygame.image.load('imagens/peixe.png')], ['pimentão', pygame.image.load('imagens/pimentão.png')], ['queijo', pygame.image.load('imagens/queijo.png')], ['uva', pygame.image.load('imagens/uva.png')]]
        self.nome, self.img = nome(self.lista)
        self.x = x()
        self.w = w
        self.h = h


    def getAli(lista):
        ali = random.choice(lista)
        nomeAli = ali[0]
        imgAli = ali[1]
        return nomeAli, imgAli

    def getX():
        x = random.randint(64 , (700 - 64))
        return x

    def checkX(foods):
        for i in range(3):
            for food in foods:
                index = foods.index(food)
                foods.pop(index)
                for f in foods:
                    for i in range(food.x, food.x + food.w +1):
                        if i == f.x or i == f.x + f.w:
                            food.x = alimento.getX()
                foods.insert(index, food)

    def draw(self, window, y):
        img1 = pygame.transform.scale(self.img, (self.w,self.h))
        window.blit(img1, (self.x, y))

    def foodClicked(self, answer, pontos, chances, y):
        pos = pygame.mouse.get_pos()
        if (self.x + 64) >= pos[0] and pos[0] >= self.x and (y + 64) >= pos[1] and pos[1] >= y: #se o mouse esta dentro da imagem
            alpha = 1
            self.img.fill((1, 1, 1, alpha), None, 0)
            if self.nome in answer:
                pontos += 100
            elif self.nome != 'del':
                chances -= 1
            return True, pontos, chances
        return False, pontos, chances

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


class construtores(alimento):

    def __init__(self, nome, x, w=64, h=64):
        self.lista = [['ovo', pygame.image.load('imagens/ovo.png')], ['leite', pygame.image.load('imagens/leite.png')], ['frango', pygame.image.load('imagens/coxa.png')], ['amendoim', pygame.image.load('imagens/amendoim.png')], ['avelã', pygame.image.load('imagens/avelã.png')], ['carnes', pygame.image.load('imagens/bife.png')], ['feijão', pygame.image.load('imagens/feijão.png')], ['nozes', pygame.image.load('imagens/nozes.png')], ['peixes', pygame.image.load('imagens/peixe.png')], ['queijo', pygame.image.load('imagens/queijo.png')]]
        self.nome, self.img = nome(self.lista)
        self.x = x()
        self.w = w
        self.h = h


class reguladores(alimento):

    def __init__(self, nome, x, w=64, h=64):
        self.lista = [['salada', pygame.image.load('imagens/salada.png')], ['banana', pygame.image.load('imagens/banana.png')], ['cenoura', pygame.image.load('imagens/cenoura.png')], ['beringela', pygame.image.load('imagens/berinjela.png')], ['cebola', pygame.image.load('imagens/cebola.png')], ['laranja', pygame.image.load('imagens/laranja.png')], ['limão', pygame.image.load('imagens/limão.png')], ['maçã', pygame.image.load('imagens/maçã.png')], ['pimentão', pygame.image.load('imagens/pimentão.png')], ['uva', pygame.image.load('imagens/uva.png')]]
        self.nome, self.img = nome(self.lista)
        self.x = x()
        self.w = w
        self.h = h

class energeticos(alimento):

    def __init__(self, nome, x, w=64, h=64):
        self.lista = [['pão', pygame.image.load('imagens/pão.png')], ['cerveja', pygame.image.load('imagens/breja.png')], ['refrigerante', pygame.image.load('imagens/coca.png')], ['cereal', pygame.image.load('imagens/cereal.png')], ['chocolate', pygame.image.load('imagens/chocolate.png')], ['azeite', pygame.image.load('imagens/azeite.png')], ['batata', pygame.image.load('imagens/batata.png')], ['farinha', pygame.image.load('imagens/farinha.png')], ['manteiga', pygame.image.load('imagens/mantega.png')]]
        self.nome, self.img = nome(self.lista)
        self.x = x()
        self.w = w
        self.h = h
