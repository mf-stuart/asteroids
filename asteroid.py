import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        top_v = pygame.math.Vector2(self.velocity.x, self.velocity.y).rotate(+angle)
        bottom_v = pygame.math.Vector2(self.velocity.x, self.velocity.y).rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        top_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        bottom_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        self.kill()

        top_asteroid.velocity = top_v * 1.2
        bottom_asteroid.velocity = bottom_v * 1.2

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255,255,255),
            self.position,
            self.radius,
            2)

    def update(self, dt):
        self.position +=  self.velocity * dt