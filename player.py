import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y): # Initializes the player object
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0 # This is used to create a time limit for the player's shots

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

    def shoot(self): # Creates a shot object that will be fired by the player
        if self.timer <= 0:
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = direction * PLAYER_SHOOT_SPEED
            Shot(self.position.x, self.position.y, velocity)
            self.timer = PLAYER_SHOOT_COOLDOWN
    
    # Some of the code below were provided by the class instructor and are used to maintain focus on the main lesson of the class
    def update(self, dt): # Controls the player movement
        keys = pygame.key.get_pressed() # Gets the keys that are currently pressed
        self.timer -= dt # Decreases the timer by the time since the last frame update

        if keys[pygame.K_a]: # If the "A" arrow key is pressed, rotate the player to the left
            self.rotate(-dt)
        if keys[pygame.K_d]: # If the "D" arrow key is pressed, rotate the player to the right
            self.rotate(dt)
        if keys[pygame.K_w]: # If the "W" arrow key is pressed, move the player forward
            self.move(dt)
        if keys[pygame.K_s]: # If the "S" arrow key is pressed, move the player backward
            self.move(-dt)
        if keys[pygame.K_SPACE]:  # If the spacebar is pressed, shoot
            self.shoot()
    
    # The code below was provided by the class instructor and is used to maintain focus on the main lesson of the class
    def move (self, dt): # Moves the player in the direction they are facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt