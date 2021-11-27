import pygame
import time
import random

from funcoes import text_objects

pygame.init()
largura = 800
altura = 600
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode( configTela )
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
pygame.display.set_caption("Dino Run - Eduarda Pagnussat")

icone = pygame.image.load("assets/dinoIcon.png")
pygame.display.set_icon(icone)
dino = pygame.image.load("assets/dinoLarge.png")
fundo = pygame.image.load("assets/skyDino.png")
meteoro = pygame.image.load("assets/meteoro.png")

explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
misselSound = pygame.mixer.Sound("assets/missile.wav")

def mostraDino(x,y):
    dino = pygame.image.load("assets/dinoLarge.png")
    gameDisplay.blit(dino, (x,y))

def mostraMeteoro(x,y):
    meteoro = pygame.image.load("assets/meteoro.png")
    gameDisplay.blit(meteoro, (x,y))

def escreverPlacar(contador):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Desvios:" +str(contador), True, white)
    gameDisplay.blit(texto, (10,10))

def dead():
    pygame.mixer.Sound.play(explosaoSound)
    pygame.mixer.music.stop()
    return escreverTela("Extinto!")

def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game()

def game():
    pygame.mixer.music.load("assets/ironsound.mp3")
    pygame.mixer.music.play(-1)
    dinoPosicaoX = largura*0.45
    dinoPosicaoY = altura*0.8
    movimentoX = 0
    larguraDino = 110
    velocidade = 10

    meteoroAltura = 250
    meteoroLargura = 50
    meteoroVelocidade = 3
    meteoroX = random.randrange(0, largura)
    meteoroY = -200

    desvios = 0

    pygame.mixer.Sound.play(misselSound)

    ######
    #config de logs + email e nome

    name = input('Enter your name: ')
    email = input('Enter your email: ')
    data = {'name':name,'email':email}
    logs = open('logs.txt','a')

    #config try except

    try:
        logs.write(f'{data}\n')
    except:
        print('Error logging')

    logs.write(str(data) + '\n')
    

    while True:
        acoes = pygame.event.get()
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade*-1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = 5
            if acao.type == pygame.KEYUP:
                movimentoX = 0
    


        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0,0))

        escreverPlacar(desvios)

        meteoroY = meteoroY + meteoroVelocidade
        mostraMeteoro(meteoroX, meteoroY)

        if meteoroY > altura:
            meteoroY = -200
            meteoroX = random.randrange(0, largura)
            desvios = desvios+1
            meteoroVelocidade += 2
            pygame.mixer.Sound.play(misselSound)

        
        dinoPosicaoX += movimentoX
        if dinoPosicaoX < 0:
            dinoPosicaoX = 0
        elif dinoPosicaoX > largura-larguraDino:
            dinoPosicaoX = largura-larguraDino

        #analise de colisao
        if dinoPosicaoY < meteoroY + meteoroAltura:
            if dinoPosicaoX < meteoroX and dinoPosicaoX+larguraDino > meteoroX or meteoroX + meteoroLargura > dinoPosicaoX and meteoroX+meteoroLargura < dinoPosicaoX + larguraDino:
                dead()
        #analise de colisao

        mostraDino(dinoPosicaoX, dinoPosicaoY)

        pygame.display.update()

        clock.tick(60)
game()