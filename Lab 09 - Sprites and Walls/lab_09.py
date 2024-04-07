"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5
SPRITE_SCALING_BERRY = 0.05

DEFAULT_SCREEN_WIDTH = 1300
DEFAULT_SCREEN_HEIGHT = 900
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7

NUMBER_OF_BERRIES = 20


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.

        # We scroll the 'sprite world' but not the GUI.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.score = 0

        self.berries_left = NUMBER_OF_BERRIES

        self.good_sound = None

        self.berry_left = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.good_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.score = 0
        self.berry_left = NUMBER_OF_BERRIES
        self.berry_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("parrot.png",
                                           scale=0.08)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # Creates obstacles
        for x in range(1, 1550, 120):
            for y in range(1, 1100, 60):
                # Randomly skip a box so the player can find a way through
                if random.randrange(10) < 8:
                    if random.randrange(4) % 2:
                        wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)
                    else:
                        wall = arcade.Sprite(":resources:images/tiles/stoneMid.png", SPRITE_SCALING)

                    # Adds walls
                    wall.center_x = x

                    wall.center_y = y

                    self.wall_list.append(wall)

        # Create horizontal rows of walls
        for x in range(0, 1600, 64):
            # Bottom edge
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

            # Top edge
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1100 - 32
            self.wall_list.append(wall)

        # Create vertical columns of walls
        for y in range(96, 1100, 64):
            # Left
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING)
            wall.center_x = 32
            wall.center_y = y
            self.wall_list.append(wall)

            # Right
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING)
            wall.center_x = 1600 - 32
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)

        for i in range(NUMBER_OF_BERRIES):
            # Create the berry instance
            berry = arcade.Sprite("cherry.png", SPRITE_SCALING_BERRY)

            berry_placed_successfully = False

            # Keep trying until success

            while not berry_placed_successfully:
                # Position the berries

                berry.center_x = random.randrange(1500)

                berry.center_y = random.randrange(800)

                # See if a berry is hitting a wall

                wall_hit_list = arcade.check_for_collision_with_list(berry, self.wall_list)

                # Checking to see if a berry is hitting another berry

                berry_hit_list = arcade.check_for_collision_with_list(berry, self.berry_list)

                if len(wall_hit_list) == 0 and len(berry_hit_list) == 0:

                    berry_placed_successfully = True

                # Add the berry to the lists

            self.berry_list.append(berry)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites

        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()

        if len(self.berry_list) != 0:
            self.berry_list.draw()

        # Select the (scrolled) camera for our GUI

        self.camera_gui.use()

        if len(self.berry_list) != 0:

            # Put the text on the screen.
            remainder = f"Berries Left: {self.berry_left}"
            arcade.draw_text(remainder, 10, 40, arcade.color.WHITE, 14)
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


        else:
            # Game Over screen when all berries are obtained.
            arcade.draw_text("Game Over", 650, 450, arcade.color.RED, 20)
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
            remainder = f"Berries Left: {self.berry_left}"
            arcade.draw_text(remainder, 10, 40, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if len(self.berry_list) != 0:
            if key == arcade.key.UP:
                self.up_pressed = True
            elif key == arcade.key.DOWN:
                self.down_pressed = True
            elif key == arcade.key.LEFT:
                self.left_pressed = True
            elif key == arcade.key.RIGHT:
                self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player

        self.scroll_to_player()

        self.berry_list.update()

        # Generate a list of all sprites that collided with the player.
        berries_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                self.berry_list)

        # When berries are picked up
        # Adds to score, and adds to total score
        for berry in berries_hit_list:
            berry.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.good_sound)

        # Minuses berries left
        for berry in berries_hit_list:
            berry.remove_from_sprite_lists()
            self.berry_left -= 1

    def scroll_to_player(self):

        """

        Scroll the window to the player.



        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.

        Anything between 0 and 1 will have the camera move to the location with a smoother

        pan.

        """

        position = Vec2(self.player_sprite.center_x - self.width / 2,

                        self.player_sprite.center_y - self.height / 2)

        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):

        """

        Resize window

        Handle the user grabbing the edge and resizing the window.

        """

        self.camera_sprites.resize(int(width), int(height))

        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
