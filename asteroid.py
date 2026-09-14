import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.position = [x, y]
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        asteroid1_vector_rotation = self.velocity.rotate(random.uniform(20, 50))
        asteroid2_vector_rotation = self.velocity.rotate(random.uniform(-50, -20))
        radius_new = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius_new)
        asteroid1.velocity = asteroid1_vector_rotation * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, radius_new)
        asteroid2.velocity = asteroid2_vector_rotation * 1.2
