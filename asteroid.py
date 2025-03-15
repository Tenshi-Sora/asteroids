from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE
import pygame

class Asteroid(CircleShape):
    containers = None # This is used to store the groups that the asteroid will be added to

    def __init__(self, x, y, radius): # Initializes the asteroid object
        super().__init__(x, y, radius) # Calls the parent class constructor
        if Asteroid.containers: # Checks if the containers variable is not None
            for container in Asteroid.containers: # Adds the asteroid to the groups that it will be added to
                container.add(self)

    def draw(self, screen): # Draws the asteroid on the screen
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt): # Moves the asteroid
        self.position += self.velocity * dt # Moves the asteroid based on its velocity and the time since the last frame update