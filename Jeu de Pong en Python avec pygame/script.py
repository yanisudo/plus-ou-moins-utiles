import pygame
import random

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)

# Paramètres du jeu
ball_radius = 10
paddle_width = 15
paddle_height = 100
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
paddle_speed = 10

# Positions initiales
ball_x = screen_width // 2
ball_y = screen_height // 2
player1_y = screen_height // 2 - paddle_height // 2
player2_y = screen_height // 2 - paddle_height // 2
player1_score = 0
player2_score = 0

# Polices de texte
font = pygame.font.Font(None, 74)

def draw_ball(x, y):
    pygame.draw.circle(screen, white, (x, y), ball_radius)

def draw_paddle(x, y):
    pygame.draw.rect(screen, white, (x, y, paddle_width, paddle_height))

def draw_score(score, x, y):
    text = font.render(str(score), True, white)
    screen.blit(text, (x, y))

# Boucle principale du jeu
running = True
while running:
    screen.fill(black)
    
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Mouvement des raquettes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
        player2_y += paddle_speed
    
    # Mouvement de la balle
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Collisions avec les murs
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        ball_speed_y *= -1

    # Collisions avec les raquettes
    if (ball_x - ball_radius <= paddle_width and player1_y < ball_y < player1_y + paddle_height) or \
       (ball_x + ball_radius >= screen_width - paddle_width and player2_y < ball_y < player2_y + paddle_height):
        ball_speed_x *= -1

    # Marquer des points
    if ball_x < 0:
        player2_score += 1
        ball_x, ball_y = screen_width // 2, screen_height // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    if ball_x > screen_width:
        player1_score += 1
        ball_x, ball_y = screen_width // 2, screen_height // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Dessiner les éléments
    draw_ball(ball_x, ball_y)
    draw_paddle(0, player1_y)
    draw_paddle(screen_width - paddle_width, player2_y)
    draw_score(player1_score, screen_width // 4, 20)
    draw_score(player2_score, screen_width * 3 // 4, 20)

    # Mettre à jour l'affichage
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
