from Asteroids import asteroid
import pygame
import random
pygame.init()

screen = pygame.display.set_mode([500, 500])
asteroids_list = [asteroid(200,20,1) , asteroid(20,50,1) , asteroid(200,20,1), asteroid(200,20,1), asteroid(200,20,1), asteroid(200,20,1), asteroid(200,20,1), asteroid(200,20,1), asteroid(200,20,1), asteroid(200,20,1), asteroid(200,20,1), asteroid(200,20,1), asteroid(200,20,1) , asteroid(200,20,1) ,]
screen.fill((255, 255, 255))
#main loop


clock = pygame.time.Clock()
running = True
while running :
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

            # enemy loader 
    screen.fill((0,0,0,0))
    for enemy in asteroids_list:
        enemy.move()
        if enemy.rand_dir == "right":
            enemy.x+= enemy.rand_x
        if enemy.rand_dir == "left" :
            enemy.x -= enemy.rand_x
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(enemy.x, enemy.y, 10, 10))
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()