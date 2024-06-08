import pygame

def dibujar(position, screen, color=(0, 255, 0), image=None):
    screen_width = 1000  # Width of the screen
    screen_height = 700  # Height of the screen
    rectangle_width = 100  # Width of the rectangle
    rectangle_height = 300  # Height of the rectangle

    if position == 1:
        x = screen_width // 4 - rectangle_width // 2  # Position the rectangle in the first third of the screen
    elif position == 2:
        x = screen_width // 2 - rectangle_width // 2  # Position the rectangle in the second third of the screen
    elif position == 3:
        x = 3 * screen_width // 4 - rectangle_width // 2  # Position the rectangle in the last third of the screen
    elif position == -1:
        pass
    else:
        raise ValueError("Invalid position. Position must be 1, 2, or 3.")

    y = screen_height // 2 - rectangle_height // 2  # Position the rectangle vertically in the middle of the screen

    if image == None:
        pygame.draw.rect(screen, color, (x, y, rectangle_width, rectangle_height))
    else:
        screen.blit(image, (x, y))


def AttackeRapido(position = -1, screen = None, color=(0, 255, 0), seleccionado = False, player = None, image=pygame.image.load("assets/AttackeRapido.png").convert() ):
    
    # Draw the rectangle using your preferred graphics library or method
    if screen == None:
        pass
    else:
        dibujar(position, screen, image = image)
    
    if seleccionado:
        player.attack_speed -= 50
        if player.attack_speed <= 0:
            player.attack_speed = 49
            print("No puedes tener un ataque tan rapido")


def BalasRapidas(position = -1, screen = None, color=(255, 0, 0), seleccionado = False, bullet_speed = None, player = None, image=pygame.image.load("assets/Balasrapidas.png").convert()):
    if screen == None:
        pass
    else:
        dibujar(position, screen, image=image)
    
    if seleccionado:
        player.bullet_speed = player.bullet_speed * 1.1
        if player.bullet_speed >= 2.5:
            player.bullet_speed = 2.49
            print("No puedes tener balas tan rapidas")

def MasVida(position = -1, screen = None, color=(0, 0, 0), seleccionado = False, player = None, image=pygame.image.load("assets/MasVida.png").convert()): 
    if screen == None:
        pass
    else:
        dibujar(position, screen, image=image)
    
    if seleccionado:
        player.vida += 1
        player.maxVida += 1

def LifeRegen(position = -1, screen = None, color=(0, 0, 255), seleccionado = False, player = None, image = pygame.image.load("assets/LifeRegen.png").convert()):
    if screen == None:
        pass
    else:
        dibujar(position, screen, image=image)
    
    if seleccionado:
        player.life_regen = player.life_regen * 2





    

# Example usage:
#draw_rectangle(1)  # Draw the rectangle in the first position