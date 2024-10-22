# import turtle as t
# my_pen = t.Turtle()

print("-------------------------WELCOME TO GEOMETRIC SHAPE BUILDER---------------------")

shapes = int(input("Enter what you want to draw:press\n(1) Triangle\n(2)Quadrilaterals\n(3) Pentagon\n:"))
no_of_sides = 3 if shapes == 1 else 4 if shapes == 2 else 5 if shapes == 3 else 0

