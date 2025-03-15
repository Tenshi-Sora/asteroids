import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape): # This class is used to create a shot object that will be fired by the player
    containers = None  # This is used to store the groups that the shot will be added to

    def __init__(self, x, y, velocity): # Initializes the shot object with the position and velocity
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        if Shot.containers:
            for container in Shot.containers:
                container.add(self)

    def update(self, dt): # Moves the shot based on its velocity and the time since the last frame update
        self.position += self.velocity * dt

    def draw(self, screen): # Draws the shot on the screen
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)