








import math
import random
import pygame

from pygame import mixer

#inicio del juego 
pygame.int()

# se crea el fondo de pantalla
screen = pygame.display.set_mode((1000,800))

#fondo de pantalla
background  = pygame.image.load('fondo.png')

# sonido de fondo
mixer.music.load('UTF-8background.wav')
mixer.music.play(-1)

# titulo y icono
pygame.display.set_caption("Perdidos en el fondo del mar")
icon = pygame.image.load('Enemigo1-removebg-preview.png')
pygame.display.set_icon(icon)

#jugador
PlayerImg=pygame.image.load('nave-transformed.png')
playerX=370
player=480
playerX_change=0

#enemigos
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies= 20

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemigo2.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

    #tridente 

    armaImg= pygame.image.load('bala-removebg-preview.png')
    armaX=0
    armaY=480
    armaX_change=0
    armaY_change=10
    arma_estado="ready"

#puntaje 

score_value=0
font =pygame.font.Font('autography(1).zip',32)


textX=10
textY=10

#juego terminado
over_font =pygame.font.Font('beauty_sunny.zip' ,64)

def show_puntaje(x,y):
    score=font.render("Score : "+str(score_value).true,(255,255,255))
    screen.blit(score,(x,y))
def gameover_text():
    over_text= over_font.render("Game Over",True,255,255,255)
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(PlayerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def Iniciar_disparo(x,y):
    global bulletstate
    arma_estado = "Fire" 
    screen.blit(armaImg,(x+16,y+10)) 
def iscollision(enemyX,enemyY,armaX,armaY):
    distance = math.sqrt(math.pow(enemyX-armaX)+(math.pow(enemyY-armaY,2)))
    if distance<27:
        return True
    else : return False

# game loop 
running = True 
while running:
    screen.fill((0,0,0))
    #imagen de fondo
    screen.blit(backgroud,(0,0))
for event in pygame.event.get():
    if event.type == pygame.quít:
        running =False


        # si presiona derecha o izquierda
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-5
            if event.key==pygame.K_RIGHT:
                playerX_change=5 

     # RGB = Red, Green, Blue
     screen.fill((0, 0, 0))
     # Backgroud Image
     screen.blit(background, (0,0))
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False

         # if keystroke is pressed check whether its right or left
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_LEFT:
                

