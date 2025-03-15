import pygame # Imports the pygame library
from player import Player # Imports the player class from the player.py file
from asteroid import Asteroid  # Imports the Asteroid class from the asteroid.py file
from constants import * # Imports the constants from the constants.py file
from asteroidfield import AsteroidField # Imports the AsteroidField class from the asteroidfield.py file


def main():
    pygame.init() # Initiates pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creates a window
    print("Starting Asteroids!") # Tells the user that the game is starting
    print(f"Screen width: {SCREEN_WIDTH}") # Tells the user the width of the screen
    print(f"Screen height: {SCREEN_HEIGHT}") # Tells the user the height of the screen
    clock = pygame.time.Clock() # Creates a clock to control the frame rate
    dt = 0 # Creates a variable to store the time since the last frame update
    updatable = pygame.sprite.Group() # Creates a group to store all the objects that need to be updated
    drawable = pygame.sprite.Group() # Creates a group to store all the objects that need to be drawn
    asteroids = pygame.sprite.Group() # Creates a group to store all the asteroids
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Creates a player object in the center of the screen
    updatable.add(player) # Adds the player to the updatable group
    drawable.add(player) # Adds the player to the drawable group
    Asteroid.containers = (asteroids, updatable, drawable) # Set the containers field of the Asteroid class
    AsteroidField.containers = (updatable,) # Set the containers field of the AsteroidField class
    asteroid_field = AsteroidField() # Create a new AsteroidField object

    while True: # Main game loop
        for event in pygame.event.get(): # Checks if the user has closed the window
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Fills the screen with black background
        updatable.update(dt)  # Updates all objects in the "updatable" group
        for asteroid in asteroids: # Checks if the player has collided with any asteroids
            if player.collision(asteroid):
                print("Game over!")
                return
        for obj in drawable: # Draws all objects in the "drawable" group
            obj.draw(screen)  
        player.update(dt) # Updates the player to allow for movement
        player.draw(screen) # Draws the player on the screen
        pygame.display.flip()  # Refresh screen
        dt = clock.tick(60) / 1000.0  # Limits FPS to 60 and calculates delta time

if __name__ == "__main__":
    main()