import pygame, subprocess, sys
from Button import Button

pygame.init()

WIDTH, HEIGHT = 800,600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Launcher")
clock = pygame.time.Clock()

# Images
hangman_logo = pygame.image.load("hangman_logo.jpg").convert()
pingpong_logo = pygame.image.load("pingpong_logo.jpg").convert()
exit_logo = pygame.image.load("/Users/vibhu/Documents/GitHub/Projects/Game_Launcher/image-removebg-preview.png").convert_alpha()

# Buttons
hangman_button = Button(150, 135, hangman_logo, .5, screen)
pingpong_button = Button(450, 135, pingpong_logo, .3, screen)
exit_button = Button(300, 450, exit_logo, .3, screen)

# Colors
WHITE = (255,255,255)
CUSTOM_COLOR = (155, 92, 196)

# Fonts
game_font = pygame.font.SysFont("DIN Alternate", 50)

running = True

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logic
    if hangman_button.check_hovering() or pingpong_button.check_hovering() or exit_button.check_hovering():
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Drawing elements
    screen.fill(CUSTOM_COLOR)

    if exit_button.draw():
        running = False
    if pingpong_button.draw():
        subprocess.run([sys.executable, "/Users/vibhu/Documents/GitHub/Projects/Pong/pong.py"])
    if hangman_button.draw():
        subprocess.run([sys.executable, "/Users/vibhu/Documents/GitHub/Projects/Hangman/hangman.py"])

    hangman_title = game_font.render("HANGMAN", True, WHITE)
    pingpong_title = game_font.render("PONG", True, WHITE)
    screen.blit(hangman_title, (125, 350))
    screen.blit(pingpong_title, (480, 350))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()