import pygame
import constantes 
from personajes import Personaje
import juego
import os
import sys
import random
from time import sleep

# funciones:

# Funcion para escalar una imagen

def invertir_imagen(imagen):
    return pygame.transform.flip(imagen, True, False)

def escalar_imagen(jugar_imagen, escala):
    return pygame.transform.scale(jugar_imagen,
                                        (jugar_imagen.get_width()*escala,
                                         jugar_imagen.get_height()*escala))
    
    

# funcion para contar elementos:
def contar_elementos(directorio):
    if os.path.exists(directorio):
        return len(os.listdir(directorio))
    


# funcion listar nombres elementos:
def nombres_carpetas(directorio):
    return os.listdir(directorio)



pygame.init()

# crear la ventana
ventana = pygame.display.set_mode((constantes.ancho, constantes.alto))


# titulo de la ventana
pygame.display.set_caption("Juego de Funciones")

animaciones = []
for i in range(1,5):
    img = pygame.image.load(f"assets//imagenes//characters//player//{i} imagen.png")
    img = escalar_imagen(img, constantes.escala_personaje)
    animaciones.append(img)

# enemigos:
directorio_enemigos = "assets\imagenes\characters\enemigo"
tipo_enemigos = nombres_carpetas(directorio_enemigos)

animaciones_enemigos = []

for eni in tipo_enemigos:
    lista_temp = []
    ruta_temp = f"assets//imagenes//characters//enemigo//{eni}"
    num_animaciones = contar_elementos(ruta_temp)
    
    for i in range(1, num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}//dragon_{i}.png")
        img_enemigo = escalar_imagen(img_enemigo, constantes.escala_enemigo)
        img_enemigo = invertir_imagen(img_enemigo) # invertir la imagen
        lista_temp.append(img_enemigo)
    animaciones_enemigos.append(lista_temp)


jugador_imagen = pygame.image.load("assets//imagenes//characters//player//1 imagen.png")
jugador_imagen = escalar_imagen(jugador_imagen, constantes.escala_personaje)

#craer un jugador de la clase personaje
jugador = Personaje(100, 100, animaciones)

#craer un enemigo de la clase personaje
dragon = Personaje(900,300, animaciones_enemigos[0])


#crear una lista de enemigos
lista_enemigos = []
lista_enemigos.append(dragon)

# definir las varibles de movimiento del jugador

mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False




# con el frame rate
    
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 50)
lista_texto = juego.lista
texto_1 = random.choice(lista_texto)
        
texto = fuente.render(texto_1, True, (255, 255, 255))


# para que la ventana no se cierre

run = True
while run == True:
    

    
    
    # que vaya a 60 fps
    reloj.tick(constantes.fps)
    
    # pinta el fondo de la ventana
    ventana.fill(constantes.color_bg) 
    
    # texto 
    
   
    ventana.blit(texto, (500, 100))

    
    # calcular el movimiento del jugador
    delta_X = 0
    delta_Y = 0
    
    # calcular el movimiento del jugador 2
    delta_X2 = 0
    delta_Y2= 0
    
    if mover_derecha == True:
        delta_X = constantes.velocidad
    if mover_izquierda == True:
        delta_X = -constantes.velocidad
    if mover_arriba == True:
        delta_Y = -constantes.velocidad
    if mover_abajo == True:
        delta_Y = constantes.velocidad
    
    
    
    # mover el jugador
    jugador.movimiento(delta_Y, delta_X)
    #actualizar el jugador
    jugador.actualizar()
    # actualizar el enemigo
    dragon.actualizar()
    # dibuja el jugador en la ventana
    
    jugador.dibujar(ventana)  
    
    #dibuja el enemigo en la ventana
    dragon.dibujar(ventana)
    
    
    
    for event in pygame.event.get():
        
        # para cerrar el juego9000
        if event.type == pygame.QUIT:
            run = False
            
            
            
        # para mover el jugador 1
        
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_arriba = True
            if event.key == pygame.K_d:
                mover_abajo = True
            if event.key == pygame.K_s:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_izquierda = True

        # para dejar de mover el jugador

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_arriba = False
            if event.key == pygame.K_d:
                mover_abajo = False  
            if event.key == pygame.K_s:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_izquierda = False
        
        
                
    pygame.display.update()  # actualiza la ventana

