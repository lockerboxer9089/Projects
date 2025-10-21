import pygame

class Button:
    def __init__(self, x, y, image, scale, screen):
        self.x = x
        self.y = y
        self.scale = scale
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.screen = screen

    def draw(self): 
        mouse_pos = pygame.mouse.get_pos()

        action = False

        hovering = self.rect.collidepoint(mouse_pos)
        if hovering:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
    
    def check_hovering(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)