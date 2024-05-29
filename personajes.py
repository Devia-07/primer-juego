import pygame


class Personaje ():
    def __init__(self, x, y, animaciones):  # coordenas donde inicializa el personake
        self.flip = False # variable para saber si el personaje esta volteado
        self.animaciones = animaciones
        
        # imagen de la animacion que se esta mostrando actualmente
        
        self.frame_index = 0
        # Aqui se almacena la hora actual(en milisegundos desde que se inicio el juego)
        
        self.animacion_actual =  pygame.time.get_ticks()
        
        self.image = animaciones[self.frame_index] # cambia el tamaño de la imagen
        self.forma = pygame.Rect(0, 0, 50, 50)  # crea un rectangulo en la coordenadas 0,0 de 50x50
        self.forma.center = (x, y) # centra el rectangulo en las coordenadas x,y
        
    def actualizar(self):
        cooldown_animacion = 100  # tiempo que dura cada frame de la animacion
        self.image = self.animaciones[self.frame_index]  # cambia la imagen del personaje
        if pygame.time.get_ticks() - self.animacion_actual >= cooldown_animacion:
            self.frame_index += 1
            self.animacion_actual = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0 
            
    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False )  # voltea la imagen
        interfaz.blit(imagen_flip, self.forma)  
        #  pygame.draw.rect(interfaz, (255, 0, 0), self.forma, 1)  # dibuja el rectangulo en la ventana con el color rojo
        
    
    def movimiento(self, delta_x, delta_y,):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False
            
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
        






























#_________________________________________________

# class personaje_circle():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.radio = 25
        
#     def dibujar(self, interfaz):
#         pygame.draw.circle(interfaz, (0, 255, 0), (self.x, self.y), self.radio)
    
#     def movimiento(self, delta_x, delta_y):
#         self.x = self.x + delta_x
#         self.y = self.y + delta_y