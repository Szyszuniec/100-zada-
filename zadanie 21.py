# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance
# from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.

print("Input direction (UP/DOWN/LEFT/RIGHT) and number of steps:")
pos = [0, 0]

while True:
    data = input()
    if data == "END":
        break
    move = data.split(" ")
    direction = move[0]
    distance = move[1]
    if direction == "UP":
        pos[1] += int(distance)
    if direction == "DOWN":
        pos[1] -= int(distance)
    if direction == "LEFT":
        pos[0] -= int(distance)
    if direction == "RIGHT":
        pos[0] += int(distance)

print("End position: {}".format(pos))
translation = ((pos[0])**2 + (pos[1])**2)**(0.5)
print("Distance from start: {}".format(translation))
print("Distance rounded: {}".format(round(translation)))