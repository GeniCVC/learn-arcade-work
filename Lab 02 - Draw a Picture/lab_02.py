# Written on 1/30/23 By Matthew Jackson

# Imports arcade library
import arcade

# Opens Window and Names it
arcade.open_window(600, 600, "Day At The Beach")

# Sets background color
arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)

# Gets program ready to draw
arcade.start_render()

# Draws Sky
arcade.draw_rectangle_filled(300, 450, 600, 100, arcade.color.BONDI_BLUE)
arcade.draw_rectangle_filled(300, 350, 600, 100, arcade.color.BLUE_GREEN)
arcade.draw_rectangle_filled(300, 250, 600, 100, arcade.color.BALL_BLUE)

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

# Draw Sand
arcade.draw_lrtb_rectangle_filled(0, 599, 150, 0, arcade.color.BLANCHED_ALMOND)

# Draw First strip of Ocean
arcade.draw_rectangle_filled(300, 180, 600, 58, arcade.color.BLUEBONNET)
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

# Draw Rest of Ocean
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

# End of Program
