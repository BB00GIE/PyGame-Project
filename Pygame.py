import pygame
pygame.init()
score = 0
screen_width = 800
screen_length = 800
Black = (0,0,0)
Red = (255,0,0)
White = (255,255,255)
pygame.display.init()
screen = pygame.display.set_mode( (screen_width , screen_length))
pygame.display.set_caption("My First Game")
#pygame.draw.rect()
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    if pygame.key.get_pressed() == pygame.key.name(32):
        score+=1

    screen.fill(White)
    pygame.draw.rect(screen, Black, [300, 300,  200, 200])
    pygame.display.update()
print(score)
pygame.quit()
    
    

    
    
    
