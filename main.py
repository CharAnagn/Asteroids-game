import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

def main():
    pygame.init()

    game_clock = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers  = updatable_group, drawable_group
    Asteroid.containers = asteroids_group, updatable_group,drawable_group
    AsteroidField.containers = updatable_group

    asteroid_field = AsteroidField()
    main_player = Player(SCREEN_WIDTH/ 2, SCREEN_HEIGHT / 2)




    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = game_clock.tick(60) / 1000

        screen.fill("black")

        updatable_group.update(dt)


        for sprite in drawable_group:
            sprite.draw(screen)

        pygame.display.flip()



if __name__ == "__main__":
    main()
