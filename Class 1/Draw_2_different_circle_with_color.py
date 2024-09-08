import turtle

turtle.color('blue')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.done()