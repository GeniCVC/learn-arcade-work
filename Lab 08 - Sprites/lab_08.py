# Written by Matthew Jackson
import random  # Imports random library
import arcade  # Imports arcade library

# --- Constants ---

# -- Sprite Scale --
SPRITE_SCALING_PLAYER = 0.03
SPRITE_SCALING_GEM = 0.2

# -- Sprite Amount --
GEM_COUNT = 5
METEOR_COUNT = 5

# -- Window --
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


class Gem(arcade.Sprite):
    """Good Sprites"""

    def reset_pos(self):
        # Reset the gem to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Moves the gem
        self.center_y -= 1

        # See if the gem has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class Meteor(arcade.Sprite):
    """Bad Sprites"""

    def reset_pos(self):
        # Reset the meteor to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT)
        self.center_x = random.randrange(SCREEN_WIDTH + 20,
                                         SCREEN_WIDTH + 120)

    def update(self):
        # Move the meteor
        self.center_x -= 1

        # See if the meteor has fallen off the bottom of the screen.
        # If so, reset it.
        if self.left < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.hit_sound = None
        self.good_sound = None
        self.player_list = None
        self.gem_list = None
        self.meteor_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Background image will be stored in this variable
        self.background = None

        self.over = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()
        self.hit_sound = arcade.load_sound(":resources:sounds/rockHit2.wav")
        self.good_sound = arcade.load_sound(":resources:sounds/coin1.wav")

        # Score
        self.score = 0

        # Set up the player
        # Source for Starship.png: https://www.pngfind.com/mpng/iRomwJ_8-bit-spaceship-png-spaceship-8-bit-png/
        self.player_sprite = arcade.Sprite("Starship.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the gems
        for i in range(GEM_COUNT):
            # Create the gem instance
            gem = Gem(":resources:images/items/gemBlue.png", SPRITE_SCALING_GEM)

            # Position the gems
            gem.center_x = random.randrange(SCREEN_WIDTH)
            gem.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the gem to the lists
            self.gem_list.append(gem)

        for i in range(METEOR_COUNT):
            # Create the meteor instance
            meteor = Meteor(":resources:images/space_shooter/meteorGrey_big1.png", SPRITE_SCALING_GEM)

            # Position the meteors
            meteor.center_x = random.randrange(SCREEN_WIDTH)
            meteor.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the meteors to the lists
            self.meteor_list.append(meteor)

        # Source for 8bitSpace.jpg: https://www.deviantart.com/yuni-naoki/art/FREE-Purple-Space-Background-139763515
        self.background = arcade.load_texture("8bitSpace.jpg")

    def on_draw(self):

        """ Draw everything """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        # Draw the background texture
        self.player_list.draw()
        if len(self.gem_list) != 0:

            self.gem_list.draw()
            self.meteor_list.draw()

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


        else:
            arcade.draw_text("Game Over", 500, 300, arcade.color.RED, 20)
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        if len(self.gem_list) != 0:
            # Move the center of the player sprite to match the mouse x, y
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.gem_list.update()
        self.meteor_list.update()

        # Generate a list of all sprites that collided with the player.
        gems_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.gem_list)
        meteor_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                               self.meteor_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        if len(self.gem_list) != 0:
            for gems in gems_hit_list:
                gems.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.good_sound)

            for meteor in meteor_hit_list:
                meteor.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(self.hit_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
