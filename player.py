from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
import pygame

class Player(CircleShape):
    def __init__(self, x, y): # Initializes the player object
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # All the methods below were provided by the class instructor and are used to maintain focus on the main lesson of the class
    def triangle(self): # Creates a triangle shape for the player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): # Draws the player on the screen
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt): # Rotates the player based on the time since the last frame update
        self.rotation += PLAYER_TURN_SPEED * dt

    # Some of the code below were provided by the class instructor and are used to maintain focus on the main lesson of the class
    def update(self, dt): # Controls the player movement
        keys = pygame.key.get_pressed() # Gets the keys that are currently pressed

        if keys[pygame.K_a]: # If the "A" arrow key is pressed, rotate the player to the left
            self.rotate(-dt)
        if keys[pygame.K_d]: # If the "D" arrow key is pressed, rotate the player to the right
            self.rotate(dt)