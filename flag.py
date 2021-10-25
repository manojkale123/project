#importing turtle module
import turtle
#Geeting a scrren
ws=turtle.Screen()
#define a turtle instance
flagturtle=turtle.Turtle()
#intially penup()
flagturtle.penup()
#intitally setting position
flagturtle.goto(-180,60)

#First rectangle and orange color

flagturtle.pendown()
flagturtle.begin_fill()
flagturtle.fillcolor("orange")
flagturtle.left(90)
flagturtle.forward(90)
flagturtle.right(90)
flagturtle.forward(400)
flagturtle.right(90)
flagturtle.forward(90)
flagturtle.right(90)
flagturtle.forward(400)
flagturtle.end_fill()

#second rectangle
flagturtle.left(90)
flagturtle.forward(90)
flagturtle.left(90)
flagturtle.forward(400)
flagturtle.left(90)
flagturtle.forward(90)
flagturtle.left(90)
flagturtle.forward(400)
flagturtle.left(90)
flagturtle.forward(90)

#for third rectangel and filling green color

flagturtle.begin_fill()
flagturtle.fillcolor("green")
flagturtle.forward(90)
flagturtle.left(90)
flagturtle.forward(400)
flagturtle.left(90)
flagturtle.forward(90)
flagturtle.left(90)
flagturtle.forward(400)
flagturtle.end_fill()

flagturtle.penup()
flagturtle.goto(23,32)
flagturtle.pendown()
flagturtle.begin_fill()
flagturtle.fillcolor("blue")
flagturtle.circle(20)
flagturtle.end_fill()

#keep the the 
turtle.done()