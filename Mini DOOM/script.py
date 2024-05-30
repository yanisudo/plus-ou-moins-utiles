import pygame
import random
import math

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mini DOOM')

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Paramètres du jeu
player_size = 20
player_speed = 5
bullet_speed = 10
enemy_speed = 2

# Initialisation du joueur
player_pos = [screen_width // 2, screen_height // 2]
player_angle = 0

# Listes pour stocker les balles et les ennemis
bullets = []
enemies = []

# Fonction pour dessiner le joueur
def draw_player():
    pygame.draw.rect(screen, green, (player_pos[0] - player_size // 2, player_pos[1] - player_size // 2, player_size, player_size))

# Fonction pour dessiner une balle
def draw_bullet(bullet):
    pygame.draw.circle(screen, red, (int(bullet[0]), int(bullet[1])), 5)

# Fonction pour dessiner un ennemi
def draw_enemy(enemy):
    pygame.draw.circle(screen, black, (int(enemy[0]), int(enemy[1])), 10)

# Fonction pour tirer une balle
def shoot():
    angle_rad = math.radians(player_angle)
    bullet_dx = bullet_speed * math.cos(angle_rad)
    bullet_dy = -bullet_speed * math.sin(angle_rad)
    bullets.append([player_pos[0], player_pos[1], bullet_dx, bullet_dy])

# Fonction pour générer un ennemi aléatoire
def spawn_enemy():
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    enemies.append([x, y])

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(white)

    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot()

    # Gérer les entrées du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_angle += 5
    if keys[pygame.K_RIGHT]:
        player_angle -= 5
    if keys[pygame.K_UP]:
        player_pos[0] += player_speed * math.cos(math.radians(player_angle))
        player_pos[1] -= player_speed * math.sin(math.radians(player_angle))
    if keys[pygame.K_DOWN]:
        player_pos[0] -= player_speed * math.cos(math.radians(player_angle))
        player_pos[1] += player_speed * math.sin(math.radians(player_angle))

    # Mettre à jour les balles
    for bullet in bullets[:]:
        bullet[0] += bullet[2]
        bullet[1] += bullet[3]
        if bullet[0] < 0 or bullet[0] > screen_width or bullet[1] < 0 or bullet[1] > screen_height:
            bullets.remove(bullet)
        draw_bullet(bullet)

    # Mettre à jour les ennemis
    for enemy in enemies[:]:
        enemy[0] += enemy_speed * (player_pos[0] - enemy[0]) / screen_width
        enemy[1] += enemy_speed * (player_pos[1] - enemy[1]) / screen_height
        draw_enemy(enemy)

    # Dessiner le joueur
    draw_player()

    # Générer des ennemis aléatoires
    if random.random() < 0.01:
        spawn_enemy()

    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
