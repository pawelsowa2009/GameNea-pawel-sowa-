import pygame

class Character:
    mapWidth = 1024 - (2 * 100)
    mapHeight = 1024 - (2 * 100)
    borderThickness = 100
    timer = 3600
    mins = 3600 // 60
    sec = 3600 % 60

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_rect().width/4, self.image.get_rect().height/4) )
        self.rect = self.image.get_rect()
        self.rect.center = (600,289)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def GetRect(self):
        return self.rect
    
    def MoveUp(self, speed):
        if self.rect.top > self.borderThickness:
            self.rect.y -= speed

    def MoveDown(self, speed):
        if self.rect.bottom < self.borderThickness + self.mapHeight:
            self.rect.y += speed

    def MoveLeft(self,  speed):
        if self.rect.left > self.borderThickness - 60:
            self.rect.x -= speed

    def MoveRight(self, speed):
        if self.rect.right < self.borderThickness  + self.mapWidth + 60:
            self.rect.x += speed
    def Timer(self,timer):
        mins = timer // 60
        sec = timer % 60
        return mins, sec
