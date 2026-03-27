import pygame
class Arrows:

    def __init__(self,screen,ypos):
        self.screen = screen
        self.image = pygame.image.load("trap_arrow.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (150, ypos)
    def blit(self):
        xpos = self.rect.x
        if xpos < self.screen.get_width():
            self.rect.x += 5
        self.screen.blit(self.image, self.rect)
    def GetRect(self):
        return self.rect