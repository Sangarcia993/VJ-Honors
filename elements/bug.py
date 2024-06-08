"""
Hola este es modulo Bug,
este modulo manejara la creacion y acciones de los Bugs
"""
import pygame, math
import random
from pygame.locals import (RLEACCEL)

BUGpng = pygame.image.load("assets/RomboAzul.png")
BUGpng_scaled = pygame.transform.scale(BUGpng, (64, 64))

class Enemy(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, speed = 3):
        # nos permite invocar métodos o atributos de Sprite
        super(Enemy, self).__init__()
        self.surf = BUGpng
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.vida = 0

        self.exp_reward = 10

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
        self.speed = speed

        self.SCREEN_WIDTH = SCREEN_WIDTH   
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

    def update(self, playerX, playerY):
        dx = playerX - self.rect.x
        dy = playerY - self.rect.y
        norm = math.sqrt(dx ** 2 + dy ** 2)
        dx = dx / norm
        dy = dy / norm


        self.rect.move_ip(dx * self.speed, dy * self.speed)
        if self.rect.right < -150 or self.rect.left > self.SCREEN_WIDTH + 150 or self.rect.bottom < -150 or self.rect.top > 150 + self.SCREEN_HEIGHT:
            self.kill()
