import turtle

turtle.color('green')
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.goto(100,20)
turtle.color('red')
turtle.pendown()
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.done()