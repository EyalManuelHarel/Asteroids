from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                           color="white",
                           radius=self.radius,
                           center=self.position,
                           width=2)
        
    def update(self, dt):
        # update the position of the asteroid
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        # do nothing if the asteroid is too small
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # create two smaller asteroids
        random_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_vector1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_vector2 * 1.2

