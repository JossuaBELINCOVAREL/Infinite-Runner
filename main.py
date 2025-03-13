import pygame
import random

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Infinite Runner")

# Gestion du temps (limitation des FPS)
clock = pygame.time.Clock()

# Couleur de fond
background_color = (100, 100, 250)

# Création du personnage
player_width = 50
player_height = 50
player_x = 50  # Position initiale à gauche
player_y = 550  # Position verticale (au bas de la fenêtre)
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Paramètre dec gravité
gravity = 0.3
jump_speed = -12 
velocity_y = 0
is_jumping = False

# Liste des obstacles
obstacle_weight = 30
obstacle_height = 30
obstacles_speed = 2
obstacles = []

# Délai minimal entre deux obstacles
obstacle_spawn_delay = 100 # Temps d'attente en frames avant un nouvel obstacle
obstacle_timer = 0

# Paramètre de la vitesse horizontale
player_speed = 0

# Fonction pour générer les obstacles
def generate_obstacles():
    obstacle_x = 1000
    obstacle_y = 570
    return pygame.Rect(obstacle_x, obstacle_y, obstacle_weight, obstacle_height)


# Boucle de jeu
running = True
while running:

    # Limitation des FPS
    clock.tick(150)

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
    player.x += player_speed

    # Ajouter un obstacle (si nécessaire)
    if obstacle_timer <= 0:
        if random.randint(0, 60 ) == 1 :
            obstacles.append(generate_obstacles())
            obstacle_timer = obstacle_spawn_delay

    if obstacle_timer > 0:
        obstacle_timer -= 1

    # Déplacement des obstacles et vérification de collision
    for obstacle in obstacles[:]:
        obstacle.x -= obstacles_speed
        if player.colliderect(obstacle):
            print("Game Over !")
            running = False
        
        if obstacle.x < 0:
            obstacles.remove(obstacle)

    # Remplir l'écran avec la couleur de fond
    screen.fill(background_color)

    # Dessiner le personnage
    pygame.draw.rect(screen, (255, 100, 0), player)

    # Dessiner les obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, (0, 255, 0), obstacle) 

    # Actualisation de l'affichage
    pygame.display.update()

# Quitter Pygame
pygame.quit()