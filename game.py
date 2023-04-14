import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des constantes du jeu
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 60
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5
BALL_SPEED = 5
BALL_SIZE = 10
BALL_COLOR = (255, 255, 255)
PADDLE_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Création des objets de jeu
ball = pygame.Rect(SCREEN_WIDTH / 2 - BALL_SIZE / 2,
                   SCREEN_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE)
paddle1 = pygame.Rect(50, SCREEN_HEIGHT / 2 -
                      PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT /
                      2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Variables de jeu
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))
paddle1_speed = 0
paddle2_speed = 0
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Boucle de jeu principale
while True:
    # Gestion des événements de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_speed = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                paddle1_speed = PADDLE_SPEED
            elif event.key == pygame.K_UP:
                paddle2_speed = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                paddle2_speed = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle1_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle2_speed = 0

    # Mise à jour des positions des objets de jeu
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    paddle1.y += paddle1_speed
    paddle2.y += paddle2_speed

    # Gestion des collisions avec les bords de l'écran
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0:
        score2 += 1
        ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        ball_speed_x = BALL_SPEED * random.choice((1, -1))
        ball_speed_y = BALL_SPEED * random.choice((1, -1))
    if ball.right >= SCREEN_WIDTH:
        score1 += 1
        ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        ball_speed_x = BALL_SPEED * random.choice((1, -1))
        ball_speed_y = BALL_SPEED * random.choice((1, -1))
    # Gestion des collisions avec les raquettes
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x = -ball_speed_x

    # Affichage des objets de jeu
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle1)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle2)
    pygame.draw.ellipse(screen, BALL_COLOR, ball)
    score_text = font.render(str(score1) + " - " +
                             str(score2), True, PADDLE_COLOR)
    screen.blit(score_text, (SCREEN_WIDTH / 2 -
                score_text.get_width() / 2, 10))

    # Mise à jour de l'affichage de l'écran
    pygame.display.update()

    # Limitation du nombre d'images par seconde
    pygame.time.Clock().tick(FRAMES_PER_SECOND)
