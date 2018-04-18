import turtle

def draw_M(some_turtle):
    some_turtle.left(90)
    some_turtle.forward(100)
    some_turtle.right(135)
    some_turtle.forward(100)
    some_turtle.left(90)
    some_turtle.forward(100)
    some_turtle.right(135)
    some_turtle.forward(100)

def draw_A(some_turtle):
    some_turtle.left(60)
    some_turtle.forward(120)
    some_turtle.right(120)
    some_turtle.forward(120)
    some_turtle.left(180)
    some_turtle.forward(60)
    some_turtle.left(60)
    some_turtle.forward(60)

def draw_initials():
    window = turtle.Screen()
    window.bgcolor("yellow")

    muco = turtle.Turtle()
    muco.shape("arrow")
    muco.color("blue")
    muco.speed(2)

    muco.penup()
    muco.setposition(-250,0)
    muco.pendown()
    
    draw_M(muco)
    muco.penup()
    muco.setposition(-50, 0)
    muco.pendown()
    muco.left(90)
    draw_M(muco)
    muco.penup()
    muco.setposition(150, 0)
    muco.pendown()
    muco.left(90)
    draw_A(muco)

    window.exitonclick()

draw_initials()
