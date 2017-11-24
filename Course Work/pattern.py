__author__ = "Will - UP853829"
__project__ = "Patterns Course Word"

import graphics as g

colors = ["Black", "Blue", "Green", "Yellow", "Orange", "Red"]

def getInput():
    # 5x5 7x7 9x9 11x11
    dimensions = input("Enter grid (N N): ").split()

    di_X = int(dimensions[0])
    di_Y = int(dimensions[1])

    color = input("Enter colors (color 1 colour 1 color 3): ").split()
    col_One = color[0]
    col_Two = color[1]
    col_Three = color[2]

    print(col_Three, col_One, col_Two)

def draw_Patch_Penultimate(window):
    color = ""
    #
    # point_One = g.Point(0, 0)
    # point_Two = g.Point(50, 0)
    # point_Three = g.Point(50, 50)
    #
    # for i in range(5):
    #     if i % 2 == 0:
    #         color = "Red"
    #     else:
    #         color = "White"
    #
    #     poly = g.Polygon(point_One, point_Two, point_Three)
    #     poly.setFill(color)
    #     poly.setOutline(color)
    #     poly.draw(window)
    #
    #     point_One = g.Point(point_One.getX() + 10, point_One.getY())
    #     point_Two = g.Point(point_Two.getX(), point_Two.getY())
    #     point_three = g.Point(point_Three.getX(), point_Three.getY() - 10)


def drawLine(window, x1, y1, x2, y2, colour):
    line = g.Line(g.Point(x1, y1), g.Point(x2, y2))
    line.draw(window)
    line.setFill(colour)

def draw_Patch_Final(window, pos_x, pos_y, colour):
    x = pos_x
    y = pos_y
    print(x, y)

    while x < pos_x + 100 and y < pos_y + 100:
        print(pos_y, x, (2 * pos_y) + 100 + x, pos_x + 100)
        #draw_line(window, pos_y, x, (2 * pos_y) + 100 - x, pos_x + 100, colour)
        #draw_line(window, y, pos_x, pos_y + 100, (2 * pos_x) + 100 - x, colour)

        drawLine(window, x, pos_y, pos_x, y, colour)
        drawLine(window, pos_x + 100, y, x, pos_x + 100, colour)

        drawLine(window, y, pos_x, pos_y, x, colour)
        drawLine(window, pos_y + 100, x, y, pos_x + 100, colour)
        x += 20; y += 20

    window.getMouse()

def main():
    window = g.GraphWin("Patch Work", 500, 500)
    window.setCoords(0, 0, 100, 100)

    getInput()

    #draw_Patch_Final(window, 200, 50, "Red")
    draw_Patch_Penultimate(window)

    window.getMouse()

if __name__ == '__main__':
    main()