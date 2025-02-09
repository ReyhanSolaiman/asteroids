import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
import sys
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
        
        screen.fill("black")

        for entity in drawable:
            entity.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()