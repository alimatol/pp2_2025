import pygame, sys
import random, time
from pygame.locals import *

# Initializing
pygame.init()


# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()
car_crash = pygame.mixer.Sound('car crash.wav')
coin_colletion = pygame.mixer.Sound('coin.wav')


# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)

# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0

road = pygame.image.load('background-1_0.png')

# Fonts
font = pygame.font.SysFont("Impact", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Create game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Coin class
class Coins(pygame.sprite.Sprite):
    def __init__(self, radius=15, color=YELLOW):
        super().__init__()
        self.radius = radius
        self.color = color
        self.respawn()

    def respawn(self):
        """Respawn the coin at a random x position, y = 520"""
        self.x = random.randint(self.radius, SCREEN_WIDTH - self.radius)
        self.y = 520
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.collected = False
        
    def draw(self):
        """Draw the coin"""
        pygame.draw.circle(DISPLAYSURF, self.color, (self.x, self.y), self.radius)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Create game objects
P1 = Player()
E1 = Enemy()
coin = Coins()

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1)

# Speed increase event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(road, (SCREEN_WIDTH//2 - road.get_width()//2 , 0))

    # Display scores
    coin_score_text = font_small.render(f"Coins: {COIN_SCORE}", True, BLACK)
    DISPLAYSURF.blit(coin_score_text, (10, 40))

    # Move and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Draw the coin separately
    coin.draw()

    # Check for collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        car_crash.play(0)
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (SCREEN_WIDTH//2 - game_over.get_width()//2, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check for collision with coin
    if P1.rect.colliderect(coin.rect) and not coin.collected:
        coin_colletion.play(0)
        COIN_SCORE += 1
        coin.collected = True
        coin.respawn()

    pygame.display.update()
    FramePerSec.tick(FPS)
