import pygame
import random
from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def _spawn_child(self, vel, radius):
        a = Asteroid(self.position.x, self.position.y, radius)
        a.velocity = vel * 1.2
        return a

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        r = self.radius - ASTEROID_MIN_RADIUS
        self._spawn_child(self.velocity.rotate( angle), r)
        self._spawn_child(self.velocity.rotate(-angle), r)

    def update(self, dt):
        self.position += (self.velocity * dt)
