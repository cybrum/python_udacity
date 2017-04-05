import turtle

def draw_rhombus(other_turtle):
    for i in range(1, 3):
        other_turtle.forward(120)
        other_turtle.left(135)
        other_turtle.forward(50)
        other_turtle.left(45)

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("green")

    fred= turtle.Turtle()
    fred.shape("square")
    fred.color("red")
    fred.speed(20)
    draw_rhombus(fred)
    for i in range(1,73):
        fred.left(5)
        draw_rhombus(fred)
    fred.right(90)
    fred.forward(150)
        
    window.exitonclick()
draw_shape()
