import pygame
import random

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simulation de Vie')

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
creature_size = 10
food_size = 5
num_creatures = 20
num_food = 50
num_predators = 5
mutation_rate = 0.1

# Cycle jour/nuit et saisons
day_length = 300
night_length = 150
season_length = day_length + night_length
cycle_length = season_length * 4  # 4 saisons
current_cycle = 0
current_season = "Printemps"

# Événements aléatoires
event_probability = 0.01  # Probabilité d'un événement à chaque tick
event_duration = 100
current_event = None
event_timer = 0

# Chargement des images
creature_img = pygame.Surface((creature_size, creature_size))
creature_img.fill(green)
predator_img = pygame.Surface((creature_size, creature_size))
predator_img.fill(yellow)
food_img = pygame.Surface((food_size, food_size))
food_img.fill(blue)
shelter_img = pygame.Surface((20, 20))
shelter_img.fill(brown)

# Classes pour les créatures, les prédateurs, la nourriture et les abris
class Creature:
    def __init__(self, x=None, y=None, speed=None, vision=None, energy=100):
        self.x = x if x is not None else random.randint(0, screen_width - creature_size)
        self.y = y if y is not None else random.randint(0, screen_height - creature_size)
        self.speed = speed if speed is not None else random.uniform(1, 3)
        self.vision = vision if vision is not None else random.uniform(50, 150)
        self.energy = energy

    def move(self):
        self.x += random.uniform(-self.speed, self.speed)
        self.y += random.uniform(-self.speed, self.speed)
        self.x = max(0, min(self.x, screen_width - creature_size))
        self.y = max(0, min(self.y, screen_height - creature_size))
        self.energy -= 0.5  # Réduction de la perte d'énergie

    def eat(self, food):
        if (self.x < food.x + food_size and
            self.x + creature_size > food.x and
            self.y < food.y + food_size and
            self.y + creature_size > food.y):
            self.energy += 50  # Augmentation de l'énergie gagnée
            return True
        return False

    def use_shelter(self, shelter):
        if (self.x < shelter.x + 20 and
            self.x + creature_size > shelter.x and
            self.y < shelter.y + 20 and
            self.y + creature_size > shelter.y):
            self.energy += 10
            return True
        return False

    def reproduce(self):
        if self.energy > 120:  # Reproduction plus fréquente
            self.energy = 100
            return Creature(
                x=self.x,
                y=self.y,
                speed=self.speed * random.uniform(1 - mutation_rate, 1 + mutation_rate),
                vision=self.vision * random.uniform(1 - mutation_rate, 1 + mutation_rate),
                energy=50
            )
        return None

    def draw(self):
        color = green if self.energy > 50 else red
        img = creature_img.copy()
        img.fill(color)
        screen.blit(img, (self.x, self.y))

class Predator(Creature):
    def __init__(self, x=None, y=None, speed=None, vision=None, energy=100):
        super().__init__(x, y, speed, vision, energy)

    def eat(self, creature):
        if (self.x < creature.x + creature_size and
            self.x + creature_size > creature.x and
            self.y < creature.y + creature_size and
            self.y + creature_size > creature.y):
            self.energy += 50
            return True
        return False

    def draw(self):
        screen.blit(predator_img, (self.x, self.y))

class Food:
    def __init__(self):
        self.x = random.randint(0, screen_width - food_size)
        self.y = random.randint(0, screen_height - food_size)

    def draw(self):
        screen.blit(food_img, (self.x, self.y))

class Shelter:
    def __init__(self):
        self.x = random.randint(0, screen_width - 20)
        self.y = random.randint(0, screen_height - 20)

    def draw(self):
        screen.blit(shelter_img, (self.x, self.y))

# Initialiser les créatures, les prédateurs, la nourriture et les abris
creatures = [Creature() for _ in range(num_creatures)]
predators = [Predator() for _ in range(num_predators)]
foods = [Food() for _ in range(num_food)]
shelters = [Shelter() for _ in range(5)]

# Fonction pour gérer les événements aléatoires
def random_event():
    global current_event, event_timer
    event = random.choice(["tempête", "feu de forêt", "sécheresse", "épidémie"])
    current_event = event
    event_timer = event_duration
    if event == "tempête":
        for creature in creatures:
            creature.speed *= 0.5
        for predator in predators:
            predator.speed *= 0.5
    elif event == "feu de forêt":
        for _ in range(10):
            foods.append(Food())
    elif event == "sécheresse":
        for food in foods[:]:
            if random.random() < 0.5:
                foods.remove(food)
    elif event == "épidémie":
        for creature in creatures[:]:
            if random.random() < 0.5:
                creatures.remove(creature)

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
while running:
    # Mise à jour du cycle jour/nuit et saison
    if current_cycle < day_length:
        screen.fill(white)
    else:
        screen.fill(gray)
    if current_cycle < season_length:
        current_season = "Printemps"
    elif current_cycle < season_length * 2:
        current_season = "Été"
    elif current_cycle < season_length * 3:
        current_season = "Automne"
    else:
        current_season = "Hiver"
    
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déclencher des événements aléatoires
    if random.random() < event_probability and current_event is None:
        random_event()

    # Mettre à jour et dessiner les créatures
    new_creatures = []
    for creature in creatures:
        creature.move()
        creature.draw()
        new_creature = creature.reproduce()
        if new_creature:
            new_creatures.append(new_creature)

    # Mettre à jour et dessiner les prédateurs
    for predator in predators:
        predator.move()
        predator.draw()

    # Dessiner la nourriture
    for food in foods:
        food.draw()

    # Dessiner les abris
    for shelter in shelters:
        shelter.draw()

    # Vérifier si les créatures mangent la nourriture
    for creature in creatures:
        for food in foods:
            if creature.eat(food):
                foods.remove(food)
                foods.append(Food())

    # Vérifier si les créatures utilisent les abris
    for creature in creatures:
        for shelter in shelters:
            if creature.use_shelter(shelter):
                shelters.remove(shelter)
                shelters.append(Shelter())

    # Vérifier si les prédateurs mangent les créatures
    for predator in predators:
        for creature in creatures:
            if predator.eat(creature):
                creatures.remove(creature)

    # Vérifier si les créatures meurent
    creatures = [creature for creature in creatures if creature.energy > 0]

    # Réinitialiser les populations si nécessaire
    if not creatures:
        creatures = [Creature() for _ in range(num_creatures)]
    if not foods:
        foods = [Food() for _ in range(num_food)]
    if not predators:
        predators = [Predator() for _ in range(num_predators)]

    # Gérer la fin des événements
    if current_event:
        event_timer -= 1
        if event_timer <= 0:
            if current_event == "tempête":
                for creature in creatures:
                    creature.speed *= 2
                for predator in predators:
                    predator.speed *= 2
            current_event = None

    # Mettre à jour le cycle jour/nuit
    current_cycle = (current_cycle + 1) % cycle_length

    # Afficher les informations
    font = pygame.font.Font(None, 36)
    info_text = f"Saison: {current_season}  Créatures: {len(creatures)}  Prédateurs: {len(predators)}  Nourriture: {len(foods)}"
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
