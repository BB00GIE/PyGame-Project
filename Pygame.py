import pygame
pygame.init()
score = 0
screen_width = 800
screen_length = 800
Black = (0,0,0)
Red = (255,0,0)
White = (255,255,255)
Blue = (0,0,255)
pygame.display.init()
screen = pygame.display.set_mode( (screen_width , screen_length))
pygame.display.set_caption("My First Game")
#pygame.draw.rect()
done = False
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score: ' +str(score), True, Black, White)
textRect = text.get_rect()
textRect.center = (400 , 20 )
Phoenix = pygame.image.load('Readme.png')
while not done:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score+=1
    
            
    

    screen.fill(White)
    screen.blit(text, textRect)
    screen.blit(Phoenix,(0,100))
    #pygame.draw.rect(screen, Black, [300, 300,  200, 200])
    text = font.render('Score: ' + str(score), True, Black, White)
    pygame.display.update()
#print(score)
pygame.quit()
    
    

    
    
    
