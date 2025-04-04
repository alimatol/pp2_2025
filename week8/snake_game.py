import pygame
import random
import os, time

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 30)
font2 = pygame.font.SysFont("Impact", 50)
level_changed = False

max_w = 400
max_h = 400

done = False
step = 20
speed = 5

x = 200
y = 200

score = 0

def BackGround(screen, width, heigth):
    for line_y in range(0, 400, step):
        pygame.draw.line(screen, (70, 70, 70), (0, line_y), (400, line_y))
    for line_x in range(0, 400, step):
        pygame.draw.line(screen, (70, 70, 70), (line_x, 0), (line_x, 400))


class GameObject:
    def __init__(self, color, points, tile_width):
        self.color = color
        self.points = points
        self.tile_width = tile_width

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

class Snake(GameObject):
    def __init__(self, x, y, tile_width):
        super().__init__((0, 255, 0), [(x,y)], tile_width)
        self.dx = 1
        self.dy = 0

    def move(self):
        head_x, head_y = self.points[0] 

        x = self.dx *step + head_x
        y = self.dy *step + head_y

        # collision with borders
        if x > max_w:
            x = 0
        if x < 0:
            x = max_w
        if y > max_h:
            y = 0
        if y < 0:
            y = max_h
        if (x, y) in self.points:
            screen.fill((255,0,0))
            screen.blit(game_over, ((max_w - game_over.get_width()) // 2, max_h // 2 - game_over.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(2000) 
            pygame.quit()
            exit()

        self.points = [(x, y)] + self.points[:-1] 

    def increas(self, pos):
        self.points.append(Point(pos.X, pos.Y))

    def draw(self, screen):
        for point in self.points:
            pygame.draw.rect(screen, self.color, (point[0], point[1], self.tile_width, self.tile_width))

    def grow(self):
        self.points.append(self.points[-1])

class Food_Apple(GameObject):
    def __init__(self, tile_width, lifespan = 7000):
        super().__init__((255, 0 ,0), [self.random_position()], tile_width)
      
    def random_position(self):
        x = random.randint(0, (max_w//20)-1) * step
        y = random.randint(0, (max_h//20) -1) * step
        return (x,y)
    

    #respawning food
    def respawn(self):
        self.points[0] = self.random_position()
        self.spawn_time = pygame.time.get_ticks()
        

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0 , 0), (self.points[0][0], self.points[0][1], self.tile_width, self.tile_width))
    
    
class Food_Lemon(GameObject):
    def __init__(self, tile_width):
        super().__init__((255, 202, 5),[self.random_position()], tile_width)

    def random_position(self):
        x = random.randint(0, (max_w//20)-1) * step
        y = random.randint(0, (max_h//20) -1) * step
        return (x,y)
    #respawning food
    def respawn(self):
        self.points[0] = self.random_position()

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 202, 5), (self.points[0][0], self.points[0][1], self.tile_width, self.tile_width))
    


class Wall(GameObject):
    def __init__(self, tile_width):
        super().__init__((56, 56,56), [], tile_width)
        self.level = 1
        self.load_level()
          
    def load_level(self):
        file = open("levels/level{}.txt".format(self.level), "r")
        row = -1
        col = -1
        for line in file:
            row = row + 1
            col = -1
            for c in line:
                col = col + 1
                if c == '#':
                    self.points.append(Point(col * self.tile_width, row * self.tile_width))
        file.close()

    def next_level(self):
        self.points = []
        self.level = (self.level + 1) % 2
        self.load_level()

    def draw(self, screen):
        for point in self.points:
            pygame.draw.rect(screen, (56, 56, 56), (point.X, point.Y, self.tile_width, self.tile_width))


snake = Snake(200, 200, step)
Apple = Food_Apple(step)
Lemon = Food_Lemon(step)
wall = Wall(step)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            #movement of snake
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = +1
            if event.key == pygame.K_RIGHT:
                snake.dx = +1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0

    screen.fill((0, 0, 0))
    BackGround(screen, max_w, max_h)

    #rendering all texts
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    game_over = font2.render("Game Over", True, (0,0,0))
    screen.blit(score_text, (10, 10))
    snake.move()

    #drawing objects
    snake.draw(screen)
    Apple.draw(screen)
    Lemon.draw(screen)
    wall.draw(screen)

    if snake.points[0] == Apple.points[0]:
        Apple.respawn()
        score += 1
        snake.grow()

    if snake.points[0] == Lemon.points[0]:
        Lemon.respawn()
        score += 3
        snake.grow()
        snake.grow()
        
    #wall collision and ending screen
    for point in wall.points:
        if snake.points[0] == (point.X, point.Y):
            screen.fill((255,0,0))
            screen.blit(game_over, ((max_w - game_over.get_width()) // 2, max_h // 2 - game_over.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(2000) 
            done = True
            


#if food devisible by 3 => change level
    if score % 10 == 0 and not level_changed:
        wall.next_level()
        level_changed = True
        speed += 2
    
    if score % 10 != 0:
        level_changed = False

    
    pygame.display.flip()
    clock.tick(speed)

    
