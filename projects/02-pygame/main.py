import pygame
import random
import math
from pygame import mixer

#Initialize pygame
pygame.init()
score = 0
num_of_enemies = 5

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./icon.png')
pygame.display.set_icon(icon)

# Score
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

# background Music
mixer.music.load('thuppakki.mp3')
mixer.music.play(-1)

# Player
player_icon = pygame.image.load("./player.png")
playerX = 380
playerY = 500
playerX_change = 0

# Enemy
enemy_icon = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(num_of_enemies):
    enemy_icon.append(pygame.image.load("./enemy.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(30)

# Bullet - ready state not visible
bullet_icon = pygame.image.load("./bullet.png")
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

# Background
bg_icon = pygame.image.load("./space.png")

def player(x,y):
    screen.blit(player_icon,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_icon[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_icon,(x+20,y+12))

def isCollison(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True

def show_score(x,y):
    score_text = font.render("Score : "+ str(score), True,(255,255,255))
    screen.blit(score_text,(x,y))

running = True

while running:

    screen.fill((0,0,0))
    screen.blit(bg_icon,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = +4
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet_sound = mixer.Sound("./gun_shot.wav")
                    bullet_sound.play()
                    fire_bullet(bulletX,bulletY) 
        if event.type == pygame.KEYUP:
            playerX_change = 0

    playerX += playerX_change

    if playerX < 0:
        playerX = 0
    if playerX > 736:
        playerX = 736

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]

        if enemyX[i] > 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
            
        if isCollison(enemyX[i],enemyY[i],bulletX,bulletY):
            score += 1
            print(score)
            die_sound = mixer.Sound("./vadivel_haba.wav")
            die_sound.play()
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)
            bullet_state = "ready"
            bulletY = 500
        
        enemy(enemyX[i], enemyY[i], i)

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    
    if bulletY < 0:
        bullet_state = "ready"
        bulletY = 500

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()