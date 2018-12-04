import pygame


pygame.init()
colorInactive = (220,220,220)
colorActive = (211,211,211)
FONT = pygame.font.SysFont('freesansbold.ft', 20)

class inputBox:

    def __init__(self, x, y, w, h, len, forbiddenKey=None, text=''):
        self.rect = pygame.Rect(x,y,w,h)
        self.len = len
        self.forbiddenKey = forbiddenKey
        self.color = colorInactive
        self.text = text
        self.initText = text
        self.textSurf = FONT.render(text, True, (0,0,0))
        self.active = False

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.color = colorActive
            else:
                self.active = False
                self.color = colorInactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if self.text == self.initText:
                    self.text = ''
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) <= self.len:
                        if event.key != self.forbiddenKey and event.key != pygame.K_RETURN:
                            self.text += event.unicode
                self.textSurf = FONT.render(self.text, True, (0,0,0))

        return self.text

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.textSurf, (self.rect.x+5, self.rect.y+5))
