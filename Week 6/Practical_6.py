#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# your name
# your six-digit student number
#-------------------------------------------------------------------------------

import graphics as g
import math
import random as rand

def distBetweenPoints(a, b):
    return math.sqrt((b.getX() - a.getX()) ** 2 + (b.getY() - a.getY()) ** 2)

def drawCircle(window, center, radius, colour):
    circle = g.Circle(center, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(window)

def drawColouredEye(window, center, radius, colour):
    drawCircle(window, center, radius, "")
    drawCircle(window, center, radius / 2, "brown")
    drawCircle(window, center, radius / 3, "black")

def fastFoodOrderPrice():
    price = float(input("Price of pizza: "))

    if price < 10.00:
        price += 1.50
    print("Cost of pizza is £", price)

def whatToDoToday():
    temp = int(input("What is the temp outside: "))

    if temp < 10:
        print("stay in")
    elif temp > 10 and temp < 25:
        print("Go GunWharf")
    elif temp > 25:
        print("Get Nekid and sun bathe")
    else:
        print("What is even happening?")

def squareRoot(num1, num2):
    for i in range(num1, num2):
        print("square root of ", i, " = ", math.sqrt(i))

def calculateGrade():
    grade = int(input("Enter grade: "))

    if grade >= 16:
        print("a".upper())
    elif grade >= 12:
        print("b".upper())
    elif grade >= 8:
        print("c".upper())
    elif grade >= 7:
        print("f".upper())
    else:
        print("You majorly fucked up")

def peasInAPod():
    peas = int(input("Number of peas? : "))

    window = g.GraphWin("Peas in pod", peas * 100, 100)

    for i in range(peas):
        pea = g.Circle(g.Point(i * 100 + 50, 50), 50).draw(window).setFill("green")

    window.getMouse()

def ticketPrice(age, distance):
    discount = 0
    if age <= 15 or age >= 60:
        discount = 0.60
    else:
        discount = 1.00

    return discount * (3.00 + (0.15 * distance))

def numberedSquare(num):
    for i in range(num, 0, -1):
        for j in range(num):
            print(str(i + j), end= " ")
        print("")

def eyeColor():
    window = g.GraphWin("Eye Color", 200, 200)

    size = int(input("Enter size: "))
    color = input("Enter colour".lower())
    pos = int(input("Enter position, x then y: ").split())

    drawColouredEye(window, g.Point(pos[0], pos[1]), size, color)

    window.getMouse()

def drawPatchWindow():
    window = g.GraphWin("ID Num 9", 100, 100)

    for x in range(0, 100, 20):
        g.Line(g.Point(x, 0), g.Point(100, 100 - x)).draw(window)
        g.Line(g.Point(100 - x, 0), g.Point(0, 100-x)).draw(window)

        g.Line(g.Point(0, x), g.Point(100 - x, 100)).draw(window)
        g.Line(g.Point(100, 100 - x), g.Point(100 - x, 100)).draw(window)


    window.getMouse()

def drawPatch(window, pos_X, pos_Y):
    for x in range(pos_X, pos_X + 100, 10):
        #g.Line(g.Point(x, pos_Y), g.Point(pos_X + 100,  (pos_Y + 100) -x)).draw(window)
        #g.Line(g.Point((pos_X + 100) - x, pos_Y), g.Point(pos_X, (pos_Y + 100) - x)).draw(window)

        g.Line(g.Point(pos_X, pos_Y + x), g.Point((pos_X + 100) - x, pos_Y + 100)).draw(window)
        print(pos_X, pos_Y + x, (pos_X + 100) - x, pos_Y + 100)
        #g.Line(g.Point(pos_X + 100,(pos_Y + 100) - x), g.Point((pos_X + 100) - x, pos_Y + 100)).draw(window)

    window.getMouse()

def eyesAllAround():
    window = g.GraphWin("Eyes All Around")

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    colors_score = 0

    for i in range(0, 30):
        drawColouredEye(window, window.getMouse(),30, colors[colors_score])
        colors_score =+ 1

        if colors_score == 4:
            colors_score = 0
    window.getMouse()


def archeryGame():
    window = g.GraphWin("Archery Game", 200, 200)

    drawCircle(window, g.Point(100, 100), 50, "")
    drawCircle(window, g.Point(100, 100), 30, "brown")
    drawCircle(window, g.Point(100, 100), 15, "black")

    score = 0
    score_Label = g.Text(g.Point(40, 40), "").draw(window)

    for i in range(5):
        click = window.getMouse()
        distance = distBetweenPoints(click, g.Point(100, 100))

        drawCircle(window, g.Point(click.getX() + rand.randint(-10, 10),
                            g.Point(click.getY() + rand.randint(-10, 10)), 10), "pink")

        if distance <= 60 and distance >= 30:
            score += 2
            score_Label.setText("2 Points")
        elif distance <= 30 and distance >= 15:
            score += 5
            score_Label.setText("5 Points")
        elif distance <= 15:
            score += 10
            score_Label.setText("10 Points")
        else:
            score_Label.setText("Missed")

    score_Label.setText("Total: ", score)
    window.getMouse()

window = g.GraphWin("Grapher", 400, 400)
drawPatch(window, 100, 100)