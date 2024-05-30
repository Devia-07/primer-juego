import pygame
import constantes 
from personajes import Personaje
import juego
import os
import sys
import random
import pygame_textinput
from time import sleep
from juego import funciones


ecuaciones_cuadraticas = [
        ("x**2 - 4*x + 4 ", [2, 2, 0],[2,0],["R","y>=0"]),
        ("2*x**2 - 3*x + 1 ", [0.5, 1, 1],[0.75, -0.125],["R","y>=-0.125"]),
        ("3*x**2 + 6*x + 3 ", [-1, -1, 3],[-1, 0],["R","y>=0"]),
        ("x**2 + 5*x + 6 ", [-3, -2, 6],[-2.5,-0.25],["R","y>=-0.25"]),
        ("4*x**2 - 4*x + 1 ", [0.5, 0.5, 1],[0.5, 0],["R","y>=0"]),
        ]
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
for i in range(1, 5):
    img = pygame.image.load(f"assets//imagenes//characters//player//{i} imagen.png")
    img = escalar_imagen(img, constantes.escala_personaje)
    animaciones.append(img)

# enemigos:
directorio_enemigos = "assets\\imagenes\\characters\\enemigo"
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

# crear un jugador de la clase Personaje
jugador = Personaje(300, 700, animaciones)

# crear un enemigo de la clase Personaje
dragon = Personaje(1000, 400, animaciones_enemigos[0])

# crear una lista de enemigos
lista_enemigos = []
lista_enemigos.append(dragon)

# definir las variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

# con el frame rate
reloj = pygame.time.Clock()

# texto en la ventana
fuente = pygame.font.Font(None, 50)
lista_texto = juego.random_f()
texto = fuente.render(lista_texto, True, (255, 255, 255))

# Configuración del campo de texto
input_texto = ''
input_rect = pygame.Rect(900, 900, 140, 32)
color_activo = pygame.Color('lightskyblue3')
color_inactivo = pygame.Color('gray15')
color_actual = color_inactivo
activo = False

# para que la ventana no se cierre
run = True
while run:
    events = pygame.event.get()
    
    # que vaya a 60 fps
    reloj.tick(constantes.fps)
    
    # pinta el fondo de la ventana
    ventana.fill(constantes.color_bg)
    ventana.blit(texto, (200, 200))

    # Renderizar el texto actual del campo de texto
    txt_surface = fuente.render(input_texto, True, color_actual)
    input_rect.w = max(200, txt_surface.get_width() + 10)
    pygame.draw.rect(ventana, color_actual, input_rect, 2)
    ventana.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))

    # calcular el movimiento del jugador
    delta_X = 0
    delta_Y = 0
    
    if mover_derecha:
        delta_X = constantes.velocidad
    if mover_izquierda:
        delta_X = -constantes.velocidad
    if mover_arriba:
        delta_Y = -constantes.velocidad
    if mover_abajo:
        delta_Y = constantes.velocidad
    
    # mover el jugador
    jugador.movimiento(delta_Y, delta_X)
    # actualizar el jugador
    jugador.actualizar()
    # actualizar el enemigo
    dragon.actualizar()
    # dibuja el jugador en la ventana
    jugador.dibujar(ventana)
    # dibuja el enemigo en la ventana
    dragon.dibujar(ventana)

    for event in events:
        # para cerrar el juego
        if event.type == pygame.QUIT:
            run = False
        
        # input del usuario
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si el usuario hace clic dentro del rectángulo de entrada, activar el campo de texto
            if input_rect.collidepoint(event.pos):
                activo = not activo
            else:
                activo = False
            color_actual = color_activo if activo else color_inactivo
            
        if event.type == pygame.KEYDOWN:
            if activo:
                if event.key == pygame.K_RETURN:
                    
                    # Puedes procesar el texto aquí
                    if input_texto == "hola":
                        print("Correcto")
                    else:
                        print("Incorrecto")
                    input_texto = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_texto = input_texto[:-1]
                else:
                    input_texto += event.unicode


    pygame.display.update()  # actualiza la ventana

pygame.quit()

