import pygame, time


def menuUpgrades(screen, screen_copy, player, DISPARO, seleccionado = 0):

    from elements.mejoras import dibujar


    habilidades = ["Cruz", "Canon", "Circulo de espadas"]
    NoSeHaSeleccionado = True

    while NoSeHaSeleccionado:
        screen.fill((0, 0, 0))  # Fill the screen with black (optional)

        transparent_copy = screen_copy
        transparent_copy.set_alpha(40)
        screen.blit(transparent_copy, (0, 0))

        #Seleccionamos 3 opciones
        Primero = habilidades[0]
        Segundo = habilidades[1]
        Tercero = habilidades[2] 

        #Dibujamos las opciones 

        dibujar(1, screen, image=pygame.image.load("assets/cruz.png"))
        dibujar(2, screen, image=pygame.image.load("assets/canon.png"))
        dibujar(3, screen, image=pygame.image.load("assets/circulo.png"))


        

        
                
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    seleccionado = (seleccionado - 1) % 3
                elif event.key == pygame.K_RIGHT:
                    seleccionado = (seleccionado + 1) % 3

                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if seleccionado == 0:
                        player.arma = "Cruz"
                    elif seleccionado == 1:
                        player.arma = "Canon"
                    elif seleccionado == 2:
                        player.arma = "circulo"
                    
                    NoSeHaSeleccionado = False
                    break
                    
                    
                
                time.sleep(0.2)
        


        #reajustar cosas despues de mejoras

        if seleccionado == 0:
            pygame.draw.rect(screen, (255, 215, 0), (200, 200, 100, 300), 5)
        elif seleccionado == 1:
            pygame.draw.rect(screen, (255, 215, 0), (450, 200, 100, 300), 5)
        elif seleccionado == 2:
            pygame.draw.rect(screen, (255, 215, 0), (700, 200, 100, 300), 5)
        
        pygame.display.flip()