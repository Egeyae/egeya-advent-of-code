# Définition de la taille de l'écran
SCREEN_SIZE = (50, 6)


def get_lines():
    """
    Renvoie une liste contenant les commandes contenues dans le fichier d'entrée 
    """
    with open("inputs/day8.txt") as f:
        return [l.strip() for l in f.readlines()]


def get_screen():
    """
    Retourne une liste à 2 dimensions initialisée à 0, la taille est déterminée par SCREEN_SIZE
    """
    return [[0 for _ in range(SCREEN_SIZE[0])] for _ in range(SCREEN_SIZE[1])]


def show(screen):
    """
    Prend une liste à 2 dimensions et l'affiche dans le terminal
    """
    for row in screen:
        print("".join(["#" if cell == 1 else "." for cell in row]))


def rect(screen, x, y):
    """
    Crée un rectangle dans l'écran donné de taille x*y
    Paramètres:
        screen: liste à 2 dimensions représentant l'écran
        x: taille du rectangle en x
        y: taille du rectangle en y
    Retour:
        L'écran modifié
    """
    for yi in range(y):
        for xi in range(x):
            screen[yi][xi] = 1
    return screen


def rotate_column(screen, x, amount):
    """
    Effectue une rotation sur la colonne x d'un écran donné, en décalant les pixels vers le bas.
    
    Paramètres:
        screen: liste à 2 dimensions représentant l'écran
        x: index de la colonne à faire pivoter
        amount: nombre de positions à décaler la colonne vers le bas

    Retour:
        L'écran avec la colonne x mise à jour après la rotation.
    """
    column = [screen[y][x] for y in range(SCREEN_SIZE[1])]

    # Réalisation de la rotation: on prend les 'amount' derniers éléments qu'on place devant les autres
    column = column[-amount:] + column[:-amount]
    
    # On réintègre la colonne modifiée dans l'écran
    for y in range(SCREEN_SIZE[1]):
        screen[y][x] = column[y]
    
    return screen


def rotate_row(screen, y, amount):
    """
    Effectue une rotation sur la ligne y d'un écran donné, en décalant les pixels vers la droite.

    Paramètres:
        screen: liste à 2 dimensions représentant l'écran
        y: index de la ligne à faire pivoter
        amount: nombre de positions à décaler la ligne vers la droite

    Retour:
        L'écran avec la ligne y mise à jour après la rotation.
    """
    
    # Réalisation de la rotation de la ligne: on prend les 'amount' derniers éléments qu'on place au début
    screen[y] = screen[y][-amount:] + screen[y][:-amount]
    
    return screen


def parse_line(line):
    """
    Analyse une ligne de commande et renvoie la fonction correspondante ainsi que les arguments extraits.
    
    Paramètres:
        line: chaîne de caractères représentant la commande à analyser (ex. 'rect 3x2' ou 'rotate column x=1 by 1')

    Retour:
        Un tuple (fonction, arg1, arg2) où la fonction correspond à l'opération à effectuer
        et arg1, arg2 sont les arguments extraits de la commande.

    Erreur:
        Si la commande n'est pas reconnue, une exception ValueError est levée.
    """
    parts = line.split()
    
    if parts[0] == "rect":
        # Commande de type 'rect', on extrait les dimensions du rectangle
        x, y = map(int, parts[1].split("x"))
        return rect, x, y  # On renvoie la fonction rect et ses arguments
    elif parts[0] == "rotate":
        if parts[1] == "row":
            # Commande de rotation d'une ligne (ex: 'rotate row y=1 by 3')
            y = int(parts[2].split("=")[1])
            amount = int(parts[4])
            return rotate_row, y, amount  # On renvoie la fonction rotate_row et ses arguments
        elif parts[1] == "column":
            # Commande de rotation d'une colonne (ex: 'rotate column x=1 by 1')
            x = int(parts[2].split("=")[1])
            amount = int(parts[4])
            return rotate_column, x, amount  # On renvoie la fonction rotate_column et ses arguments
    # Si la commande n'est pas reconnue, on lève une exception
    raise ValueError(f"Unknown command: {line}")


def parse_line_and_exec(line, screen):
    """
    Analyse une ligne de commande, exécute l'opération correspondante et renvoie l'écran mis à jour.
    
    Paramètres:
        line: chaîne de caractères représentant la commande
        screen: liste à 2 dimensions représentant l'écran

    Retour:
        L'écran modifié après exécution de la commande.
    """
    # On analyse la ligne pour obtenir la fonction à exécuter et ses arguments
    func, arg1, arg2 = parse_line(line)
    
    # On exécute la fonction avec les arguments et on retourne l'écran modifié
    return func(screen, arg1, arg2)


def count_pixels(screen):
    """
    Compte le nombre de pixels allumés (valeur 1) sur l'écran.
    
    Paramètres:
        screen: liste à 2 dimensions représentant l'écran

    Retour:
        Le nombre total de pixels allumés.
    """
    # On utilise une double boucle pour sommer tous les pixels allumés dans l'écran
    s = 0
    for row in screen:
        for element in row:
            if element == 1:
                s += 1
    return s


def main():
    """
    Fonction principale. Elle lit les instructions, les exécute, puis affiche l'écran et le nombre total de pixels allumés.
    """
    # Lecture des instructions depuis le fichier
    lines = get_lines()
    
    # Initialisation de l'écran vide
    screen = get_screen()
    
    # Exécution de chaque commande sur l'écran
    for line in lines:
        screen = parse_line_and_exec(line, screen)
    
    # Affichage de l'écran final
    show(screen)
    
    # Affichage du nombre total de pixels allumés
    print("Total pixels:", count_pixels(screen))


main()
