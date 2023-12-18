import pygame
import random
import sys
import time

pygame.init()

Coordenada_z = [ "nom1","nom2","nom3", "nom4", "nom5", "nom6", "nom7", "nom8", "nom9", "nom10", "nom11", "nom12", "nom13", "nom14", "nom15", "nom16", "nom17", "nom18", "nom19", "nom20","nom21", "nom22" ]

yeti = random.choice(Coordenada_z)

print(yeti)

reloj = 0
credits = 0
premio = 0

Azul = (0, 58, 253)

Rojo = (183, 18, 18 )

ventana = pygame.display.set_mode((1024, 690))

tiempo_pausa = random.uniform(5, 12)
tiempo_inicio_pausa = None
en_pausa = False

fondo = pygame.image.load("image/end.jpg")

pygame.display.set_caption("Funny Furries")

Coordenada_X = 50

Coordenada_Y = 25

screen = pygame.image.load("image/bar.png")
screen0 = pygame.image.load("image/barbar.png")
screen2 = pygame.image.load("image/bell.png")
screen3 = pygame.image.load("image/cherry.png")
screen4 = pygame.image.load("image/manzana.png")
screen5 = pygame.image.load("image/melon.png")
screen6 = pygame.image.load("image/naranja.png")
screen7 = pygame.image.load("image/sandia.png")
screen8 = pygame.image.load("image/sevenseven.png")
screen9 = pygame.image.load("image/star.png")


screen1 = pygame.transform.scale(screen, (60, 60))
barbar = pygame.transform.scale(screen0, (60, 60))
bell = pygame.transform.scale(screen2, (60, 60))
cherry = pygame.transform.scale(screen3, (60, 60))
manzana = pygame.transform.scale(screen4, (60, 60))
melon = pygame.transform.scale(screen5, (60, 60))
naranja = pygame.transform.scale(screen6, (60, 60))
sandia = pygame.transform.scale(screen7, (60, 60))
sevenseven = pygame.transform.scale(screen8, (60, 60))
star = pygame.transform.scale(screen9, (60, 60))

vuelta = True 

velocidad = 50

movimiento = True

font = pygame.font.Font(None, 36)

def mostrar_texto(texto, posicion, color, tamano=50):
    fuente = pygame.font.Font(None, tamano)
    texto_renderizado = fuente.render(texto, True, color)
    ventana.blit(texto_renderizado, posicion) 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Corregido aquí
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c: 
                 credits += 1
            if event.key == pygame.K_SPACE:
                    vuelta = not True
                    credits -= 1

        
    ventana.fill(Azul)
    ventana.blit(fondo, [0,0])

    mostrar_texto(f"Créditos: {credits}", (800, 60), (255, 0, 0))
    mostrar_texto(f"Premio: {premio}", (800, 95), (255, 0, 0))
 
    pygame.draw.rect(ventana, Azul, (50, 25, 60, 60))
    pygame.draw.rect(ventana, Azul, (150, 25, 60, 60))
    pygame.draw.rect(ventana, Azul, (250, 25, 60, 60))
    pygame.draw.rect(ventana, Azul, (350, 25, 60, 60))
    pygame.draw.rect(ventana, Azul, (450, 25, 60, 60))
    pygame.draw.rect(ventana, Azul, (550, 25, 60, 60))
    pygame.draw.rect(ventana, Azul, (650, 625, 60, 60))
    
    pygame.draw.rect(ventana, Azul, (650, 125, 60, 60))
    pygame.draw.rect(ventana, Azul, (650, 225, 60, 60))
    pygame.draw.rect(ventana, Azul, (650, 325, 60, 60))
    pygame.draw.rect(ventana, Azul, (650, 425, 60, 60))
    pygame.draw.rect(ventana, Azul, (650, 525, 60, 60))
    pygame.draw.rect(ventana, Azul, (650, 625, 60, 60))
    pygame.draw.rect(ventana, Azul, (550, 625, 60, 60))
    pygame.draw.rect(ventana, Azul, (450, 625, 60, 60))
    pygame.draw.rect(ventana, Azul, (350, 625, 60, 60))
    pygame.draw.rect(ventana, Azul, (250, 625, 60, 60))
    pygame.draw.rect(ventana, Azul, (150, 625, 60, 60))
    pygame.draw.rect(ventana, Azul, (50, 625, 60, 60))
    pygame.draw.rect(ventana, Azul, (50, 525, 60, 60))
    pygame.draw.rect(ventana, Azul, (50, 425, 60, 60))
    pygame.draw.rect(ventana, Azul, (50, 325, 60, 60))
    pygame.draw.rect(ventana, Azul, (50, 225, 60, 60))
    pygame.draw.rect(ventana, Azul, (50, 125, 60, 60))
    pygame.draw.rect(ventana, Azul, (650, 25, 60, 60))

    nom1 = ventana.blit(naranja, (50, 25))
    nom2 = ventana.blit(bell, (150, 25))
    nom3 =ventana.blit(screen1, (250, 25))
    nom4 = ventana.blit(barbar, (350, 25))
    nom5 = ventana.blit(manzana, (450, 25))
    nom6 = ventana.blit(cherry, (550, 25))
    nom7 = ventana.blit(melon, (650, 25))
    nom8 = ventana.blit(sandia, (650, 125))
    nom9 = ventana.blit(cherry, (650, 225))
    nom10 = ventana.blit(manzana, (650, 425))
    nom11 = ventana.blit(cherry, (650, 525))
    nom12 = ventana.blit(naranja, (650, 625))
    nom13 = ventana.blit(bell, (550, 625))
    nom14 = ventana.blit(cherry, (450, 625))
    nom15 = ventana.blit(sevenseven, (350, 625))
    nom16 = ventana.blit(manzana, (250, 625))
    nom17 = ventana.blit(cherry, (150, 625))
    nom18 = ventana.blit(melon, (50, 625))
    nom19 = ventana.blit(star, (50, 525))
    nom20 = ventana.blit(cherry, (50, 425))
    nom21 = ventana.blit(manzana, (50, 225))
    nom22 = ventana.blit(cherry, (50, 125))

    pygame.draw.rect(ventana, Rojo, (Coordenada_X, Coordenada_Y, 60, 60),5)

    if vuelta == False:
            if movimiento:
                if Coordenada_X < 650:
                    Coordenada_X += velocidad
                elif Coordenada_Y < 625:
                    Coordenada_Y += velocidad
                else: 
                     movimiento = False
            else:
                if Coordenada_X > 25:
                    Coordenada_X -= velocidad
                elif Coordenada_Y > 60:
                     Coordenada_Y -= velocidad
                else:
                    movimiento = True

    pygame.display.update()