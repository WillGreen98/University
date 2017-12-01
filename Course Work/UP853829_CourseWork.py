__author__ = "Will - UP853829"
__project__ = "Patterns Course Word"

import graphics as g
import random as rand
import numbers

DEBUG = False

# Could I use a dictionary for both valid colours and entered colours
# Checking both against each other - this could reduce line count

valid_colours = ["red", "green", "blue", "magenta", "cyan", "orange", "brown", "pink"]

def getInput():
    size_Index = 0
    val_Dimensions = [5, 7, 9, 11]

    colour_Choices = []

    while True:
        dimensions = input("Enter dimension: ")
        if dimensions.isnumeric(): #__contains__(filter(lambda i: isinstance(i, numbers.Number), val_Dimensions)):
            dimensions = int(dimensions)
            if dimensions % 2 == 1:
                if dimensions in val_Dimensions:
                    break
                else:
                    print("X or Y value not a valid digit")
            else:
                print("Y value not even")
        else:
            print("Only numbers!")

    while True:
        colour = input("Enter colours: ")
        if colour  in valid_colours:
            if colour  not in colour_Choices:
                colour_Choices.append(colour)
            else:
                print("You cannot use the same colour twice")
        else:
            print("Invalid input your inputs must be one of {0}".format(valid_colours))
        if len(colour_Choices) >= 3:
            break

def draw_Patch_Penultimate(window, reversed):

    point_One = g.Point(0, 0)
    point_Two = g.Point(50, 0)
    point_Three = g.Point(50, 50)

    colour = ""

    poly = g.Polygon(point_One, point_Two, point_Three)
    poly.setFill(colour)
    poly.setOutline(colour)
    poly.draw(window)

    if reversed == False:
        for i in range(5):
            if i % 2 == 0:
                colour = "Red"
            else:
                colour = "White"

            point_One = g.Point(point_One.getX() + 10, point_One.getY())
            point_Two = g.Point(point_Two.getX(), point_Two.getY())
            point_three = g.Point(point_Three.getX(), point_Three.getY() - 10)
    elif reversed == True:
        for i in range(5):
            if i % 2 == 0:
                colour = "White"
            else:
                colour = "Red"
            point_One = g.Point(point_One.getX() - 10, point_One.getY())
            point_Two = g.Point(point_Two.getX(), point_Two.getY())
            point_three = g.Point(point_Three.getX(), point_Three.getY() + 10)


def drawLine(window, x1, y1, x2, y2, colour):
    line = g.Line(g.Point(x1, y1), g.Point(x2, y2)).draw(window)
    line.setFill(colour)

def draw_Patch_Final(window, pos_x, pos_y, colour):
    x = pos_x
    y = pos_y

    while x < pos_x + 100 and y < pos_y + 100:
        # TODO Flip Coordinates for reverted pattern
        # If X and Y are different values, pattern diverges
        #Top Left to Bottom Right
        drawLine(window, pos_y, x, (2 * pos_y) + 100 - x, pos_x + 100, colour) # Problem line
        drawLine(window, y, pos_x, pos_y + 100, (2 * pos_x) + 100 - x, colour)

        #Top Right to Bottom Left
        drawLine(window, y, pos_x, pos_y, x, colour)
        drawLine(window, pos_y + 100, x, y, pos_x + 100, colour)

        x += 20
        y += 20

        if DEBUG:
            print("x1: ", pos_y, " y1: ", x, " x2: ", ((2 * pos_y) + 100 - x), " y2: ", (pos_x + 100))

def main():
    window = g.GraphWin("Patch Work", 500, 500)

    getInput()

    draw_Patch_Penultimate(window, False)

    if DEBUG:
        draw_Patch_Final(window, 50, 50, "Red")
        draw_Patch_Final(window, 180, 180, "Black")
        draw_Patch_Final(window, 300, 250, "Green")
    else:
        for rows in range(0, 600, 100):
            for cols in range(0, 600, 100):
                draw_Patch_Final(window, rows + 100, cols + 100, rand.choice(valid_colours))


    window.getMouse()

if __name__ == '__main__':
    main()