import pygame
import main
class Doors:
    def __init__(self, screen, direction):
        self.screen = screen
        self.image = pygame.image.load(main.doorMode).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()/4), int(self.image.get_height()/4)))
        self.rect = self.image.get_rect()
        if direction == "up":
            self.rect.center = (500, 126)
            self.image = pygame.transform.scale_by(self.image, 1.6)
        elif direction == "down":
            self.rect.center = (512, 900)
            self.image = pygame.transform.rotate(self.image, 180)
        elif direction == "left":
            self.rect.center = (145, 512)
            self.image = pygame.transform.rotate(self.image, 90)
        elif direction == "right":
            self.rect.center = (915, 512)
            self.image = pygame.transform.rotate(self.image, 270)
    def blit(self):
        self.screen.blit(self.image, self.rect)
        
        