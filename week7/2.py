import pygame
import time


pygame.init()
screen = pygame.display.set_mode((500, 450))
done = False

clock = pygame.image.load("clock.png")
right_hand = pygame.image.load("min_hand.png")
left_hand = pygame.image.load("sec_hand.png")

clock = pygame.transform.scale(clock, (500, 450))
right_hand = pygame.transform.scale(right_hand, (700,200))
left_hand = pygame.transform.scale(left_hand, (500,200))

center_x = 250
center_y = 225



def rot_center(image , angle, center_x, center_y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(center_x, center_y))

    return rotated_image, new_rect



while not done:

    screen.fill((255, 255, 255))
    screen.blit(clock,(0,0))

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    angle_sec = -(minutes %60) *6
    angle_min = -(seconds %60) *6
    '''degrees'''

    rotated_right_hand, right_hand_rect = rot_center(right_hand, angle_sec, center_x, center_y)
    rotated_left_hand, left_hand_rect = rot_center(left_hand, angle_min, center_x, center_y)

    screen.blit(rotated_right_hand, right_hand_rect.topleft)
    screen.blit(rotated_left_hand, left_hand_rect.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip() 

    pygame.time.delay(1000)
