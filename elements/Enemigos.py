"""
Hola este es modulo Bug,
este modulo manejara la creacion y acciones de los Bugs
"""
import pygame, math
import random
from pygame.locals import (RLEACCEL)
from elements.bullet import Bullet


class EnemigoPower(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, vida = 3):
        # nos permite invocar métodos o atributos de Sprite
        super(EnemigoPower, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 255, 0))
        #self.surf.set_colorkey((0, 255, 0), RLEACCEL)
        self.vida = int(vida)
        self.vidaMax = int(vida)
        self.exp_reward = 20

        # X
        minPosX = -100
        minExcludeX = 0
        maxPosX = SCREEN_WIDTH + 100
        maxExcludeX = SCREEN_WIDTH

        # Y
        minPosY = -100
        minExcludeY = 0
        maxPosY = SCREEN_HEIGHT + 100
        maxExcludeY = SCREEN_HEIGHT

        while True:
            posX = random.randint(minPosX, maxPosX)
            posY = random.randint(minPosY, maxPosY)
            if not (minExcludeX < posX < maxExcludeX and minExcludeY < posY < maxExcludeY):
                break


        self.rect = self.surf.get_rect(
            center=(
                posX,
                posY,
            )
        )
        self.speed = random.randint(1, 2)

        self.SCREEN_WIDTH = SCREEN_WIDTH   
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        self.balas = pygame.sprite.Group()

    def update(self, playerX, playerY):
        #Vida
        self.surf.fill((int(255 * (int(self.vidaMax)-int(self.vida))/int(self.vidaMax)), int(255 * (int(self.vida) / int(self.vidaMax))), 0))

        #Movimiento
        dx = playerX - self.rect.x
        dy = playerY - self.rect.y
        norm = math.sqrt(dx ** 2 + dy ** 2)
        dx = dx / norm
        dy = dy / norm

        self.rect.move_ip(dx * self.speed, dy * self.speed)
        

        if self.rect.right < -150 or self.rect.left > self.SCREEN_WIDTH + 150 or self.rect.bottom < -150 or self.rect.top > 150 + self.SCREEN_HEIGHT:
            self.kill()

        if pygame.time.get_ticks() % 1000 >= 900:
            new_bullet = Bullet(self.rect.x, self.rect.y, dx, dy, "enemigo", 1.2)
            self.balas.add(new_bullet)



class Jefe(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, vida = 1000):
        # nos permite invocar métodos o atributos de Sprite

        bossPng = pygame.image.load("assets/pixelBoss.png").convert()
        bossPngScaled = pygame.transform.scale(bossPng, (50, 50))

        super(Jefe, self).__init__()
        self.surf = bossPngScaled
        #self.surf.fill((0, 255, 0))
        #self.surf.set_colorkey((0, 255, 0), RLEACCEL)
        self.vida = int(vida)
        self.vidaMax = int(vida)
        self.exp_reward = 20


        self.rect = self.surf.get_rect(
            center=(
                900,
                350,
            )
        )
        self.speed = random.randint(1, 2)

        self.SCREEN_WIDTH = SCREEN_WIDTH   
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        self.balas = pygame.sprite.Group()

        self.clon = False

    def update(self, playerX, playerY):
        #Vida
        #self.surf.fill((int(255 * (int(self.vidaMax)-int(self.vida))/int(self.vidaMax)), int(255 * (int(self.vida) / int(self.vidaMax))), 0))

        dx = playerX - self.rect.x
        dy = playerY - self.rect.y
        norm = math.sqrt(dx ** 2 + dy ** 2)
        dx = dx / norm
        dy = dy / norm


        if pygame.time.get_ticks() % 1000 >= 900:
            new_bullet = Bullet(self.rect.x, self.rect.y, dx, dy, "enemigo", 3)
            self.balas.add(new_bullet)
        
            if self.clon:
                dx = playerX - 0
                dy = playerY - 0
                norm = math.sqrt(dx ** 2 + dy ** 2)
                dx = dx / norm
                dy = dy / norm

                new_bullet = Bullet(0, 0, dx, dy, "enemigo", 3)
                self.balas.add(new_bullet)
    
    def circulo(self, N):
        angle = 360 / N
        N = 30
        radius = 100

        offset = random.uniform(0, math.pi)
        for i in range(N):
            
            angle_rad = math.radians(angle * i + offset)
            x = self.rect.centerx + radius * math.cos(angle_rad + offset)
            y = self.rect.centery + radius * math.sin(angle_rad + offset)

            dx = x - self.rect.centerx 
            dy = y - self.rect.centery
            norm = math.sqrt(dx ** 2 + dy ** 2)
            dx = -dx / norm
            dy = -dy / norm

            new_bullet = Bullet(x, y, -dx, -dy, "enemigo", 1.2)
            self.balas.add(new_bullet)
        
        if self.clon:
            offset = random.uniform(0, math.pi)
            for i in range(N):
                
                angle_rad = math.radians(angle * i + offset)
                x = 0 + radius * math.cos(angle_rad + offset)
                y = 0 + radius * math.sin(angle_rad + offset)

                dx = x - 0
                dy = y - 0
                norm = math.sqrt(dx ** 2 + dy ** 2)
                dx = -dx / norm
                dy = -dy / norm

                new_bullet = Bullet(x, y, -dx, -dy, "enemigo", 1.2)
                self.balas.add(new_bullet)
        
  
    
    def muro(self):
        N = random.randint(30, 50)

        x = 980

        safe_space = 50

        safe_start = random.randint(safe_space, 700 - safe_space)

        for i in range(N):
            y = random.randint(0, 700)
            if safe_start - safe_space <= y <= safe_start + safe_space:
                pass
            else:
                dx = -3
                dy = 0

                new_bullet = Bullet(x, y, dx, dy, "enemigo", 1.2)
                self.balas.add(new_bullet)
        
        if self.clon:
            x = 10

            for i in range(N):
                y = random.randint(0, 700)
                if safe_start - safe_space <= y <= safe_start + safe_space:
                    pass
                else:
                    dx = 3
                    dy = 0

                    new_bullet = Bullet(x, y, dx, dy, "enemigo", 1.2)
                    self.balas.add(new_bullet)

    def Clon(self):
        pass




            
            

