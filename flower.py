import turtle
import random

a = turtle
barvy = ["hotpink", "blueviolet", "fuchsia", "salmon"]

# květy kytičky
for i in range(18):
    for ii in range(4):
        a.speed(15)
        a.pencolor(random.choice(barvy))
        a.forward(50)
        a.left(90)
    a.left(20)
a.right(90)

# stonek naváže a vytvoří listy
a.speed(3)
a.pencolor("darkgreen")
a.forward(100)

for g in range(5, 55, 5):
    if g % 2 == 0:
        a.left(90)
        a.forward(g)
        a.left(45)
        a.forward(g)
        a.left(135)
        a.forward(g)
        a.left(45)
        a.forward(g)
        a.left(45)
        a.forward(g)
    else:
        a.right(90)
        a.forward(g)
        a.right(45)
        a.forward(g)
        a.right(135)
        a.forward(g)
        a.right(45)
        a.forward(g)
        a.right(45)
        a.forward(g)

a.exitonclick()