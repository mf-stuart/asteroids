import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:

        for member in updatable:
            member.update(dt)

        for member in asteroids:
            if member.collision(player):
                print("Game over!")
                pygame.event.post(pygame.event.Event(pygame.QUIT))

            for shot in shots:
                if member.collision(shot):
                    member.split()
                    shot.kill()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        for member in drawable:
            member.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000.0




if __name__ == "__main__":
    main()