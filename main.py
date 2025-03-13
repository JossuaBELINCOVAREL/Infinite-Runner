import pygame

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Infinite Runner")

# Couleur de fond
background_color = (100, 100, 250)

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Couleur de fond
    screen.fill(background_color)

    # Actualisation de l'affichage
    pygame.display.update()

# Quitter Pygame
pygame.quit()








