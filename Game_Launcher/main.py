import pygame

pygame.init()

class Button:
    def __init__(self, x, y, width, height, text, function=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.function = function
        self.onePress = onePress
        self.alreadyPressed = False
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333'
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(text, True, (20,20,20))
        objects.append(self)

    def process(self):
        mouse_pos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mouse_pos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.function()
                elif not self.alreadyPressed:
                    self.function()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = True
        
        self.buttonSurface.blit(self.buttonSurf, [])

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

    # Updating Display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()