import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def _spawn_child(self, velocity, radius):
        child = Asteroid(self.position.x, self.position.y, radius)
        child.velocity = velocity * 1.2
        return child

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self._spawn_child(self.velocity.rotate(angle), new_radius)
        self._spawn_child(self.velocity.rotate(-angle), new_radius)

    def update(self, dt):
        self.position += self.velocity * dt
