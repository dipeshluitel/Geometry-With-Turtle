import turtle
import turtle as t


drawer = t.Turtle()


def draw(sides, angle, no_of_sides):
    for i in range(no_of_sides):
        drawer.forward(sides)
        drawer.right(angle)


turtle.speed(20)
screen = t.Screen()
screen.listen()
