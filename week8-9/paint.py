import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

done = False

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


color = BLACK
brush_size = 5
start_pos = None
drawing = False
mode = "free_draw"  # Modes: "free_draw", "rectangle", "circle", "square"
screen.fill(WHITE)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True


            if event.key == pygame.K_c:
                screen.fill(WHITE)  # Clear screen
            if event.key == pygame.K_e:
                color = WHITE  # Eraser
            if event.key == pygame.K_b:
                color = BLACK
            if event.key == pygame.K_r:
                color = RED
         
            if event.key == pygame.K_UP:
                brush_size = min(50, brush_size + 10)
            if event.key == pygame.K_DOWN:
                brush_size = max(1, brush_size - 5)


            if event.key == pygame.K_1:
                mode = "rectangle"
            if event.key == pygame.K_2:
                mode = "circle"
            if event.key == pygame.K_3:
                mode = "square"
            if event.key == pygame.K_4:
                mode = "rigth triangle"
            if event.key == pygame.K_5:
                mode = "free_draw"
            if event.key == pygame.K_6:
                mode = "equivalent triangle"
            if event.key == pygame.K_7:
                 mode ="rhombos"
            

        if event.type == pygame.MOUSEBUTTONDOWN: #while preessed
            start_pos = event.pos
            drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            if mode == "rectangle":
                end_pos = event.pos
                width = abs(start_pos[0] - end_pos[0])
                height = abs(start_pos[1] - end_pos[1])
                rect_x = min(start_pos[0], end_pos[0])
                rect_y = min(start_pos[1], end_pos[1])
                pygame.draw.rect(screen, color, (rect_x, rect_y, width, height), 2)

            if mode == "square":
                    end_pos = event.pos
                    width = abs(start_pos[0] - end_pos[0])
                    rect_x = min(start_pos[0], end_pos[0])
                    rect_y = min(start_pos[1], end_pos[1])
                    pygame.draw.rect(screen, color, (rect_x, rect_y, width, width), 2)
            
            if mode == "rigth triangle":
                    end_pos = event.pos
                    p1 = start_pos
                    p3 = end_pos
                    p2 = (start_pos[0], end_pos[1])  
                    pygame.draw.polygon(screen, color, [p1, p2, p3], 2)

            if mode == "rhombos":
                    end_pos = event.pos
                    p1 = (start_pos[0] +end_pos[0])//2, start_pos[1] #point in the bottom
                    p3 = (start_pos[0] +end_pos[0])//2, end_pos[1] #point in the top
                    p4 = end_pos[0], (end_pos[1] + start_pos[1])//2 #point on ;eft
                    p2 = start_pos[0], (end_pos[1] + start_pos[1])//2 #point on rigth
                    pygame.draw.polygon(screen, color, [p1, p2, p3, p4], 2)

            if mode == "equivalent triangle":
                    end_pos = event.pos
                    p1 = start_pos
                    p3 = end_pos
                    side = abs(start_pos[0] - end_pos[0]) 
                    h = (math.sqrt(3)/2) * side
                    p2 = (start_pos[0] +(end_pos[0] - start_pos[0])//2), start_pos[1] - int(h)

                    pygame.draw.polygon(screen, color, [p1, p2, p3], 2)


            if mode == "circle":
                end_pos = event.pos
                radius = abs(start_pos[0]-end_pos[0])
                pygame.draw.circle(screen, color, start_pos, radius, 2)

            drawing = False

    if drawing and pygame.mouse.get_pressed()[0] and mode == "free_draw":
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, color, start_pos, mouse_pos, brush_size)
        start_pos = mouse_pos

    pygame.display.update()
    clock.tick(60)

pygame.quit()



        

