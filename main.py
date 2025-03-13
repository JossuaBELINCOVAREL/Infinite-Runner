import pygame
import random
import style

# Initialisation de Pygame
pygame.init()

# Chargement de la police depuis style.py
font = style.load_font(50)

# Création de la fenêtre
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Infinite Runner")

# Gestion du temps (limitation des FPS)
clock = pygame.time.Clock()

# Afficher la fenêtre restart
font = pygame.font.Font(None, 50)

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

# Etat du jeu
game_over = False

# Ajout d'un score
score = 0
score_timer = 0

# Fonction pour générer les obstacles
def generate_obstacles():
    obstacle_x = 1000
    obstacle_y = 570
    return pygame.Rect(obstacle_x, obstacle_y, obstacle_weight, obstacle_height)

def reset_game():
    global player, velocity_y, is_jumping, obstacles, game_over, obstacle_timer, score, score_timer
    player = pygame.Rect(player_x, player_y, player_width, player_height)
    velocity_y = 0
    is_jumping = False
    obstacles = []
    game_over = False
    score = 0
    obstacle_timer = 0

# Boucle de jeu
running = True
while running:

    # Limitation des FPS
    clock.tick(150)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

        # Gérer les déplacements gauche/droite
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed = -2
            elif event.key == pygame.K_RIGHT:
                player_speed = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speed = 0

    # Ecran Game Over
    if game_over:
        screen.fill((0, 0, 0))  # Fond noir
        text = font.render("Game Over - Press R to Restart", True, (255, 255, 255))
        screen.blit(text, (250, 250))

    # Affichage du score final
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (450, 300))

        pygame.display.update()
        continue  # Empêcher le reste du code de s'exécuter

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

    # Empêcher le joueur de sortir de l'écran
    player.x += player_speed
    if player.x < 0:
        player.x = 0
    elif player.x + player_width > 1000:
        player.x = 1000 - player_width

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
            game_over = True
        
        if obstacle.x < 0:
            obstacles.remove(obstacle)

    if not game_over:
        score_timer += 1
        if score_timer >= 30:
            score += 1
            score_timer = 0  #

    # Remplir l'écran
    style.fill_background(screen)

    # Dessiner le personnage
    pygame.draw.rect(screen, style.PLAYER_COLOR, player)

    # Dessiner les obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, style.OBSTACLE_COLOR, obstacle)

    # Afficher le score en haut à gauche
    style.display_score(screen, score, font)

    # Actualisation de l'affichage
    pygame.display.update()

# Quitter Pygame
pygame.quit()