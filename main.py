import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH) 
    print("Screen height:",SCREEN_HEIGHT)

    fps_timer = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = fps_timer.tick(60) / 1000
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                return
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.kill()
        
    


if __name__ == "__main__":
    main()
