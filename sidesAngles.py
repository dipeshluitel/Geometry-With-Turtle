lengths = []
angles = []


def side_length(sides):
    for i in range(sides):
        lengths.append(input(f"Input side length {i+1} :"))


def angleinput(sides):
    for i in range(sides):
        angles.append(input(f"Input {i+1} angle:"))
