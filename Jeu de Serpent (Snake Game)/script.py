import curses
import random

# Initialiser l'écran
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Initialiser le serpent et la nourriture
snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]
food = [sh // 2, sw // 2]
w.addch(food[0], food[1], curses.ACS_PI)

# Initialiser les touches
key = curses.KEY_RIGHT

# Boucle principale du jeu
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Calculer la nouvelle position de la tête du serpent
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Vérifier les collisions avec le bord de l'écran ou avec le corps du serpent
    if (
        new_head[0] in [0, sh] or
        new_head[1] in [0, sw] or
        new_head in snake
    ):
        curses.endwin()
        quit()

    # Insérer la nouvelle tête du serpent
    snake.insert(0, new_head)

    # Vérifier si le serpent mange la nourriture
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Supprimer la queue du serpent
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # Afficher le serpent
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
