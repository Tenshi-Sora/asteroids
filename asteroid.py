import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE


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

    def split(self): # Splits the asteroid into two smaller asteroids if it is larger than the minimum radius
        self.kill() # Removes the asteroid from the game
        if self.radius <= ASTEROID_MIN_RADIUS: # Checks if the asteroid is larger than the minimum radius
            return
        else:  # Creates two smaller asteroids
            random_angle = random.uniform(20, 50)  # Generates a random angle between 20 and 50 degrees
            new_radius = self.radius - ASTEROID_MIN_RADIUS  # Compute the new radius of the smaller asteroids

            # Create two new velocity vectors rotated by random_angle and -random_angle
            velocity1 = self.velocity.rotate(random_angle) * 1.2
            velocity2 = self.velocity.rotate(-random_angle) * 1.2

            # Create two new Asteroid objects at the current asteroid position with the new radius
            Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
            Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2