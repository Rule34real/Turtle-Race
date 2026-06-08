#Θέλω να φτιάξετε 5 σχήματα για HW. Σε 5 διαφορετικές θέσεις του παραθυρου

import turtle
turtle.title("My Turtle Program")
scn=turtle.Screen()
scn.bgcolor("black")
t=turtle.Turtle()
t.pencolor("white")
t.fillcolor("red")
t.shapesize(2,2,1)
#Κυκλος
t.circle(60)
t.penup()
t.goto(100,100)
t.pendown()
#Βουλα
t.dot(50)
t.penup()
t.goto(-100,-100)
t.pendown()
#Τριγωνο
for i in range(0,3,1):
    t.rt(120)
    t.fd(100)
t.penup()
t.goto(200,200)
t.pendown()
#Τετραγωνο
for i in range(4):
    t.forward(100)
    t.right(90)
#Ορθογωνιο
t.penup()
t.goto(-300,200)
t.pendown()
for i in range(2):
    t.forward(150)
    t.right(90)
    t.forward(100)
    t.right(90)
turtle.done()