import pygame
class Player:
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 1200
    borderThickness = 200
    mapWidth = SCREEN_WIDTH - (2 * borderThickness)
    mapHeight = SCREEN_HEIGHT - (2 * borderThickness )

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_rect().width/4, self.image.get_rect().height/4) )
        self.rect = self.image.get_rect()
        self.rect.center = (600,289)
        self.maxStamina = 100
        self.stamina = 100
        self.staminaRegen = 0.5
        self.staminaCost = 1.5

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def GetRect(self):
        return self.rect
    
    def MoveUp(self, screenHeight, speed):
        if self.rect.top > self.borderThickness:
            self.rect.y -= speed

    def MoveDown(self, screenHeight, speed):
        if self.rect.bottom < self.borderThickness + self.mapHeight:
            self.rect.y += speed

    def MoveLeft(self, screenWidth, speed):
        if self.rect.left > self.borderThickness:
            self.rect.x -= speed

    def MoveRight(self, screenWidth, speed):
        if self.rect.right < self.borderThickness + self.mapWidth:
            self.rect.x += speed

    def draw_stamina(self):
        bar_width = 200
        bar_height = 20
        bar_x = (self.screen.get_width() / 2) - (bar_width / 2)
        bar_y = self.screen.get_height() - 40 
        pygame.draw.rect(self.screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))
        current_width = (self.stamina / self.maxStamina) * bar_width
        pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, current_width, bar_height))
        pygame.draw.rect(self.screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height), 2)