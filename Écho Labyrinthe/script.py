import pygame
import random

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Écho Labyrinthe')

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
gray = (169, 169, 169)
blue = (0, 0, 255)

# Paramètres du jeu
tile_size = 40
num_tiles_x = screen_width // tile_size
num_tiles_y = screen_height // tile_size
player_pos = [1, 1]
exit_pos = [num_tiles_x - 2, num_tiles_y - 2]
echo_range = 2
echo_count = 0

# Création du labyrinthe (simple labyrinthe avec des murs aléatoires)
labyrinth = [[0 for _ in range(num_tiles_x)] for _ in range(num_tiles_y)]
for y in range(num_tiles_y):
    for x in range(num_tiles_x):
        if x == 0 or x == num_tiles_x - 1 or y == 0 or y == num_tiles_y - 1 or (random.random() < 0.2 and (x, y) != tuple(player_pos) and (x, y) != tuple(exit_pos)):
            labyrinth[y][x] = 1

# Fonction pour dessiner le labyrinthe
def draw_labyrinth():
    for y in range(num_tiles_y):
        for x in range(num_tiles_x):
            if labyrinth[y][x] == 1:
                pygame.draw.rect(screen, gray, (x * tile_size, y * tile_size, tile_size, tile_size))

# Fonction pour dessiner le joueur
def draw_player():
    pygame.draw.rect(screen, blue, (player_pos[0] * tile_size, player_pos[1] * tile_size, tile_size, tile_size))

# Fonction pour émettre un écho
def emit_echo():
    global echo_count
    echo_count += 1
    for dy in range(-echo_range, echo_range + 1):
        for dx in range(-echo_range, echo_range + 1):
            if 0 <= player_pos[1] + dy < num_tiles_y and 0 <= player_pos[0] + dx < num_tiles_x:
                if labyrinth[player_pos[1] + dy][player_pos[0] + dx] == 1:
                    pygame.draw.rect(screen, white, ((player_pos[0] + dx) * tile_size, (player_pos[1] + dy) * tile_size, tile_size, tile_size))

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(black)
    
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gérer les entrées du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and labyrinth[player_pos[1]][player_pos[0] - 1] == 0:
        player_pos[0] -= 1
    if keys[pygame.K_RIGHT] and labyrinth[player_pos[1]][player_pos[0] + 1] == 0:
        player_pos[0] += 1
    if keys[pygame.K_UP] and labyrinth[player_pos[1] - 1][player_pos[0]] == 0:
        player_pos[1] -= 1
    if keys[pygame.K_DOWN] and labyrinth[player_pos[1] + 1][player_pos[0]] == 0:
        player_pos[1] += 1

    # Émettre un écho si la touche ESPACE est pressée
    if keys[pygame.K_SPACE]:
        emit_echo()

    # Vérifier si le joueur atteint la sortie
    if player_pos == exit_pos:
        print(f"Vous avez trouvé la sortie en utilisant {echo_count} échos!")
        running = False

    # Dessiner le labyrinthe et le joueur
    draw_labyrinth()
    draw_player()

    # Afficher le nombre d'échos utilisés
    font = pygame.font.Font(None, 36)
    echo_text = f"Échos: {echo_count}"
    text_surface = font.render(echo_text, True, white)
    screen.blit(text_surface, (10, 10))

    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
