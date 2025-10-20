import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (150, 150, 150)
font = pygame.font.SysFont("Chalkboard SE", 50)

player1_score = 0
player2_score = 0

player1_size = 80
player1_x, player1_y = 10, HEIGHT// 2 - player1_size // 2
player1_speed = 5

player2_size = 80
player2_x, player2_y = WIDTH - 10 - 10, HEIGHT//2 - player2_size // 2
player2_speed = 5

#ball
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_radius = 10
ball_speed_x = 4
ball_speed_y = 3  

ball_starttime = None
ball_delay = 1000

winner = ""

state = 'intro'

btn_width = 200
btn_height = 60
btn_x = WIDTH//2 - btn_width//2
btn_y = HEIGHT//2 + 50
btn_rect = pygame.Rect(btn_x, btn_y, btn_width, btn_height)

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if state == 'intro':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_rect.collidepoint(event.pos):
                    state = 'play'
                    ball_starttime = pygame.time.get_ticks()

    if state == 'intro':
        screen.fill(BLACK)

        text = font.render("Ping Pong", True, WHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 80))

        hovering = btn_rect.collidepoint(mouse_pos)

        btn_color = WHITE if hovering else GRAY
        pygame.draw.rect(screen, WHITE, btn_rect, 4, border_radius=15)

        btn_text = font.render("START", True, BLACK if hovering else WHITE)
        tx = btn_rect.centerx - btn_text.get_width()//2
        ty = btn_rect.centery - btn_text.get_height()//2
        screen.blit(btn_text, (tx, ty))

        pygame.display.flip()
        clock.tick(60)
        continue

    #keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        player1_y += player1_speed
    if keys[pygame.K_w]:
        player1_y -= player1_speed
    if keys[pygame.K_DOWN]:
        player2_y += player2_speed
    if keys[pygame.K_UP]:
        player2_y -= player2_speed

    if player1_score == 5 or player2_score == 5:
        if player1_score == 5:
            winner = "Player 1"
        else:
            winner = "Player 2"
        running = False
        continue

    screen.fill(BLACK)

    if ball_starttime is None or pygame.time.get_ticks() - ball_starttime >= ball_delay:
        ball_x += ball_speed_x
        ball_y += ball_speed_y

    if ball_y - ball_radius <= 0:
        ball_speed_y *= -1
    if ball_y + ball_radius >= HEIGHT:
        ball_speed_y *= -1

    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius*2, ball_radius*2)
    player1_rect = pygame.Rect(player1_x, player1_y, 10, player1_size)
    player2_rect = pygame.Rect(player2_x, player2_y, 10, player2_size)

    collision = ball_rect.colliderect(player1_rect) or ball_rect.colliderect(player2_rect)

    if collision:
        ball_speed_x *= -1

    if ball_x - ball_radius <= 0:
        ball_x = WIDTH//2 
        ball_y = HEIGHT//2
        ball_speed_x = 4
        ball_speed_y = random.randrange(-3, 3)
        player2_score += 1
        ball_starttime = pygame.time.get_ticks()
    if ball_x + ball_radius >= WIDTH:
        ball_x = WIDTH//2
        ball_y = HEIGHT//2
        ball_speed_x = -4
        ball_speed_y = random.randrange(-3, 3)
        player1_score += 1
        ball_starttime  = pygame.time.get_ticks()
    

    #drawing stuff
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (WIDTH//2-60, 20))
    screen.blit(player2_text, (WIDTH//2+40, 20))

    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 10)

    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, 10, player1_size))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, 10, player2_size))

    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)

    player1_y = max(0, min(HEIGHT - player1_size, player1_y))
    player2_y = max(0, min(HEIGHT - player2_size, player2_y))

    pygame.display.flip()

    clock.tick(120)

screen.fill(BLACK)
    
final_text = font.render(f"Winner is {winner}", True, WHITE)    
screen.blit(final_text, (WIDTH//2 - final_text.get_width()//2, HEIGHT//2 - final_text.get_height()))

pygame.display.flip()

pygame.time.delay(2000)

pygame.quit()