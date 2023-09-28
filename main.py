import pygame
import time
from random import randint

pygame.init()

largeur = 1980
hauteur = 1080

screen = pygame.display.set_mode((largeur, hauteur))

pygame.display.set_caption("attraction gravitationnelle")

running = True

clock = pygame.time.Clock()

prev_time = time.time()

class Particle:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), 10)

nbParticles = 100
Particle = [Particle(randint(0,largeur), randint(0, hauteur)) for i in range(nbParticles)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time = time.time()
    dt = (current_time - prev_time)*60
    prev_time = current_time
    
    for p in Particle:
        p.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()