import random

class Game:
    def __init__(self):
        self.rooms = {
            "hall": {
                "description": "Vous êtes dans le hall. Il y a des portes au nord, au sud, à l'est et à l'ouest.",
                "exits": {"nord": "bibliothèque", "sud": "cuisine", "est": "salle à manger", "ouest": "jardin"},
                "items": [],
                "puzzle": None,
                "pnj": None
            },
            "bibliothèque": {
                "description": "Vous êtes dans la bibliothèque. Des livres poussiéreux tapissent les murs. Il y a une porte au sud.",
                "exits": {"sud": "hall"},
                "items": ["clé"],
                "puzzle": None,
                "pnj": None
            },
            "cuisine": {
                "description": "Vous êtes dans la cuisine. Il y a une étrange odeur. Il y a une porte au nord.",
                "exits": {"nord": "hall"},
                "items": ["pomme"],
                "puzzle": "four",
                "pnj": None
            },
            "salle à manger": {
                "description": "Vous êtes dans la salle à manger. La table est dressée pour le dîner. Il y a une porte à l'ouest.",
                "exits": {"ouest": "hall"},
                "items": [],
                "puzzle": "table",
                "pnj": "fantôme"
            },
            "jardin": {
                "description": "Vous êtes dans le jardin. Les fleurs sont en pleine floraison. Il y a une porte à l'est.",
                "exits": {"est": "hall"},
                "items": ["épée"],
                "puzzle": None,
                "pnj": "chat"
            }
        }
        self.current_room = "hall"
        self.inventory = []
        self.game_over = False
        self.solved_puzzles = set()
        self.treasures_found = 0

    def print_welcome(self):
        print("Bienvenue dans l'aventure de la Maison Hantée !")
        print("Tapez 'exit' pour quitter le jeu.")
        print("Tapez 'inventaire' pour voir ce que vous avez ramassé.")
        print("Tapez 'prendre [objet]' pour ramasser un objet.")
        print("Tapez 'utiliser [objet]' pour utiliser un objet.")
        print("Tapez 'parler [pnj]' pour parler à un personnage.")

    def print_room_description(self):
        room = self.rooms[self.current_room]
        print(room["description"])
        if room["items"]:
            print("Objets présents : " + ", ".join(room["items"]))
        if room["puzzle"]:
            print("Il y a quelque chose d'inhabituel ici : " + room["puzzle"])
        if room["pnj"]:
            print("Il y a quelqu'un ici : " + room["pnj"])

    def get_command(self):
        command = input("> ").strip().lower()
        return command

    def execute_command(self, command):
        if command == "exit":
            self.game_over = True
        elif command.startswith("prendre "):
            item = command.split("prendre ")[1]
            self.take_item(item)
        elif command.startswith("utiliser "):
            item = command.split("utiliser ")[1]
            self.use_item(item)
        elif command.startswith("parler "):
            pnj = command.split("parler ")[1]
            self.talk_to_pnj(pnj)
        elif command == "inventaire":
            self.show_inventory()
        elif command in ["nord", "sud", "est", "ouest"]:
            self.move(command)
        else:
            print("Commande invalide. Essayez 'nord', 'sud', 'est', 'ouest', 'prendre [objet]', 'utiliser [objet]', 'parler [pnj]', ou 'inventaire'.")

    def take_item(self, item):
        room = self.rooms[self.current_room]
        if item in room["items"]:
            self.inventory.append(item)
            room["items"].remove(item)
            print(f"Vous avez ramassé {item}.")
        else:
            print(f"Il n'y a pas de {item} ici.")

    def use_item(self, item):
        room = self.rooms[self.current_room]
        if item in self.inventory:
            if room["puzzle"] == "four" and item == "pomme":
                self.solve_puzzle("four")
            elif room["puzzle"] == "table" and item == "clé":
                self.solve_puzzle("table")
            else:
                print(f"Vous ne pouvez pas utiliser {item} ici.")
        else:
            print(f"Vous n'avez pas de {item}.")

    def talk_to_pnj(self, pnj):
        room = self.rooms[self.current_room]
        if room["pnj"] == pnj:
            if pnj == "fantôme":
                print("Le fantôme vous murmure : 'Trouve la clé et libère-moi...'.")
            elif pnj == "chat":
                print("Le chat vous regarde et miaule : 'Miaou... Suivez-moi dans la bibliothèque.'.")
        else:
            print(f"Il n'y a pas de {pnj} ici.")

    def solve_puzzle(self, puzzle):
        if puzzle == "four":
            print("Vous placez la pomme dans le four et il s'ouvre magiquement, révélant une clé dorée !")
            self.inventory.append("clé dorée")
            self.rooms["cuisine"]["items"].append("clé dorée")
            self.solved_puzzles.add(puzzle)
        elif puzzle == "table":
            print("Vous utilisez la clé pour ouvrir un tiroir caché sous la table. Vous trouvez une carte au trésor !")
            self.inventory.append("carte au trésor")
            self.solved_puzzles.add(puzzle)
            self.treasures_found += 1
            self.check_victory()

    def check_victory(self):
        if self.treasures_found >= 2:
            print("Félicitations ! Vous avez trouvé tous les trésors et libéré la maison de sa malédiction !")
            self.game_over = True

    def show_inventory(self):
        if self.inventory:
            print("Votre inventaire contient : " + ", ".join(self.inventory))
        else:
            print("Votre inventaire est vide.")

    def move(self, direction):
        room = self.rooms[self.current_room]
        if direction in room["exits"]:
            self.current_room = room["exits"][direction]
            self.print_room_description()
        else:
            print("Vous ne pouvez pas aller dans cette direction.")

    def start(self):
        self.print_welcome()
        self.print_room_description()

        while not self.game_over:
            command = self.get_command()
            self.execute_command(command)

if __name__ == "__main__":
    game = Game()
    game.start()
