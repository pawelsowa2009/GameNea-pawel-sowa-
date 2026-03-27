
import pygame
import random
from TrapArrows import *
from player import *
from exit import *
pygame.init()
pygame.font.init()
scoreFont = pygame.font.SysFont("Arial", 60)
score = 3
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
borderThickness = 200
mapWidth = SCREEN_WIDTH - (2 * borderThickness)
mapHeight = SCREEN_HEIGHT - (2 * borderThickness )
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
background = pygame.image.load("map.png").convert()
gameWin = pygame.image.load("gameWin.png").convert()
player = Player(screen)
run = True
arrows = []
exit = Exit(screen)
restart = False
try:
    pygame.mixer.init()
    pygame.mixer.music.load("music.ogg")
    pygame.mixer.music.play(-1)
except Exception as e:
    print("Audio error:", e)

while(run):

    if restart == True:
        arrows.clear()
        player = Player(screen)
        player.rect.center = (600, 289)
        restart = False

    rand = random.randint(0, 100)
    if rand > 90:
        ypos = random.randint(borderThickness, borderThickness + mapHeight)
        arrows.append(Arrows(screen, ypos))
    for arrow in arrows:
        if arrow.GetRect().x > 1000:
            arrows.remove(arrow)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    sprinting = keys[pygame.K_LSHIFT] and (keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d])
    if keys[pygame.K_e] and player.GetRect().colliderect(exit.GetRect()):
        exit.open()
        screen.blit(gameWin, (0, 0))
        pygame.display.update()
        pygame.time.delay(2000)
        score += 1

        exit.close()
        restart = True
    if keys[pygame.K_w]:
        player.MoveUp(SCREEN_HEIGHT, currentSpeed)
    if keys[pygame.K_s]:
        player.MoveDown(SCREEN_HEIGHT, currentSpeed)
    if keys[pygame.K_a]:
        player.MoveLeft(SCREEN_WIDTH, currentSpeed)
    if keys[pygame.K_d]:
        player.MoveRight(SCREEN_WIDTH, currentSpeed)
    if sprinting and player.stamina == 0:
        sprinting = False
    if sprinting and player.stamina > 0:
        currentSpeed = 4
        player.stamina -= player.staminaCost
    else:
        currentSpeed = 2
        if player.stamina < player.maxStamina:
            player.stamina += player.staminaRegen
    screen.blit(background, (0, 0))
    player.draw_stamina()
    exit.blit()
    player.blit()
    score_surface = scoreFont.render("Score: " + str(score), True, (0,255,0))
    screen.blit(score_surface, (10, 10))


    for arrow in arrows:
        arrow.blit()
        arrowRect = arrow.GetRect()
        playerRect = player.GetRect()
        if arrowRect.colliderect(playerRect):
            gameOver = pygame.image.load("lostLife.png")
            screen.blit(gameOver, (0, 0))
            pygame.display.update()
            pygame.time.delay(2000)
            score -=1
            restart = True
    if score <= 0:
        gameOver = pygame.image.load("gameLost.png")
        screen.blit(gameOver, (0, 0))
        pygame.display.update()
        pygame.time.delay(10000)
        score = 3
    if score >= 6:
        gameWin = pygame.image.load("win.png")
        screen.blit(gameWin, (0, 0))
        pygame.display.update()
        pygame.time.delay(10000)
        score = 3

    clock.tick(100)
    pygame.display.update()
print(score)
pygame.quit()