# control + alt + L = correct indentation
import pygame
import random
dot = pygame.image.load("dot.png")


pygame.init()  # intialize the game
# create a screen
screen = pygame.display.set_mode((900, 700))
background = pygame.image.load('space.png')

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("rocketx32.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("rocketx128.png")
playerX = 400
playerY = 550
playerX_change = 0

# bullet
bulletImg = pygame.image.load("bulletx32.png")
bulletX = 0
bulletY = 550
bulletY_change = 9
bullet_state = "ready"  # ready / fire

# enemy
enemyImg = pygame.image.load("monsterx64.png")
enemyX = random.randint(30, 806)
# enemyY = random.randint(50, 300)
enemyY = 50
enemyX_change = 3.5
# enemyY_change = 0
moving_which_side = ""

score = 0

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


def enemy(ex, ey):
    screen.blit(enemyImg, (ex, ey))

def player(x, y):
    screen.blit(playerImg, (x, y))


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
                moving_which_side = "left"
            if event.key == pygame.K_RIGHT:
                playerX_change = 4.5
                moving_which_side = "right"
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if moving_which_side == "left":
                if event.key == pygame.K_LEFT:
                    playerX_change = 0
            elif moving_which_side == "right":
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 771:
        playerX = 771

    enemyX += enemyX_change
    if enemyX < 30 or enemyX > 807:
        enemyX_change = -1 * enemyX_change
        enemyY += 75

    # bullet movement
    if bulletY < 0:
        bulletY = 550
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # collision
    collision = iscollission(enemyX,enemyY,bulletX,bulletY)
    if collision is True:
        bulletY = 550
        bullet_state = "ready"
        score += 100
        print(score)
        enemyX = random.randint(30, 806)
        enemyY = 50

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

# https://www.ncertbooks.guru/ts-grewal-accountancy-class-12-solutions-chapter-4/
