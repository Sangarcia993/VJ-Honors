
import pygame, time

def TP(screen_copy, screen):
    print("TP")
    running = True
    square_size = 50
    square_x = screen.get_width() // 2 - square_size // 2
    square_y = screen.get_height() // 2 - square_size // 2

    
    time.sleep(0.01)


    while running:
        pygame.draw.rect(screen, (255, 255, 255), (square_x, square_y, square_size, square_size))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Salimos del TP")
                    return(square_x, square_y)

        
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            square_x -= 2
        if keys[pygame.K_RIGHT]:
            square_x += 2
        if keys[pygame.K_UP]:
            square_y -= 2
        if keys[pygame.K_DOWN]:
            square_y += 2

        transparent_copy = screen_copy
        transparent_copy.set_alpha(40)
        screen.blit(transparent_copy, (0, 0))

        if square_x < 0:
            square_x = 0
        if square_x > screen.get_width() - square_size:
            square_x = screen.get_width() - square_size
        if square_y < 0:
            square_y = 0
        if square_y > screen.get_height() - square_size:
            square_y = screen.get_height() - square_size

          # Draw the square
        pygame.draw.rect(screen, (255, 255, 255), (square_x, square_y, square_size, square_size))
        pygame.display.flip()  # Update the display



    pygame.quit()


