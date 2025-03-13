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

# Paramètre dec gravité
gravity = 0.5
jump_speed = -10
velocity_y = 0
is_jumping = False

# Paramètre de la vitesse horizontale
player_speed = 1

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gérer le saut avec la barre d'espace
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        velocity_y = jump_speed # Appliquation de la force du saut
        is_jumping = True

    # Appliquer la gravité
    velocity_y += gravity
    player.y += velocity_y

    # Touche le sol
    if player.y >= 550:
        player.y = 550
        velocity_y = 0
        is_jumping = False

    # Déplacement horizontal du personnage
    player.x += player_speed  # Le personnage se déplace à cette vitesse

    # Remplir l'écran avec la couleur de fond
    screen.fill(background_color)

    # Dessiner le personnage
    pygame.draw.rect(screen, (255, 100, 0), player)

    # Actualisation de l'affichage
    pygame.display.update()

# Quitter Pygame
pygame.quit()