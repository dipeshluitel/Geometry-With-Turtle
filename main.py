from drawer import draw


start = ""
print("-------------------------WELCOME TO GEOMETRIC SHAPE BUILDER---------------------")

shapes = int(input("Enter what you want to draw:press\n(1) Triangle\n(2)Quadrilaterals\n(3) Pentagon\n(4) Hexagon\n:"))
no_of_sides = 3 if shapes == 1 else 4 if shapes == 2 else 5 if shapes == 3 else 6 if shapes == 4 else 0

if no_of_sides != 0:

    perimeter = int(input("Input The perimeter of geometric shape: "))
    print(f"The perimeter of geometric shape is {perimeter}")
    lengths = perimeter / no_of_sides
    print(f"\n{lengths} will be the number of sides")
    angle = 360 / no_of_sides

    draw(lengths, angle, no_of_sides)

else:
    print("Invalid Shapes Selected")
