import pygame
import random
from alimento import alimento

pygame.init()

win = pygame.display.set_mode((720, 480))
disWidth = 720
disHeight = 480

globalFont = pygame.font.SysFont("freesansbold.ft", 20)
theme = ""
question = ""
answer = []
y = 120
vel = 1
pontos = 0
chances = 3
rank = ''
name = ''

def textObjects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def getTheme():
    global question
    global answer
    global theme
    r = random.randint(1,3)
    if r == 1:
        theme = "Construtores"
        question, answer = alimento.getQuestion('construPerg', 'construResp')
    elif r == 2:
        theme = "Reguladores"
        question, answer = alimento.getQuestion('reguPerg', 'reguResp')
    else:
        theme = "Energeticos"
        question, answer = alimento.getQuestion('energPerg', 'energResp')

def button(msg, x, y, w, h, action=None):
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

def gameName():
    global name
    global rank
    inputBox = pygame.Rect(disWidth/2 -70, disHeight/2 +16, 140, 32)
    colorInactive = (220,220,220)
    colorActive = (211,211,211)
    color = colorInactive
    active = False
    text = 'Name:'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputBox.collidepoint(event.pos):
                    active = not active
                    color = colorActive
                else:
                    active = False
                    color = colorInactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if text == 'Name:':
                        text = ''
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) <= 15:
                            if event.key != pygame.K_SPACE and event.key != pygame.K_RETURN:
                                text += event.unicode
        if text != 'Name:':
            name = text
        win.fill((192,192,192))

        largeText = pygame.font.SysFont("comicsansms", 90)
        titleSurf, titleRect = textObjects("A FOOD GAME", largeText)
        titleRect.center = (disWidth/2, (disHeight/4)-25)
        win.blit(titleSurf, titleRect)

        textSurf, textRect = textObjects(text, globalFont)
        pygame.draw.rect(win, color, inputBox)
        win.blit(textSurf, (inputBox.x+5, inputBox.y+5))

        start = button("START", (disWidth+200)/2, (disHeight - 155), 100, 50, gameIntro if name != '' else None)
        ranking = button("RANKING", (disWidth-400)/2, (disHeight - 155), 100, 50, gameRanking)
        pygame.display.update()

        if start == True or ranking == True:
            break

def saveRank():
    global rank
    rank = '{};{};{}'.format(pontos,name,theme)
    ranking = open('ranking/ranking.txt','a')
    ranking.write(rank + '\n')
    ranking.close()
    quit()

def getRank():
    ranking = open('ranking/ranking.txt', 'r')
    list = ranking.readlines()
    rankingList = []
    for r in list:
        rankingList.append(r.strip().split(';'))
    print(rankingList)
    return rankingList

def gameRanking():
    rankingList = getRank()
    rankingList.sort(reverse=True)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for count in range(1, len(rankingList)+1):
            joined = (21*'...').join(rankingList[count-1])
            rankSurf, rankRect = textObjects(joined, globalFont)
            rankRect.center = (disWidth/2, 20*count)
            win.blit(rankSurf, rankRect)
        pygame.display.update()

        win.fill((192,192,192))



def gameIntro():
    global theme
    global chances
    global pontos
    theme = " "
    chances = 3
    pontos = 0
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((192,192,192))

        b = button("SORTEAR", (disWidth - 100)/2, disHeight - 150, 100, 50, getTheme)

        pygame.draw.rect(win, (140,120,83), (((disWidth/2)-300),((disHeight/4)-90), 600, 180))
        largeText = pygame.font.SysFont("comicsansms", 90)
        TextSurf, TextRect = textObjects(theme, largeText)
        TextRect.center = ((disWidth/2), (disHeight/4))
        win.blit(TextSurf,TextRect)

        pygame.display.update()

        if b == True:
            for i in range(3,0,-1):
                TextSurf, TextRect = textObjects(str(i), globalFont)
                TextRect.center = ((disWidth/2), 250)
                blankSurf = globalFont.render(str(i), True, (255, 255, 255))
                win.blit(TextSurf, TextRect)
                pygame.display.update()
                pygame.time.delay(700)
                win.blit(blankSurf, TextRect)
                pygame.display.update()
            gameDisplay()
            break
        else:
            continue

def gameOver():
    fail = True
    while fail:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((192,192,192))

        s = button("SIM", (disWidth/2 - 150), (disHeight - 150), 100, 50, gameIntro)
        n = button("NÃO", (disWidth/2 + 50), (disHeight - 150), 100, 50, saveRank)

        if s or n == True:
            break

        pygame.draw.rect(win, (140,120,83), ((disWidth/2 - 180), (disHeight/2 - 170 ), 360, 200))
        largeText = pygame.font.SysFont("comicsansms", 55)
        smallText = pygame.font.SysFont("freesansbold.ft", 25)
        TextSurf, TextRect = textObjects('GAME OVER', largeText)
        TextSurf1, TextRect1 = textObjects('Deseja jogar novamente?', smallText)
        TextSurf2, TextRect2 = textObjects("Sua pontuação foi: {}".format(pontos), smallText)
        TextRect.center = ((disWidth/2), (disHeight/2 - 100))
        TextRect1.center = ((disWidth/2), (disHeight/2 - 10))
        TextRect2.center = ((disWidth/2), (disHeight/2 - 40))
        win.blit(TextSurf,TextRect)
        win.blit(TextSurf1, TextRect1)
        win.blit(TextSurf2, TextRect2)


        pygame.display.update()

def objClicked(nome, x, img):
    global pontos
    global chances
    pos = pygame.mouse.get_pos()
    if (x + 64) >= pos[0] and pos[0] >= x and (y + 64) >= pos[1] and pos[1] >= y: #se o mouse esta dentro da imagem
        alpha = 1
        img.fill((1, 1, 1, alpha), None, 0)
        if nome in answer:
            pontos += 100
        elif nome != 'del':
            chances -= 1
        return True
    return False

def fallingImg(nome1, x1, img1, nome2 ,x2, img2, nome3, x3, img3, nome4, x4, img4):
    global y
    for y in range(110, 480, vel):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                click1 = objClicked(nome1, x1, img1)
                click2 = objClicked(nome2, x2, img2)
                click3 = objClicked(nome3, x3, img3)
                click4 = objClicked(nome4, x4, img4)
                if click1 == True:
                    nome1 = 'del'
                elif click2 == True:
                    nome2 = 'del'
                elif click3 == True:
                    nome3 = 'del'
                elif click4 == True:
                    nome4 = 'del'


        win.fill((192,192,192))

        pygame.draw.rect(win, (140,120,83), (((disWidth/2)-350),(disHeight-470), 700, 50))
        questionFont = pygame.font.SysFont("comicsansms", 20)
        TextSurf, TextRect = textObjects(question, questionFont)
        TextRect.center = ((disWidth/2), ((disHeight - 445)))
        win.blit(TextSurf,TextRect)
        pygame.draw.rect(win, (211,211,211), (((disWidth/2)-350),(disHeight-375), 700, 390))
        win.blit(pygame.image.load('imagens/estrela.png'), (((disWidth/2)-350), (disHeight-415)))
        pontosSurf, pontosRect = textObjects('{}'.format(pontos), questionFont)
        pontosRect.center = (((disWidth/2)-290), (disHeight - 399))
        win.blit(pontosSurf, pontosRect)
        win.blit(pygame.image.load('imagens/coração.png'), (((disWidth/2)-250), (disHeight-415)))
        chancesSurf, chancesRect = textObjects('{}'.format(chances), questionFont)
        chancesRect.center = (((disWidth/2)-190), (disHeight - 399))
        win.blit(chancesSurf, chancesRect)

        img1 = pygame.transform.scale(img1, (64,64))
        img2 = pygame.transform.scale(img2, (64,64))
        img3 = pygame.transform.scale(img3, (64,64))
        img4 = pygame.transform.scale(img4, (64,64))

        pygame.time.delay(10)
        win.blit(img1, (x1, y))
        win.blit(img2, (x2, y))
        win.blit(img3, (x3, y))
        win.blit(img4, (x4, y))
        if chances == 0 or nome1 == 'del' and nome2 == 'del' and nome3 == 'del' and nome4 == 'del':
            break

        pygame.display.update()

def get4Alis(classe):
    ali = alimento(alimento.getAli, alimento.getX) #transformar em lista alimentos
    ali2 = alimento(alimento.getAli, alimento.getX)
    ali3 = alimento(alimento.getAli, alimento.getX)
    aliJoker = classe(alimento.getAli, alimento.getX)
    return ali, ali2, ali3, aliJoker #retornar lista de alimentos

def gameDisplay():
    global question
    global answer
    game = True
    while game:
        pygame.time.delay(300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if theme == 'Construtores':
            ali, ali2, ali3, aliJoker = get4Alis(alimento.construtores) #colocar a função em uma lista ao invés de 4 variáveis
            question, answer = alimento.getQuestion('construPerg', 'construResp')
        elif theme == 'Reguladores':
            ali, ali2, ali3, aliJoker = get4Alis(alimento.reguladores)
            question, answer = alimento.getQuestion('reguPerg', 'reguResp')
        elif theme == 'Energeticos':
            ali, ali2, ali3, aliJoker = get4Alis(alimento.energeticos)
            question, answer = alimento.getQuestion('energPerg', 'energResp')

        for i in range(0,5): #fazer uma lista com as posições sorteadas (alimenyo[0].x) e apenas um while para sortear novas posições se a nova posição estiver na lista
            while (ali.x + ali.w) >= ali2.x and ali.x <= (ali2.x + ali2.w)  or (ali.x + ali.w) >= ali3.x and ali.x <= (ali3.x + ali3.w) or (ali.x + ali.w) >= aliJoker.x and ali.x <= (aliJoker.x + aliJoker.w):
                ali.x = alimento.getX()
            while (ali2.x + ali2.w) >= ali3.x and ali2.x <= (ali3.x + ali3.w) or (ali2.x + ali2.w) >= aliJoker.x and ali2.x <= (aliJoker.x + aliJoker.w):
                ali2.x = alimento.getX()
            while(ali3.x + ali3.w) >= aliJoker.x and ali3.x <= (aliJoker.x + aliJoker.w):
                ali3.x = alimento.getX()

        fallingImg(ali.nome, ali.x, ali.img, ali2.nome, ali2.x, ali2.img, ali3.nome, ali3.x, ali3.img, aliJoker.nome, aliJoker.x, aliJoker.img) #alimento[0].nome etc
        if chances == 0:
            gameOver()
            break

        pygame.display.update()

if __name__ == '__main__':
    gameName()
    gameOver()
