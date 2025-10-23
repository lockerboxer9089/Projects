import pygame

pygame.init()

class Button:
    def __init__(self, x, y, text, enabled):
        self.x = x
        self.y = y
        self.text = text
        self.enabled = enabled
        self.draw()

    def draw(self):
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x, self.y), (150,25))
        pygame.draw.rect(screen, 'gray', button_rect, 0, 5)
        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x+3, self.y+3))

WIDTH,HEIGHT = 600,600
objects = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Launcher")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 40)

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
    button = Button('Click me!', 10, 10, True)

    # Updating Display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()