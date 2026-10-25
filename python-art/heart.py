
from turtle import *
import math

bgcolor("black")
speed(0)
color("pink")
pensize(2)

def heart(n):
    x = 15 * math.sin(n) ** 3
    y = (
        12 * math.cos(n)
        - 5 * math.cos(2 * n)
        - 2 * math.cos(3 * n)
        - math.cos(4 * n)
    )
    return x, y

for i in range(1, 17):
    penup()
    for j in range(101):
        x, y = heart(j / 15)
        goto(x * i, y * i)
        if j == 0:
            pendown()

    penup()

hideturtle()
done()
