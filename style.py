import pygame

# style.py

import pygame

# Fonction pour charger une police
def load_font(size):
    return pygame.font.Font(pygame.font.get_default_font(), size)

# Définir des couleurs
#BACKGROUND_COLOR = (100, 100, 250)
PLAYER_COLOR = (255, 100, 0)
OBSTACLE_COLOR = (0, 255, 0)
TEXT_COLOR = (255, 255, 255)
SCORE_COLOR = (255, 255, 0)  # Pour un halo lumineux sur le score

# Créer une fonction pour afficher le score
def display_score(screen, score, font):
    score_text = font.render(f"Score: {score}", True, SCORE_COLOR)
    screen.blit(score_text, (50, 50))

# Créer une fonction pour afficher le texte "Game Over"
def display_game_over(screen, font, score):
    screen.fill((0, 0, 0))  # Fond noir
    game_over_text = font.render("Game Over - Press R to Restart", True, TEXT_COLOR)
    screen.blit(game_over_text, (250, 250))
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (450, 300))

# Créer une fonction pour charger une image de fond
def load_background_image(image_path):
    image = pygame.image.load(image_path).convert()
    return pygame.transform.scale(image, (1000, 600))

# Remplir l'écran
def fill_background(screen, background_image):
    screen.blit(background_image, (0, 0))

