import math, pygame

SCREEN_WIDTH = 1000  # revisar ancho de la imagen de fondo
SCREEN_HEIGHT = 700



# 1. Create the Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, tipo = "jugador", velocidad = 1):


        super().__init__()
        self.radius = 5  # Set the radius of the circle
        self.surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        
        self.color = (0, 255, 0)  # Set the color to green
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)


        self.dx = dx
        self.dy = dy
        self.velocidad = velocidad

        if tipo != "jugador":
            self.color = (255, 165, 0)
            self.surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        
        pygame.draw.circle(self.surf, self.color, (self.radius, self.radius), self.radius)

    def update(self, ContraJefe = False, jefeX = 0, jefeY = 0):
        
            #self.rect.move_ip(self.dx, self.dy)
        if not ContraJefe:


            self.rect.x += self.dx * self.velocidad
            self.rect.y += self.dy * self.velocidad
            # Remove the bullet if it's off-screen
            if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
                self.kill()

        else:
            dx = 820 - self.rect.x
            dy = 360 - self.rect.y
            norm = math.sqrt(dx ** 2 + dy ** 2)
            if norm != 0:
                dx = dx / norm 
                dy = dy / norm
            else:
                dx = 0
                dy = 0

            self.rect.x += dx * self.velocidad
            self.rect.y += dy * self.velocidad

            if self.rect.right < -150 or self.rect.left > SCREEN_WIDTH + 150 or self.rect.bottom < -150 or self.rect.top > 150 + SCREEN_HEIGHT:
                self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)





