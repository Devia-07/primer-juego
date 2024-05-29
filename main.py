import pygame
import constantes 
from personajes import Personaje


pygame.init()

# crear la ventana
ventana = pygame.display.set_mode((constantes.ancho, constantes.alto))


# titulo de la ventana
pygame.display.set_caption("Juego de Funciones")

def escalar_imagen(jugar_imagen, escala):
    return pygame.transform.scale(jugar_imagen,
                                        (jugar_imagen.get_width()*escala,
                                         jugar_imagen.get_height()*escala))
animaciones = []
for i in range(1,5):
    img = pygame.image.load(f"assets//imagenes//characters//player//{i} imagen.png")
    img = escalar_imagen(img, constantes.escala_personaje)
    animaciones.append(img)


jugador_imagen = pygame.image.load("assets//imagenes//characters//player//1 imagen.png")
jugador_imagen = escalar_imagen(jugador_imagen, constantes.escala_personaje)

jugador = Personaje(100, 100, animaciones)
# definir las varibles de movimiento del jugador

mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False




# con el frame rate
    
reloj = pygame.time.Clock()


# para que la ventana no se cierre

run = True
while run == True:
    
    # que vaya a 60 fps
    reloj.tick(constantes.fps)
    
    # pinta el fondo de la ventana
    ventana.fill(constantes.color_bg)  
    
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
    
    jugador.actualizar()
    
    # dibuja el jugador en la ventana
    
    jugador.dibujar(ventana)  
    
    
    
    
    for event in pygame.event.get():
        
        # para cerrar el juego
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

