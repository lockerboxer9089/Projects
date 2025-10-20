"""
Improvements:
1. Make the program end if the word is guessed correctly
2. Make the program display the word in the game over screen
"""

import pygame, random 

pygame.init()

WIDTH = 800
HEIGHT = 600
BG_COLOR = (238, 240, 204)
WHITE = (255,255,255)
BLACK = (0,0,0)

with open('hangman_words.txt', 'r') as f:
    words = f.readlines()

words = [word.strip() for word in words]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

title_font = pygame.font.SysFont("Apple Chancery", 80)
word_font = pygame.font.SysFont("Bradley Hand", 50)

# Images
start_btn_image = pygame.image.load("5360348.png").convert_alpha()
end_btn_image = pygame.image.load("image-removebg-preview.png").convert_alpha()
img0 = pygame.image.load("0.jpg").convert()
img1 = pygame.image.load("1.jpg").convert()
img2 = pygame.image.load("2.jpg").convert()
img3 = pygame.image.load("3.jpg").convert()
img4 = pygame.image.load("4.jpg").convert()
img5 = pygame.image.load("5.jpg").convert()
img6 = pygame.image.load("6.jpg").convert()

random_word = random.choice(words).lower()
word = '_' * len(random_word)

allowed_letters = list('abcdefghijklmnopqrstuvwxyz')
found = False

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False 
        mouse_pos = pygame.mouse.get_pos()

        hovering = self.rect.collidepoint(mouse_pos)
        if hovering:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

# Buttons 
start_btn = Button(310, 300, start_btn_image, 0.35)
end_btn = Button(300, 415, end_btn_image, 0.25)

wrong_guesses = 0

clock = pygame.time.Clock()

state = 'intro'
final_message = ''

key_pressed = None

running = True
guessed = False

# Game Loop
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and state == "main":
            pressed = event.unicode.lower()
            if pressed in allowed_letters:
                key_pressed = pressed
                allowed_letters.remove(pressed)

    # Logic
    if state == 'main':
        if key_pressed and state == 'main':
            words_list = list(random_word)
            display_list = list(word)
            found = False
            for i in range(len(words_list)):
                if words_list[i] == key_pressed:
                    display_list[i] = key_pressed
                    found = True
            word = ''.join(display_list)
            if not found:
                wrong_guesses += 1 
        key_pressed = None

    key_pressed = None

    # Displaying Elements 
    if state == 'intro':
        screen.fill(BG_COLOR)
        title = title_font.render("Hangman", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - title.get_height()))

        if start_btn.draw():
            current_time = pygame.time.get_ticks()
            state = 'main'
            continue

    elif state == 'main' and (pygame.time.get_ticks() - current_time) >= 750:
        screen.fill(BLACK)

        display_word = ' '.join(word)
        word_to_guess = word_font.render(display_word, True, WHITE)
        screen.blit(word_to_guess, (WIDTH//2 - word_to_guess.get_width()//2, HEIGHT//2-250))

        hangman_images = [img0, img1, img2, img3, img4, img5, img6]
        current_image = hangman_images[wrong_guesses]
        screen.blit(current_image, (WIDTH//2-current_image.get_width()//2, HEIGHT//2-current_image.get_height()//2))

        if wrong_guesses == 6:
            pygame.display.flip()
            final_message = 'You Lost!'
            pygame.time.delay(2000)
            running = False

        if '_' not in word:
            pygame.display.flip()
            guessed = True
            final_message = 'You Guessed Correctly!'
            pygame.time.delay(2000)
            running = False

        if end_btn.draw():
            pygame.time.delay(1000)
            running = False

    # Updating Screen
    pygame.display.flip()
    clock.tick(60)

screen.fill(WHITE)

exit_text = title_font.render("Game Over!", True, BLACK)
result_text = title_font.render(final_message, True, BLACK)

screen.blit(exit_text, (WIDTH//2-exit_text.get_width()//2, HEIGHT//2-exit_text.get_height()))
screen.blit(result_text, (WIDTH//2-result_text.get_width()//2, HEIGHT//2+result_text.get_height()))

if not guessed:
    final_word_text = title_font.render(f"The word was {random_word}", True, BLACK) 
    screen.blit(final_word_text, (WIDTH//2-final_word_text.get_width()//2, HEIGHT//2-final_word_text.get_height()//3.5))
pygame.display.flip()
pygame.time.delay(2500)

pygame.quit()