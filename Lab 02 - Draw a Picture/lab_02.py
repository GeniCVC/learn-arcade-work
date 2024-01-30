# Written on 1/30/23 By Matthew Jackson

# Imports arcade library
import arcade

# Opens Window
arcade.open_window(600, 600, "Drawing Example")

# Sets background color
arcade.set_background_color(arcade.color.BALL_BLUE)

# Gets program ready to draw
arcade.start_render()

# Draw Sand
arcade.draw_lrtb_rectangle_filled(0, 599, 150, 0, arcade.color.BLANCHED_ALMOND)
# Dots in Sand
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

# Draw Sun
arcade.draw_circle_filled(520, 550, 40, arcade.color.YELLOW)

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

# Draw Towel
arcade.draw_rectangle_filled(50, 75, 80, 120, arcade.color.CARMINE)
arcade.draw_line(10, 75, 90, 75, arcade.color.WHITE, 3)
arcade.draw_line(10, 100, 90, 100, arcade.color.WHITE, 3)
arcade.draw_line(10, 35, 90, 35, arcade.color.WHITE, 3)
arcade.draw_line(10, 55, 90, 55, arcade.color.WHITE, 3)
arcade.draw_line(10, 120, 90, 120, arcade.color.WHITE, 3)

# Draw Ocean
arcade.draw_rectangle_filled(600, 60, 180, 183, arcade.color.BLUEBONNET)
arcade.draw_line(530, 85, 540, 85, arcade.color.WHITE)
arcade.draw_line(550, 75, 570, 75, arcade.color.WHITE)
arcade.draw_line(580, 65, 590, 65, arcade.color.WHITE)
arcade.draw_line(550, 95, 570, 95, arcade.color.WHITE)
arcade.draw_line(520, 105, 540, 105, arcade.color.WHITE)
arcade.draw_line(530, 55, 580, 55, arcade.color.WHITE)
arcade.draw_line(520, 35, 535, 35, arcade.color.WHITE)
arcade.draw_line(560, 25, 590, 25, arcade.color.WHITE)
arcade.draw_line(560, 125, 590, 125, arcade.color.WHITE)

# Finishes Drawing
arcade.finish_render()

# Keeps running the windows until closed.
arcade.run()
