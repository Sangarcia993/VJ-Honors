"""
Hola este es modulo Jorge,
este modulo manejara la creacion y movimiento de Jorge

foto de cavallero> https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.redbubble.com%2Fi%2Fart-board-print%2FPixel-Art-Knight-by-AdiDsgn%2F38497478.7Q6GI&psig=AOvVaw0razozSHZCsL-Cf2j2AbjF&ust=1711759162950000&source=images&cd=vfe&opi=89978449&ved=0CBQQjhxqFwoTCMDE5fadmIUDFQAAAAAdAAAAABAE

"""
import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL, K_SPACE)


JorgePNG = pygame.image.load("assets/Cavallero.png")
#JorgePNG_scaled = pygame.transform.scale(JorgePNG)

class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Player, self).__init__()
        self.surf = JorgePNG
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        self.vida = 3
        self.maxVida = 3
        self.life_regen = 0.001

        self.nivel = 0
        self.exp = 0

        self.attack_speed = 200
        self.bullet_speed = 2

        self.Orientada = False

        self.habilidad = ""
        self.habilidad_wait_time = 10 #segundos
        self.habilidad_usable = True
        self.habilidad_activa = False


        self.arma = ""

    def update(self, pressed_keys):
        
        if self.vida < self.maxVida:
            self.vida += self.life_regen

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -4)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 4)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-4, 0)

            if self.Orientada:
                self.surf = pygame.transform.flip(self.surf, True, False)
                self.Orientada = False

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(4, 0)

            if self.Orientada == False:
                self.surf = pygame.transform.flip(self.surf, True, False)
                self.Orientada = True
    
        if self.rect.left < 0:
            self.rect.left = 0 
        if self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.SCREEN_HEIGHT: 
            self.rect.bottom = self.SCREEN_HEIGHT
        