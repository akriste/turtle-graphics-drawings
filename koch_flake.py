
import turtle

t = turtle.Turtle()
t.ht()
wn = turtle.Screen()
wn.bgcolor("black")
t.speed(0)
barvy = ["blue", "steelblue", "slategray1"]
t.pu()
t.goto(-200, 0)
t.pd()

def koch(t, iterace, delka, zkraceni, uhel):
  if iterace == 0:
    t.forward(delka)
  else:
    iterace = iterace - 1
    delka = delka / zkraceni
    koch(t, iterace, delka, zkraceni, uhel)
    t.left(uhel)
    koch(t, iterace, delka, zkraceni, uhel)
    t.right(uhel * 2)
    koch(t, iterace, delka, zkraceni, uhel)
    t.left(uhel)
    koch(t, iterace, delka, zkraceni, uhel)

# for i in range(3):
#   t.pencolor( barvy[i % 3] )
#   koch(t, 4, 400, 3, 60)
#   t.right(120)

for i in range(3):
  t.pencolor( barvy[i % 3] )
  koch(t, 4, 500, 3, -60)
  t.right(120)

wn.exitonclick()
