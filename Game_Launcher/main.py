import pygame
import pygame_widgets as pw

pygame.init()

WIDTH,HEIGHT = 600,600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Launcher")
clock = pygame.time.Clock()

# Images
hangman_logo = pygame.image.load("hangman_logo.jpg").convert()
pong_logo = pygame.image.load("pong_logo.jpg").convert()

# Rects
hangman_rect = hangman_logo.get_rect()
pong_rect = pong_logo.get_rect()
hangman_rect.topleft = (50, 50)

running = True

# Main Game Loop
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Displaying Elements
    screen.blit(hangman_logo, hangman_rect)

    # Updating Display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()