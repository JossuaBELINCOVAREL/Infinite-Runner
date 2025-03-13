import pygame

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Infinite Runner")

# Couleur de fond
background_color = (100, 100, 250)

# Création du personnage
player_width = 50
player_height = 50
player_x = 50  # Position initiale à gauche
player_y = 550  # Position verticale (au bas de la fenêtre)
player = pygame.Rect(player_x, player_y, player_width, player_height)


# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour des coordonnées du personnage
    player.x += 0.5

    # Couleur de fond
    screen.fill(background_color)

    # Dessin du personnage
    pygame.draw.rect(screen, (255, 100, 0), player)

    # Actualisation de l'affichage
    pygame.display.update()

# Quitter Pygame
pygame.quit()








