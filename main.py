#imports
import pygame
import random
from player import *
from doorN import *
#-----------------------------------------------------------
#initialization
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Escape Root")
#-----------------------------------------------------------
#constants and variables
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
scoreFont = pygame.font.SysFont("Arial", 30)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
background = pygame.image.load("arena.png")
logo = pygame.image.load("logo.png")
enemy = pygame.image.load("enemy.png")
musicMenu = pygame.image.load("musicMenu.png")
movement = pygame.image.load("movement.png")
maps = pygame.image.load("map.png")
exitRoomImg = pygame.image.load("exitRoomYAY.png")
timer = 1200000
currentSpeed = 5 
trapRooms = random.sample(range(1, 50), 10)
validRooms = [room for room in range(1, 50) if room not in trapRooms]
currentRoom = random.choice(validRooms)
#funny death texts
deathText = ["You slipped on a banana peel and died!","You stepped on a lego and died from the pain!","You were eaten by a hungry infant!","You fell into a puddle of water!","You forgot to eat breakfast and starved to death!","You were teleported into the sun!","You charged straight into a wall. Bold strategy", "You were attacked by a swarm of imaginary bees!",
             "You were hit by a falling piano!","You jumped too high and hit your head on the ceiling!","You forgot to breathe!","You got scared to death by a spider!","You sneezed too hard and died!","You lost a fight with the door!","I told you that room was sketchy!","I don't even know what to say",
             "It says here that you... died? What did you do?","That was on you buddy!","Honestly, it's best if we both pretend that never happened","Moments like this really explain the whole “switched at birth” situation","Your mom was right...you really are...special","Bro i'm telling your friends about this one!","Hint: THE POINT OF THIS GAME IS TO ESCAPE!",
             "Wrong room buddy!","You have been executed by a intrusive thought!","YOU WON...... wait no you lost!","It hurts to watch you play","At least you didn't die of embarrassment","Congratulations! You discovered a new way to fail. I'm writing this one down"]
restart = False
exitRoom = random.randint(1, 49)
musicVol = 0.5
run = True
#-----------------------------------------------------------
#ensuring exit != start room
while exitRoom == currentRoom or exitRoom in trapRooms:
    exitRoom = random.randint(1, 49)
keys = pygame.key.get_pressed()
doorUp = Doors(screen, "up")
doorDown = Doors(screen, "down")
doorLeft = Doors(screen, "left")
doorRight = Doors(screen, "right")
player = Character(screen)
player.rect.center = (512, 512)

while run == True:
#-----------------------------------------------------------
    #door visibility logic
    showLeft = True
    showRight = True
    showUp = True
    showDown = True
    timer -= 100
    mins = timer // 600000
    sec = (timer // 10000) % 60
#-----------------------------------------------------------
    #restart logic
    if restart == True:
        player = Character(screen)
        player.rect.center = (512, 512)
        trapRooms = random.sample(range(1, 50), 10)
        validRooms = [room for room in range(1, 50) if room not in trapRooms]
        currentRoom = random.choice(validRooms)
        exitRoom = random.randint(1, 49)
        while exitRoom == currentRoom or exitRoom in trapRooms:
            exitRoom = random.randint(1, 49)
        timer = 1200000
        restart = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#-----------------------------------------------------------
    #door visibility logic(rest)
    if currentRoom % 7 == 1: 
        showLeft = False
    if currentRoom % 7 == 0: 
        showRight = False
    if currentRoom < 8: 
        showUp = False
    if currentRoom > 42: 
        showDown = False
#-----------------------------------------------------------
    #player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: 
        player.MoveUp(currentSpeed)
    if keys[pygame.K_a]: 
        player.MoveLeft(currentSpeed)
    if keys[pygame.K_s]: 
        player.MoveDown(currentSpeed)
    if keys[pygame.K_d]: 
        player.MoveRight(currentSpeed)

    

#-----------------------------------------------------------
    #music

    if keys[pygame.K_UP]:
        if musicVol < 1.0:
            musicVol += 0.01
            pygame.mixer.music.set_volume(musicVol)
    if keys[pygame.K_DOWN]:
        if musicVol > 0.0:
            musicVol -= 0.01
            pygame.mixer.music.set_volume(musicVol)
    if keys[pygame.K_1]:
        try:
            music = pygame.mixer.music.load("SevenNationArmy.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(musicVol)
        except Exception as e:
            print("Error loading music:", e)
    if keys[pygame.K_2]:
        try:
            music = pygame.mixer.music.load("7Years.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(musicVol)
        except Exception as e:
            print("Error loading music:", e)
    if keys[pygame.K_3]:
        try:
            music = pygame.mixer.music.load("Beggin.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(musicVol)
        except Exception as e:
            print("Error loading music:", e)
    if keys[pygame.K_4]:
        try:
            music = pygame.mixer.music.load("BloodWater.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(musicVol)
        except Exception as e:
            print("Error loading music:", e)
    if keys[pygame.K_5]:
        try:
            music = pygame.mixer.music.load("DevilinDisguise.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(musicVol)
        except Exception as e:
            print("Error loading music:", e)
    if keys[pygame.K_6]:
        try:
            music = pygame.mixer.music.load("Heathens.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(musicVol)
        except Exception as e:
            print("Error loading music:", e)
    if keys[pygame.K_7]:
        try:
            music = pygame.mixer.music.load("HouseofMemories.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(musicVol)
        except Exception as e:
            print("Error loading music:", e)
    if keys[pygame.K_8]:
        try:
            music = pygame.mixer.music.load("Human.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(musicVol)
        except Exception as e:
            print("Error loading music:", e)
    if keys[pygame.K_9]:
        try:
            music = pygame.mixer.music.load("LegendsNeverDie.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(musicVol)
        except Exception as e:
            print("Error loading music:", e)
    if keys[pygame.K_0]:
        pygame.mixer.music.stop()
#-----------------------------------------------------------
    #hidden easter eggs
    if currentRoom == 7 and not pygame.mixer.music.get_busy():
        try:
            music = pygame.mixer.music.load("SevenNationArmy.mp3")
            pygame.mixer.music.play(-1)
        except Exception as e:
            print("Error loading music:", e)
    

#-----------------------------------------------------------
    #door logic
    if player.rect.top < 150 and showUp == True and player.rect.centerx > 444 and player.rect.centerx < 590:
        currentRoom -= 7
        player.rect.bottom = 800
    elif player.rect.bottom > 850 and showDown == True and player.rect.centerx > 444 and player.rect.centerx < 590:
        currentRoom += 7
        player.rect.top = 200
    elif player.rect.left < 50 and showLeft == True and player.rect.centery > 444 and player.rect.centery < 590:
        currentRoom -= 1
        player.rect.right = 924
    elif player.rect.right > 974 and showRight == True and player.rect.centery > 444 and player.rect.centery < 590:
        currentRoom += 1
        player.rect.left = 100

    if currentRoom in trapRooms:
        screen.blit(enemy, (0, 0))
        deathMessage = random.choice(deathText)
        loseText = scoreFont.render(deathMessage.format(deathMessage=deathMessage), True, (255, 0, 0))
        screen.blit(loseText, (100, 800))
        pygame.display.update()
        pygame.time.delay(3000)
        restart = True
    if keys[pygame.K_BACKSPACE]:
        restart = True
    if keys[pygame.K_ESCAPE]:
        run = False
    if timer <= 0:
        screen.blit(enemy, (0, 0))
        timeOver = scoreFont.render("Time's Up! You failed to escape in time!", True, (255, 0, 0))
        screen.blit(timeOver, (100, 800))
        pygame.display.update()
        pygame.time.delay(3000)
        restart = True
#-----------------------------------------------------------
    #showing entities
    screen.blit(background, (0, 0))

    if showUp == True: 
        doorUp.blit()
    if showDown == True: 
        doorDown.blit()
    if showLeft == True: 
        doorLeft.blit()
    if showRight == True: 
        doorRight.blit()

    player.blit()  
    roomText = scoreFont.render(f"Room: {currentRoom}         time: {timer//600000}m{sec}s             J: Music K: Movement M: Map", True, (255, 255, 255))
    screen.blit(roomText, (0, 0))
    screen.blit(logo, (915, 0))
    if keys[pygame.K_j]:
        screen.blit(musicMenu, (0, 0))
    if keys[pygame.K_k]:
        screen.blit(movement, (0, 0))
    if keys[pygame.K_m]:
        screen.blit(maps, (0, 0))
    if currentRoom == exitRoom:
        screen.blit(exitRoomImg, (0, 0))
        winText = scoreFont.render("You Escaped! The exit was in Room {exitRoom}!".format(exitRoom=exitRoom), True, (0, 0, 0))
        screen.blit(winText, (512 - winText.get_width() // 2, 100))
        pygame.display.update()
        pygame.time.delay(3000)
        restart = True
    clock.tick(100)
    pygame.display.update()
pygame.quit()