import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.colliderect(mouse_pos):
            print("Colission")

pygame.init()

WIDTH,HEIGHT = 600,600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Launcher")
clock = pygame.time.Clock()

# Images
hangman_logo = pygame.image.load("hangman_logo.jpg").convert()
pong_logo = pygame.image.load("pong_logo.jpg").convert()

submit = Button(120, 240, 60, 60, "hi", "blue", "blue", True)

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