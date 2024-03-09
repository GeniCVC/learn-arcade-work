""" Lab 7 - User Control """

# Imports arcade library
import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


def draw_sky():
    # Draws Sky
    arcade.draw_rectangle_filled(300, 550, 600, 100, arcade.color.BLUE_SAPPHIRE)
    arcade.draw_rectangle_filled(300, 450, 600, 100, arcade.color.BONDI_BLUE)
    arcade.draw_rectangle_filled(300, 350, 600, 100, arcade.color.BLUE_GREEN)
    arcade.draw_rectangle_filled(300, 250, 600, 100, arcade.color.BALL_BLUE)


# Seagull function
def draw_seagulls():
    # Draw First Seagull
    arcade.draw_point(500, 450, arcade.color.WHITE, 3)
    arcade.draw_point(503, 453, arcade.color.WHITE, 3)
    arcade.draw_point(505, 455, arcade.color.WHITE, 3)
    arcade.draw_point(507, 457, arcade.color.WHITE, 3)
    arcade.draw_point(498, 453, arcade.color.WHITE, 3)
    arcade.draw_point(496, 455, arcade.color.WHITE, 3)
    arcade.draw_point(494, 457, arcade.color.WHITE, 3)

    # Draw Second Seagull
    arcade.draw_point(470, 460, arcade.color.WHITE, 3)
    arcade.draw_point(473, 463, arcade.color.WHITE, 3)
    arcade.draw_point(475, 465, arcade.color.WHITE, 3)
    arcade.draw_point(477, 467, arcade.color.WHITE, 3)
    arcade.draw_point(468, 463, arcade.color.WHITE, 3)
    arcade.draw_point(466, 465, arcade.color.WHITE, 3)
    arcade.draw_point(464, 467, arcade.color.WHITE, 3)

    # Draw Third Seagull
    arcade.draw_point(535, 455, arcade.color.WHITE, 3)
    arcade.draw_point(538, 457, arcade.color.WHITE, 3)
    arcade.draw_point(541, 459, arcade.color.WHITE, 3)
    arcade.draw_point(544, 461, arcade.color.WHITE, 3)
    arcade.draw_point(533, 457, arcade.color.WHITE, 3)
    arcade.draw_point(531, 459, arcade.color.WHITE, 3)
    arcade.draw_point(529, 461, arcade.color.WHITE, 3)


# Ocean Function
def ocean():
    # Draw Ocean
    arcade.draw_rectangle_filled(300, 180, 600, 58, arcade.color.BLUEBONNET)
    arcade.draw_rectangle_filled(600, 60, 180, 183, arcade.color.BLUEBONNET)


# Wave Function

def lines():
    # Draw Waves
    arcade.draw_line(0, 200, 200, 200, arcade.color.WHITE)
    arcade.draw_line(150, 180, 240, 180, arcade.color.WHITE)
    arcade.draw_line(220, 200, 280, 200, arcade.color.WHITE)
    arcade.draw_line(300, 200, 350, 200, arcade.color.WHITE)
    arcade.draw_line(450, 200, 550, 200, arcade.color.WHITE)
    arcade.draw_line(30, 180, 100, 180, arcade.color.WHITE)
    arcade.draw_line(370, 180, 490, 180, arcade.color.WHITE)
    arcade.draw_line(0, 170, 20, 170, arcade.color.WHITE)
    arcade.draw_line(100, 170, 170, 170, arcade.color.WHITE)
    arcade.draw_line(300, 170, 380, 170, arcade.color.WHITE)
    arcade.draw_line(560, 170, 610, 170, arcade.color.WHITE)
    arcade.draw_line(550, 155, 590, 155, arcade.color.WHITE)

    arcade.draw_line(530, 85, 540, 85, arcade.color.WHITE)
    arcade.draw_line(550, 75, 570, 75, arcade.color.WHITE)
    arcade.draw_line(580, 65, 590, 65, arcade.color.WHITE)
    arcade.draw_line(550, 95, 570, 95, arcade.color.WHITE)
    arcade.draw_line(520, 105, 540, 105, arcade.color.WHITE)
    arcade.draw_line(530, 55, 580, 55, arcade.color.WHITE)
    arcade.draw_line(520, 35, 535, 35, arcade.color.WHITE)
    arcade.draw_line(560, 25, 590, 25, arcade.color.WHITE)
    arcade.draw_line(560, 125, 590, 125, arcade.color.WHITE)


# Towel Function
def towel():
    # Draw Towel
    arcade.draw_rectangle_filled(50, 75, 80, 120, arcade.color.CARMINE)
    arcade.draw_line(10, 75, 90, 75, arcade.color.WHITE, 3)
    arcade.draw_line(10, 100, 90, 100, arcade.color.WHITE, 3)
    arcade.draw_line(10, 35, 90, 35, arcade.color.WHITE, 3)
    arcade.draw_line(10, 55, 90, 55, arcade.color.WHITE, 3)
    arcade.draw_line(10, 120, 90, 120, arcade.color.WHITE, 3)


def sand():
    # Draw Sand
    arcade.draw_lrtb_rectangle_filled(0, 599, 150, 0, arcade.color.BLANCHED_ALMOND)


# Rocks in Sand Function
def sand_detail():
    # Draw Dots in Sand
    arcade.draw_circle_filled(75, 50, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(50, 70, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(150, 80, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(300, 50, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(350, 90, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(180, 85, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(20, 40, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(150, 100, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(110, 40, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(470, 40, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(380, 60, 2, arcade.color.BLACK)


# Palm Tree Function
def palm_tree():
    # Draw Palm Tree
    arcade.draw_rectangle_filled(120, 285, 20, 300, arcade.csscolor.SIENNA)

    # Palm Tree Leaves
    arcade.draw_arc_filled(160, 380, 100, 50, arcade.color.APPLE_GREEN, 0, 180)
    arcade.draw_arc_filled(70, 380, 100, 50, arcade.color.APPLE_GREEN, 0, 180)
    arcade.draw_arc_filled(160, 420, 100, 50, arcade.color.APPLE_GREEN, 0, 180)
    arcade.draw_arc_filled(160, 400, 100, 50, arcade.color.APPLE_GREEN, 0, 180)
    arcade.draw_arc_filled(70, 400, 100, 50, arcade.color.APPLE_GREEN, 0, 180)
    arcade.draw_arc_filled(70, 420, 100, 50, arcade.color.APPLE_GREEN, 0, 180)

    # Draw Coconuts
    arcade.draw_ellipse_filled(120, 370, 10, 20, arcade.color.BITTER_LIME)
    arcade.draw_ellipse_filled(90, 370, 10, 20, arcade.color.BITTER_LIME)
    arcade.draw_ellipse_filled(110, 400, 10, 20, arcade.color.BITTER_LIME)


# Sun Function
def sun(x, y):
    # Draw Sun
    arcade.draw_circle_filled(x, y, 40, arcade.color.YELLOW)


class Seagull:
    """Seagull Class"""

    def __init__(self, position_x, position_y):
        """ Initializer """
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        # Draws Seagull
        arcade.draw_point(self.position_x, self.position_y, arcade.color.WHITE, 3)
        arcade.draw_point(self.position_x + 3, self.position_y + 2, arcade.color.WHITE, 3)
        arcade.draw_point(self.position_x + 6, self.position_y + 4, arcade.color.WHITE, 3)
        arcade.draw_point(self.position_x + 9, self.position_y + 6, arcade.color.WHITE, 3)
        arcade.draw_point(self.position_x - 2, self.position_y + 2, arcade.color.WHITE, 3)
        arcade.draw_point(self.position_x - 4, self.position_y + 4, arcade.color.WHITE, 3)
        arcade.draw_point(self.position_x - 6, self.position_y + 6, arcade.color.WHITE, 3)


class Babygull:
    """Baby Seagull Class"""

    def __init__(self, position_x, position_y, change_x, change_y, size):
        """ Initializer """
        self.border_sound = arcade.load_sound("Babygull.wav")
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.size = size

    def draw(self):
        """Called to draw Baby Seagull"""
        # Draws Baby Seagull
        arcade.draw_point(self.position_x, self.position_y, arcade.color.WHITE, self.size)
        arcade.draw_point(self.position_x + 2, self.position_y + 3, arcade.color.WHITE, self.size)
        arcade.draw_point(self.position_x + 4, self.position_y + 5, arcade.color.WHITE, self.size)
        arcade.draw_point(self.position_x - 2, self.position_y + 3, arcade.color.WHITE, self.size)
        arcade.draw_point(self.position_x - 4, self.position_y + 5, arcade.color.WHITE, self.size)

    def update(self):
        """Called when keyboard controlled Seagull tried to leave window"""
        # Moves Baby Seagull
        self.position_y += self.change_y
        self.position_x += self.change_x
        # Checks to see if Baby Seagull hits edge of screen. If so, change direction
        if self.position_x < self.size:
            self.position_x = self.size
            arcade.play_sound(self.border_sound)

        if self.position_x > SCREEN_WIDTH - self.size:
            self.position_x = SCREEN_WIDTH - self.size
            arcade.play_sound(self.border_sound)

        if self.position_y < self.size:
            self.position_y = self.size
            arcade.play_sound(self.border_sound)

        if self.position_y > SCREEN_HEIGHT - self.size:
            self.position_y = SCREEN_HEIGHT - self.size
            arcade.play_sound(self.border_sound)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(600, 600, "Lab 7 - User Control")

        # Make the mouse disappear when it is over the window.
        self.set_mouse_visible(False)

        # Sets Baby Seagull in the Palm Tree
        self.baby = Babygull(90, 385, 0, 0, 3)

        #
        self.seagull = Seagull(100, 450)
        self.click_sound = arcade.load_sound("Seagull.wav")

    def on_draw(self):
        """Called to draw all functions and classes."""

        # Sky Function

        draw_sky()

        # Sand Function

        sand()

        # Ocean Function

        ocean()

        # Waves Function

        lines()

        # Seagull Function

        draw_seagulls()

        # Towel Function

        towel()

        # Rock Function

        sand_detail()

        # Palm Tree Function

        palm_tree()

        # Calls Sun function and sets Sun function at 520 x and 520 y
        sun(520, 520)

        # Draws Seagull
        self.seagull.draw()

        # Draws Baby Seagull
        self.baby.draw()

    def update(self, delta_time):
        """Called to update keyboard controlled Seagull """
        self.baby.update()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.seagull.position_x = x
        self.seagull.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.click_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.click_sound)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.baby.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.baby.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.baby.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.baby.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.baby.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.baby.change_y = 0


def main():
    # End of Main Method #
    window = MyGame()
    arcade.run()
main()
