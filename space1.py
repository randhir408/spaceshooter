#Step1---import "pygame module" in your pycharm.
#file->setting-->project interpreter search module and install
#step2---download pic from "icon8.com" or "flaticon.com"
#Now let's program step follow


import pygame
import random
import math
from pygame import mixer
pygame.init()
disp = pygame.display.set_mode([800, 600])
bullet = mixer.Sound("bullet.ogg")
collision = mixer.Sound("pew.wav")
#For player
img1 = pygame.image.load("icons8-launch-96 (1).png")
px = 20
py = 480
px_change = 0
py_change = 0
#for enemy:
img2 = []
ex = []
ey = []
ey_change = []
for i in range(0, 5):
    img2.append(pygame.image.load("icons8-cute-monster-48.png"))
    ex.append(random.randint(50, 750))
    ey.append(random.randint(20, 100))
    ey_change.append(0.5)

#for bullet
img3 = pygame.image.load("missile.png")
bx = 0
by = 480
by_change = 0
state = 0

#for score
score_value = 0
score_font = pygame.font.SysFont("comicsansms", 35)

#for game over
over_font = pygame.font.SysFont("comicsansms", 80)

#for background
backg = pygame.image.load("backgdpic.jpg")
mixer.music.load("backgroung.ogg")
mixer.music.play(-1)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            px_change = -7
            py_change = 0
        elif event.key == pygame.K_RIGHT:
            px_change = 7
            py_change = 0
        elif event.key == pygame.K_SPACE:
            if state == 0:
                bullet.play()
                bx = px
                by_change = -60
                state = 1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            px_change = 0
            py_change = 0
    # changing co-ordinates of player
    px = px+px_change
    # changing co-ordinates of bullet
    by = by+by_change
    if px > 736:
        px = 736
    if px < 0:
        px = 0
    disp.fill((0, 0, 0))
    disp.blit(backg, (0, 0))
    if state == 1:
        disp.blit(img3, (bx+40, by))
        if by <= 0:
            by = 480
            state = 0
    for i in range(0, 5):
        if ey[i] >= 480:
            over = over_font.render("GAME OVER", True, (255, 255, 0))
            disp.blit(over, (200, 200))
            for j in range(0, 5):
                ey[j] = 2000
        distance = math.sqrt(((bx-ex[i])**2)+((by-ey[i])**2))
        if distance < 25:
            collision.play()
            ex[i] = random.randint(50, 750)
            ey[i] = random.randint(20, 100)
            score_value += 1
        # changing co-ordinates of enemy
        ey[i] = ey[i] + ey_change[i]
        score = score_font.render("SCORE:"+str(score_value), True, (255, 255, 0))
        disp.blit(score, (10, 10))
        disp.blit(img2[i], (ex[i],ey[i]))
    disp.blit(img1, (px, py))
    pygame.display.flip()
pygame.quit()

#Please like,share and subscribe my channel friend .
