import pygame
import random
from food import *
from inputBox import inputBox

pygame.init()

win = pygame.display.set_mode((720, 480))
pygame.display.set_caption("A Food Game")
disWidth = 720
disHeight = 480

globalFont = pygame.font.SysFont("freesansbold.ft", 20)
vel = 1

#global variables
theme = ""
question = ""
answer = []
y = 120
points = 0
chances = 3
rank = ''
name = ''

def textObjects(text, font, color=(0,0,0)): #creates text Objects
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def getTheme(): #gets a random theme of 3 possible themes
    global question
    global answer
    global theme
    r = random.randint(1,3)
    if r == 1:
        theme = "Protein"
    elif r == 2:
        theme = "Vitamin"
    else:
        theme = "Carbs"

def button(msg, x, y, w, h, action=None): #creates a button on the screen that makes an action when pressed
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    isClicked = False

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, (0, 255, 0), (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
            isClicked = True

    else:
        pygame.draw.rect(win, (0, 220, 0), (x,y,w,h))
        isClicked = False

    textSurf, textRect = textObjects(msg, globalFont)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    win.blit(textSurf, textRect)
    return isClicked

def gameIntro(): #first screen of the game. Contains the player's name input box and two buttons, one for start the game and one for access the ranking screen
    global name
    iB1 = inputBox(disWidth/2-70,disHeight/2+16,140,32,10,pygame.K_SPACE, 'Name:')
    text = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            text = iB1.handleEvent(event)


        win.fill((192,192,192))
        if text != 'Name:':
            name = text

        largeText = pygame.font.SysFont("comicsansms", 90)
        titleSurf, titleRect = textObjects("A FOOD GAME", largeText, (140,120,83))
        titleRect.center = (disWidth/2, (disHeight/4)-25)
        win.blit(titleSurf, titleRect)

        iB1.draw(win)

        start = button("START", (disWidth+200)/2, (disHeight - 155), 100, 50, preGame if name != '' else None)
        ranking = button("RANKING", (disWidth-400)/2, (disHeight - 155), 100, 50, gameRanking)

        pygame.display.update()

        if start == True or ranking == True:
            break

def saveRank(): #save a variable with the player's name, player's points and theme (ranking data) on a txt file
    global rank
    global points
    global name
    rank = '{};{};{}'.format(points,name,theme)
    ranking = open('ranking/ranking.txt','a')
    ranking.write(rank + '\n')
    ranking.close()
    gameIntro()

def getRank(): #transform the txt file with the ranking data in a list
    ranking = open('ranking/ranking.txt', 'r')
    list = ranking.readlines()
    rankingList = []
    for r in list:
        rankingList.append(r.strip().split(';'))
    rankingList.sort(reverse=True)
    if len(rankingList) > 15:
        del(rankingList[15:])
    return rankingList

def gameRanking(): #displays a table on screen with the ranking data
    rankingList = getRank()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((192,192,192))
        for count in range(1, len(rankingList)+1):
            rankPointsSurf, rankPointsRect = textObjects(rankingList[count-1][0], globalFont)
            rankPointsRect.center = (60, 60+20*count)
            rankNameSurf, rankNameRect = textObjects(rankingList[count-1][1], globalFont)
            rankNameRect.center = (disWidth/2-22, 60+20*count)
            rankThemeSurf, rankThemeRect = textObjects(rankingList[count-1][2], globalFont)
            rankThemeRect.center = (638, 60+20*count)
            win.blit(rankPointsSurf, rankPointsRect)
            win.blit(rankNameSurf, rankNameRect)
            win.blit(rankThemeSurf, rankThemeRect)
            pygame.draw.rect(win, (0, 0, 0), (45,50+20*count,640,19),2)

        strgPointsFont = pygame.font.SysFont("comicsansms", 32)
        strgPointsSurf, strgPointsRect = textObjects('Points', strgPointsFont, (140,120,83))
        strgPointsRect.center = (60, 30)
        strgNameSurf, strgNameRect = textObjects('Name', strgPointsFont, (140,120,83))
        strgNameRect.center = (disWidth/2 -22, 30)
        strgThemeSurf, strgThemeRect = textObjects('Theme', strgPointsFont, (140,120,83))
        strgThemeRect.center = (638, 30)
        win.blit(strgPointsSurf, strgPointsRect)
        win.blit(strgNameSurf, strgNameRect)
        win.blit(strgThemeSurf, strgThemeRect)

        back = button("BACK", (disWidth/2)-65, 400, 100, 50, gameIntro)

        pygame.display.update()

def preGame(): #screen with a button to call getTheme function and display the theme
    global theme
    global chances
    global points
    theme = " "
    chances = 3
    points = 0
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((192,192,192))

        d = button("DRAW", (disWidth - 100)/2, disHeight - 150, 100, 50, getTheme)

        pygame.draw.rect(win, (140,120,83), (((disWidth/2)-300),((disHeight/4)-90), 600, 180))
        largeText = pygame.font.SysFont("comicsansms", 90)
        TextSurf, TextRect = textObjects(theme, largeText)
        TextRect.center = ((disWidth/2), (disHeight/4))
        win.blit(TextSurf,TextRect)

        pygame.display.update()

        if d == True:
            for i in range(3,0,-1):
                TextSurf, TextRect = textObjects(str(i), globalFont)
                TextRect.center = ((disWidth/2), 250)
                blankSurf = globalFont.render(str(i), True, (255, 255, 255))
                win.blit(TextSurf, TextRect)
                pygame.display.update()
                pygame.time.delay(700)
                win.blit(blankSurf, TextRect)
                pygame.display.update()
            gameManager()
            break
        else:
            continue

def gameOver(): #game over screen that shows the player's score and two buttons, one for return to the first screen of the game and one for play again
    fail = True
    while fail:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((192,192,192))

        y = button("YES", (disWidth/2 - 150), (disHeight - 150), 100, 50, preGame)
        n = button("NO", (disWidth/2 + 50), (disHeight - 150), 100, 50, saveRank)

        if y or n == True:
            break

        pygame.draw.rect(win, (140,120,83), ((disWidth/2 - 180), (disHeight/2 - 170 ), 360, 200))
        largeText = pygame.font.SysFont("comicsansms", 55)
        smallText = pygame.font.SysFont("freesansbold.ft", 25)
        TextSurf, TextRect = textObjects('GAME OVER', largeText)
        TextSurf1, TextRect1 = textObjects('Do you want to play again?', smallText)
        TextSurf2, TextRect2 = textObjects("Your score: {}".format(points), smallText)
        TextRect.center = ((disWidth/2), (disHeight/2 - 100))
        TextRect1.center = ((disWidth/2), (disHeight/2 - 10))
        TextRect2.center = ((disWidth/2), (disHeight/2 - 40))
        win.blit(TextSurf,TextRect)
        win.blit(TextSurf1, TextRect1)
        win.blit(TextSurf2, TextRect2)


        pygame.display.update()

def gameDisplay(foods): #checks if each current food object is clicked and displays each of them on screen. Also displays current score, current question and chances left
    global y
    global points
    global chances
    for y in range(110, 480, vel):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for fd in foods:
                    click, points, chances = fd.foodClicked(answer,points,chances,y)
                    if click == True:
                        fd.name = 'del'

        win.fill((192,192,192))

        pygame.draw.rect(win, (140,120,83), (((disWidth/2)-350),(disHeight-470), 700, 50))
        questionFont = pygame.font.SysFont("comicsansms", 20)
        TextSurf, TextRect = textObjects(question, questionFont)
        TextRect.center = ((disWidth/2), ((disHeight - 445)))
        win.blit(TextSurf,TextRect)

        pygame.draw.rect(win, (211,211,211), (((disWidth/2)-350),(disHeight-375), 700, 390))
        win.blit(pygame.image.load('images/star.png'), (((disWidth/2)-350), (disHeight-415)))
        pointsSurf, pointsRect = textObjects('{}'.format(points), questionFont)
        pointsRect.center = (((disWidth/2)-290), (disHeight - 399))
        win.blit(pointsSurf, pointsRect)

        win.blit(pygame.image.load('images/heart.png'), (((disWidth/2)-250), (disHeight-415)))
        chancesSurf, chancesRect = textObjects('{}'.format(chances), questionFont)
        chancesRect.center = (((disWidth/2)-190), (disHeight - 399))
        win.blit(chancesSurf, chancesRect)

        for fd in foods:
            fd.draw(win, y)

        pygame.time.delay(10)
        pygame.display.update()

        if chances == 0 or all(fd.name == 'del' for fd in foods):
            break

def getNFoods(n, joker): #gets n food objects including a joker (type of food that is the right answer for the current question) and stores them on a list
    foods = []
    for i in range(1,n):
        foods.append(food())
    foods.append(joker())
    return foods

def gameManager(): #calls the getNFoods function according to drawed theme and the questions/answers for each round of the game. Also calls a funcion that checks if any food's x are the same
    global question
    global answer
    game = True
    while game:
        pygame.time.delay(300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if theme == 'Protein':
            foods = getNFoods(4, protein)
            question, answer = food.getQuestion('proteinQuest', 'proteinAnswer')
        elif theme == 'Vitamin':
            foods = getNFoods(4, vitamin)
            question, answer = food.getQuestion('vitaminQuest', 'vitaminAnswer')
        elif theme == 'Carbs':
            foods = getNFoods(4, carbs)
            question, answer = food.getQuestion('carbsQuest', 'carbsAnswer')

        food.checkX(foods)

        gameDisplay(foods)
        if chances == 0:
            gameOver()
            break
        pygame.display.update()

if __name__ == '__main__':
    gameIntro()
    gameOver()
