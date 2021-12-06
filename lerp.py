import pygame, math
from pygame import font

pygame.init()
def lerp_color(colors, value):
    fract, index = math.modf(value)
    color1 = pygame.Color(colors[int(index) % len(colors)])
    color2 = pygame.Color(colors[int(index + 1) % len(colors)])
    return color1.lerp(color2, fract)

def button(screen, position, text):
    font = pygame.font.SysFont("Anton", 50)
    text_render = font.render(text, 1, (0, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))

pygame.init()
screen = pygame.display.set_mode((800, 800)) 
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
b1 = button(screen,(310,200), "Faster")

variable = 1



run = True
while run:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            start_time = pygame.time.get_ticks()

    
    colors = [ (255,0,0), (255,154,000), (255,255,0), (9,255,0), (000,255,239), (0,60,255), (230,000,255)]
    value = (pygame.time.get_ticks() - start_time) / 1000
    current_color = lerp_color(colors, value)
  
    

    screen.fill(0)
    
    
     

    if event.type == pygame.MOUSEBUTTONDOWN:
            if b.collidepoint(pygame.mouse.get_pos()):
                    variable = variable + 1
                   

    if variable > 2:
        pygame.draw.circle(screen, current_color, screen.get_rect().center, 1000)          
    elif variable < 2:
        pygame.draw.circle(screen, (255,255,255), screen.get_rect().center, 1000)        
        b = button(screen,(305,600), "Press Me")                
    


    
  
    pygame.display.flip()

pygame.quit()
exit()