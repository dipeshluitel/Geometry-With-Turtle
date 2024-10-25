import turtle
from turtle import Screen, Turtle

# drawer object created from class Turtle()
drawer = Turtle()


def draw(sides, angle, no_of_sides):  # function to draw requested geometric shapes
    turtle.speed(10)
    for _ in range(no_of_sides):
        drawer.forward(sides)
        drawer.right(angle)


# screen object created
screen = Screen()

start = ""
print("-------------------------WELCOME TO GEOMETRIC SHAPE BUILDER---------------------")

# User choice is taken on what should be drawn
shapes = int(screen.textinput("Shapes", "Enter what you want to draw:press\n(1) "
                                        "Triangle\n(2)Quadrilaterals\n(3) Pentagon\n(4) Hexagon\n:"))

# on the basis of shapes respective value for no_of_sides is assigned
no_of_sides = 3 if shapes == 1 else 4 if shapes == 2 else 5 if shapes == 3 else 6 if shapes == 4 else 0

if no_of_sides != 0:

    perimeter = int(screen.textinput(title="Shapes", prompt="Enter the perimeter of shape you have chosen to draw:"))
    print(f"The perimeter of geometric shape is {perimeter}")
    lengths = perimeter / no_of_sides
    print(f"\n{lengths} will be the length of one side")
    angle = 360 / no_of_sides

    # function call to draw the geometric shape
    draw(lengths, angle, no_of_sides)

else:
    print("Invalid Shapes Selected")

turtle.done()
