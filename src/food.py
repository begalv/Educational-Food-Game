import pygame
import random
import time

class food(object):

    def __init__(self, name, x, w=64, h=64):
        self.list = [['banana', pygame.image.load('images/banana.png')], ['carrot', pygame.image.load('images/carrot.png')], ['egg', pygame.image.load('images/egg.png')], ['chicken', pygame.image.load('images/chicken.png')], ['bread', pygame.image.load('images/bread.png')], ['ale', pygame.image.load('images/ale.png')], ['soda', pygame.image.load('images/soda.png')], ['milk', pygame.image.load('images/milk.png')], ['salad', pygame.image.load('images/salad.png')], ['chocolate', pygame.image.load('images/chocolate.png')], ['cereal', pygame.image.load('images/cereal.png')], ['peanut', pygame.image.load('images/peanut.png')], ['hazelnut', pygame.image.load('images/hazelnut.png')], ['oliveOil', pygame.image.load('images/oliveOil.png')], ['potato', pygame.image.load('images/potato.png')], ['eggplant', pygame.image.load('images/eggplant.png')], ['steaks', pygame.image.load('images/steak.png')], ['onion', pygame.image.load('images/onion.png')], ['flour', pygame.image.load('images/flour.png')], ['bean', pygame.image.load('images/bean.png')], ['orange', pygame.image.load('images/orange.png')], ['lemon', pygame.image.load('images/lemon.png')], ['apple', pygame.image.load('images/apple.png')], ['butter', pygame.image.load('images/butter.png')], ['nut', pygame.image.load('images/nut.png')], ['fish', pygame.image.load('images/fish.png')], ['pepper', pygame.image.load('images/pepper.png')], ['cheese', pygame.image.load('images/cheese.png')], ['grape', pygame.image.load('images/grape.png')]]
        self.name, self.img = name(self.list)
        self.x = x()
        self.w = w
        self.h = h


    def getFood(list): #gets a random name and a random image according to a list of names and images
        food = random.choice(list)
        foodName = food[0]
        foodImg = food[1]
        return foodName, foodImg

    def getX(): #gets a random x position on a certain area of the screen
        x = random.randint(64 , (700 - 64))
        return x

    def checkX(foods): #checks if a food's image is overlayin another food's image on screen, and, if it's true, gets another x position for the food
        for i in range(3):
            for fd in foods:
                index = foods.index(fd)
                foods.pop(index)
                for f in foods:
                    for i in range(fd.x, fd.x + fd.w +1):
                        if i == f.x or i == f.x + f.w:
                            fd.x = food.getX()
                foods.insert(index, fd)

    def draw(self, window, y): #draws a food object on screen
        img1 = pygame.transform.scale(self.img, (self.w,self.h))
        window.blit(img1, (self.x, y))

    def foodClicked(self, answer, points, chances, y): #checks if a food object is clicked and do what needs to be done if it is (more points or less chances)
        pos = pygame.mouse.get_pos()
        if (self.x + 64) >= pos[0] and pos[0] >= self.x and (y + 64) >= pos[1] and pos[1] >= y:
            alpha = 1
            self.img.fill((1, 1, 1, alpha), None, 0)
            if self.name in answer:
                points += 100
            elif self.name != 'del':
                chances -= 1
            return True, points, chances
        return False, points, chances

    def getQuestion(questType, answerType): #opens the question's file and the answer's file to create a list with all questions and its respectives answers. Then, returns a random question with its respectives answers
        quest = open("questions/{}.txt".format(questType), "r")
        answer = open("questions/{}.txt".format(answerType), "r")
        listQuest = quest.readlines()
        listAnswer = answer.readlines()
        listQA = []

        for q,a in zip(listQuest, listAnswer):
            listQA.append((q.strip()+a.strip()).split(";"))
        x = random.choice(listQA)
        question = x[0]
        answer = x[1:len(x)]
        return question, answer


class protein(food):

    def __init__(self, name, x, w=64, h=64):
        self.list = [['egg', pygame.image.load('images/egg.png')], ['milk', pygame.image.load('images/milk.png')], ['chicken', pygame.image.load('images/chicken.png')], ['peanut', pygame.image.load('images/peanut.png')], ['hazelnut', pygame.image.load('images/hazelnut.png')], ['steaks', pygame.image.load('images/steak.png')], ['bean', pygame.image.load('images/bean.png')], ['nut', pygame.image.load('images/nut.png')], ['fish', pygame.image.load('images/fish.png')], ['cheese', pygame.image.load('images/cheese.png')]]
        self.name, self.img = name(self.list)
        self.x = x()
        self.w = w
        self.h = h


class vitamin(food):

    def __init__(self, name, x, w=64, h=64):
        self.list = [['salad', pygame.image.load('images/salad.png')], ['banana', pygame.image.load('images/banana.png')], ['carrot', pygame.image.load('images/carrot.png')], ['eggplant', pygame.image.load('images/eggplant.png')], ['onion', pygame.image.load('images/onion.png')], ['orange', pygame.image.load('images/orange.png')], ['lemon', pygame.image.load('images/lemon.png')], ['apple', pygame.image.load('images/apple.png')], ['pepper', pygame.image.load('images/pepper.png')], ['grape', pygame.image.load('images/grape.png')]]
        self.name, self.img = name(self.list)
        self.x = x()
        self.w = w
        self.h = h

class carbs(food):

    def __init__(self, name, x, w=64, h=64):
        self.list = [['bread', pygame.image.load('images/bread.png')], ['ale', pygame.image.load('images/ale.png')], ['soda', pygame.image.load('images/soda.png')], ['cereal', pygame.image.load('images/cereal.png')], ['chocolate', pygame.image.load('images/chocolate.png')], ['oliveOil', pygame.image.load('images/oliveOil.png')], ['potato', pygame.image.load('images/potato.png')], ['flour', pygame.image.load('images/flour.png')], ['butter', pygame.image.load('images/butter.png')]]
        self.name, self.img = name(self.list)
        self.x = x()
        self.w = w
        self.h = h
