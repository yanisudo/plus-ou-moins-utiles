import pygame
import random

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Terraformers')

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
gray = (169, 169, 169)
brown = (139, 69, 19)

# Paramètres du jeu
tile_size = 20
num_tiles_x = screen_width // tile_size
num_tiles_y = screen_height // tile_size

# Ressources
water = 100
food = 100
energy = 100

# Cycle jour/nuit
day_length = 300
night_length = 150
cycle_length = day_length + night_length
current_cycle = 0

# Événements aléatoires
event_probability = 0.01  # Probabilité d'un événement à chaque tick
event_duration = 100
current_event = None
event_timer = 0

# Chargement des images
plant_img = pygame.Surface((tile_size, tile_size))
plant_img.fill(green)
animal_img = pygame.Surface((tile_size, tile_size))
animal_img.fill(brown)
water_img = pygame.Surface((tile_size, tile_size))
water_img.fill(blue)
energy_img = pygame.Surface((tile_size, tile_size))
energy_img.fill(yellow)

# Classes pour les plantes, les animaux et les ressources
class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(plant_img, (self.x * tile_size, self.y * tile_size))

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 50

    def move(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        self.x = max(0, min(self.x, num_tiles_x - 1))
        self.y = max(0, min(self.y, num_tiles_y - 1))
        self.energy -= 1

    def draw(self):
        screen.blit(animal_img, (self.x * tile_size, self.y * tile_size))

class Resource:
    def __init__(self, x, y, resource_type):
        self.x = x
        self.y = y
        self.resource_type = resource_type

    def draw(self):
        if self.resource_type == "water":
            screen.blit(water_img, (self.x * tile_size, self.y * tile_size))
        elif self.resource_type == "food":
            screen.blit(plant_img, (self.x * tile_size, self.y * tile_size))
        elif self.resource_type == "energy":
            screen.blit(energy_img, (self.x * tile_size, self.y * tile_size))

# Initialiser les plantes, les animaux et les ressources
plants = [Plant(random.randint(0, num_tiles_x - 1), random.randint(0, num_tiles_y - 1)) for _ in range(10)]
animals = [Animal(random.randint(0, num_tiles_x - 1), random.randint(0, num_tiles_y - 1)) for _ in range(5)]
resources = [Resource(random.randint(0, num_tiles_x - 1), random.randint(0, num_tiles_y - 1), random.choice(["water", "food", "energy"])) for _ in range(20)]

# Fonction pour gérer les événements aléatoires
def random_event():
    global current_event, event_timer
    event = random.choice(["tempête de poussière", "chute de météores"])
    current_event = event
    event_timer = event_duration
    if event == "tempête de poussière":
        for animal in animals:
            animal.energy -= 10
    elif event == "chute de météores":
        for _ in range(5):
            resources.append(Resource(random.randint(0, num_tiles_x - 1), random.randint(0, num_tiles_y - 1), random.choice(["water", "food", "energy"])))

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
while running:
    # Mise à jour du cycle jour/nuit
    if current_cycle < day_length:
        screen.fill(white)
    else:
        screen.fill(gray)
    
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déclencher des événements aléatoires
    if random.random() < event_probability and current_event is None:
        random_event()

    # Mettre à jour et dessiner les plantes
    for plant in plants:
        plant.draw()

    # Mettre à jour et dessiner les animaux
    for animal in animals:
        animal.move()
        animal.draw()

    # Dessiner les ressources
    for resource in resources:
        resource.draw()

    # Vérifier si les animaux consomment les ressources
    for animal in animals:
        for resource in resources:
            if animal.x == resource.x and animal.y == resource.y:
                if resource.resource_type == "water":
                    water += 10
                elif resource.resource_type == "food":
                    food += 10
                elif resource.resource_type == "energy":
                    energy += 10
                resources.remove(resource)
                break

    # Vérifier si les animaux meurent
    animals = [animal for animal in animals if animal.energy > 0]

    # Réinitialiser les populations si nécessaire
    if not animals:
        animals = [Animal(random.randint(0, num_tiles_x - 1), random.randint(0, num_tiles_y - 1)) for _ in range(5)]
    if len(resources) < 20:
        resources.append(Resource(random.randint(0, num_tiles_x - 1), random.randint(0, num_tiles_y - 1), random.choice(["water", "food", "energy"])))

    # Gérer la fin des événements
    if current_event:
        event_timer -= 1
        if event_timer <= 0:
            current_event = None

    # Mettre à jour le cycle jour/nuit
    current_cycle = (current_cycle + 1) % cycle_length

    # Afficher les informations
    font = pygame.font.Font(None, 36)
    info_text = f"Eau: {water}  Nourriture: {food}  Énergie: {energy}"
    text_surface = font.render(info_text, True, black)
    screen.blit(text_surface, (10, 10))
    if current_event:
        event_text = f"Événement: {current_event} ({event_timer})"
        event_surface = font.render(event_text, True, black)
        screen.blit(event_surface, (10, 50))

    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
