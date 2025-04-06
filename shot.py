from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(surface=screen,
                           color="white",
                           radius=self.radius,
                           center=self.position,
                           width=2)
        
    def update(self, dt):
        # update the position of the shot
        self.position += self.velocity * dt
