import pygame
class Exit:

    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("exitClosed.png")
        self.rect = self.image.get_rect()
        self.rect.center = (600, 1000)
    def blit(self):
        self.screen.blit(self.image, self.rect)
    def GetRect(self):
        return self.rect
    def open(self):
        self.image = pygame.image.load("exitOpen.png")
    def close(self):
        self.image = pygame.image.load("exitClosed.png")