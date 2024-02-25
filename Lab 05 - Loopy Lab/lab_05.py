import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():  # Draws First Section
    for row in range(30):
        for column in range(30):  # Creates white squares.
            x = column * 10 + 5  # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 5  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():  # Draws Second Section
    for row in range(30):
        for column in range(30):
            x = column * 10 + 305  # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 5  # Instead of zero, calculate the proper y location using 'row'
            if column % 2:  # Switches between white and black squares.
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_3():   # Draws Third Section
    for row in range(30):
        for column in range(30):
            x = column * 10 + 605  # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 5  # Instead of zero, calculate the proper y location using 'row'
            if row % 2:  # Switches between black and white squares vertically.
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_4():  # Draws Fourth Section
    for row in range(31):
        for column in range(31):
            x = column * 10 + 905  # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 - 5  # Instead of zero, calculate the proper y location using 'row'
            if column % 2 and row % 2:  # Creates more black squares than white ones
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_5():  # Draws Fifth Section
    for column in range(30):
        for row in range(column + 2):  # Creates a 'stairway' of white squares.
            x = column * 10 + 5  # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 295  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():   # Draws Sixth Section
    for row in range(30):
        for column in range(30 - row):  # Creates a reverse 'stairway' of white squares.
            x = column * 10 + 305  # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 305  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_7():  # Draws Seventh Section
    for row in range(60):
        for column in range(row - 1):  # Creates an upside down 'stairway' of white squares
            x = column * 10 + 605  # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 285  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():  # Draws Eighth Section
    for row in range(31):
        for column in range(row):  # Creates an upside down reverse 'stairway' of white squares
            x = 1195 - (column * 10)  # Instead of zero, calculate the proper x location using 'column'
            y = row * 10 + 295  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():  # Main Function
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)  # Sets background color

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
