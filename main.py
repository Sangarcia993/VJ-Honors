"""
Hola este es modulo principal,
el codigo que al ejecutar pondra en marcha nuestro juego
"""
import pygame, math, cProfile
import scenes.game as GameScene

'''Inicio la escena de mi juego'''
SCREEN_WIDTH = 1000  # revisar ancho de la imagen de fondo
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load("assets/backmenu.png").convert()


"""https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.es%2Fpin%2F773985885952741484%2F&psig=AOvVaw1hEy4tNHIvYS9PTJnZjNVH&ust=1712162264552000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCND62c37o4UDFQAAAAAdAAAAABAE"""

pygame.font.init()
font = pygame.font.Font(None, 36) 
#menu



def main():

    pygame.mixer.init()
    pygame.mixer.music.load("assets/[Mix]The Toxic Avenger - My Only Chance to Make This Right.wav")
    pygame.mixer.music.play(-1)

    """"""

    while True:
    
        with open("score.txt", "r") as puntaje:
            score = puntaje.readlines()
            #print("score:", score)
            scores = []
            for i in score:
                try:
                    scores.append(float(i.strip()))
                except:
                    pass


            if len(scores) >= 3:
                score1 = scores[0]
                score2 = scores[1]
                score3 = scores[2]
            elif len(scores) == 2:
                score1 = scores[0]
                score2 = scores[1]
                score3 = 0
            elif len(scores) == 1:
                score1 = scores[0]
                score2 = score3 = 0
            else:
                score1 = score2 = score3 = 0

        screen.blit(background_image, [0, 0])

        text_surface = font.render("Presiona enter para jugar", True, (255, 255, 255))
        screen.blit(text_surface, (100, 350))

        text_surface = font.render("O esc para salir", True, (255, 255, 255))
        screen.blit(text_surface, (100, 400))

        

        text_surface = font.render("Record a vencer:", True, (255, 255, 255))
        screen.blit(text_surface, (600, 100))

        text_surface = font.render(str(score1), True, (255, 255, 255))
        screen.blit(text_surface, (600, 120))

        if len(scores) >= 2:
            text_surface = font.render(str(score2), True, (255, 255, 255))
            screen.blit(text_surface, (600, 150))

            if len(scores) >= 3:
                text_surface = font.render(str(score3), True, (255, 255, 255))
                screen.blit(text_surface, (600, 180))


        

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    GameScene.StartScene()
                if event.key == pygame.K_ESCAPE:
                    """with open("score.txt", "w") as puntaje:
                        puntaje.write("")"""
                    #print("Se cerro el programa")
                    pygame.quit()
            elif event.type == pygame.QUIT:
                
                """with open("score.txt", "w") as puntaje:
                    pass
                    puntaje.write("")"""
                
                #print("Se cerro el programa")
                pygame.quit()
                

        pygame.display.flip()

cProfile.run("main()", sort="cumtime")
#main()