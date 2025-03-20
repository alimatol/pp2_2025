import pygame


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500,500))

done = False

playlist = [
    r"C:\Users\user\Desktop\kbtu\university pp\PP2\week7\Introduction.mp3",
    r"C:\Users\user\Desktop\kbtu\university pp\PP2\week7\StardustDiving.mp3",
    r"C:\Users\user\Desktop\kbtu\university pp\PP2\week7\Over The Garden Wall.mp3"
    ]
current_track = 0


def play_music(track):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(playlist[track])
    pygame.mixer.music.play()

paused = False
play_music(current_track)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(playlist) 
                play_music(current_track)


            if event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(playlist)
                play_music(current_track)
                

            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
                  
              
    
    pygame.time.delay(60)
        
