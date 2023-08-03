# control + alt + L = correct indentation
import pygame
import random
from pygame import mixer
dot = pygame.image.load("D:\Shubham\(Python)\SpaceWar\dot.png")


pygame.init()  # intialize the game
# create a screen
screen = pygame.display.set_mode((900, 700))
background = pygame.image.load('D:\Shubham\(Python)\SpaceWar\space.png')

'''
# background music
mixer.music.load('backgrownd.wav')
mixer.music.play(-1)                     '''

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('D:\Shubham\(Python)\SpaceWar\irocketx128.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('D:\Shubham\(Python)\SpaceWar\irocketx128.png')
playerX = 400
playerY = 550
playerX_change = 0

# bullet
bulletImg = pygame.image.load("D:\Shubham\(Python)\SpaceWar\ibulletx32.png")
bulletX = 0
bulletY = 550
bulletY_change = 9
bullet_state = "ready"  # ready / fire

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
no_of_enemy = 6

for i in range(no_of_enemy):
    enemyImg.append(pygame.image.load("D:\Shubham\(Python)\SpaceWar\imonsterx64.png"))
    enemyX.append(random.randint(30, 806))
    # enemyY = random.randint(50, 300)
    enemyY.append(50)
    enemyX_change.append(3.5)
    # enemyY_change = 0

# score
score_value = 0
#font = pygame.font.Font('D:\(Python)\pythonProject1\freesansbold.ttf',32)
textX = 10
textY = 10

# game over
overFont = pygame.font.Font('C:\Windows\Fonts\Arial.ttf',64)

def game_over_text():
    over_text = overFont.render('GAME OVER', True, (255, 0, 0))
    screen.blit(over_text, (250,300))

def show_score(x,y):
    score = overFont.render('score :' + str(score_value), True,(255,255,255))
    screen.blit(score, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 48, y))



#
def iscollission(enemyX, enemyY, bulletX, bulletY):
    a, b, c, d = enemyX, enemyY, bulletX + 48, bulletY
    d= (a-c)**2 + (b-d)**2
    #if (c - a < 1) and (d - b < 1):
    if d < 1000:
        return True
    else:
        return False


def enemy(ex, ey,i):
    screen.blit(enemyImg[i], (ex, ey))

def player(x, y):
    screen.blit(playerImg, (x, y))

moving_which_side = "left"

# game loop
running = True
while running:
    # screen.fill((220, 220, 220))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 4.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    #bullet_sound = mixer.Sound('lazer.wav')
                    #bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if moving_which_side == "left":
                if event.key == pygame.K_LEFT:
                    playerX_change = 0
            elif moving_which_side == "right":
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0

    show_score(textX,textY)

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 771:
        playerX = 771

    # enemy movement
    for i in range(no_of_enemy):

        # game over
        if enemyY[i] > 550:
            for j in range(no_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 30 or enemyX[i] > 807:
            enemyX_change[i] = -1 * enemyX_change[i]
            enemyY[i] += 75

        # collision
        collision = iscollission(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision is True:
            #explosion_sound = mixer.Sound('explosion.wav')
            #explosion_sound.play()
            bulletY = 550
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(30, 806)
            enemyY[i] = 50
        enemy(enemyX[i], enemyY[i],i)


    # bullet movement
    if bulletY < 0:
        bulletY = 550
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)

    pygame.display.update()