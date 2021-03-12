import turtle as t
import random

listi = ["darkgreen", "seagreen", "limegreen", "green", "darkolivegreen", "chartreuse2"]

t.speed(0)
t.bgcolor("black")
t.pencolor("silver")
t.ht()
t.penup()
t.goto(0, -450)
t.pendown()
t.left(90)

def vetveni(vetve_len):
    uhel = random.randint(28, 30)
    hustoty = random.uniform(0.5, 1) #hustota množení větvení
    tloustky = vetve_len / 15 #ztenčování
    t.pensize(tloustky)
    if vetve_len < 7:
        t.color(random.choice(listi))        
    elif vetve_len > 7:
        t.pencolor("silver") 
        t.forward(vetve_len)
        t.left(uhel)
        vetveni(vetve_len * hustoty)
        t.right(uhel * 2)
        vetveni(vetve_len * hustoty)
        t.left(uhel)
        t.backward(vetve_len)
    
vetveni(150)
t.exitonclick()