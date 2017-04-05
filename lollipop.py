import turtle

def draw():
    mycanvas = turtle.Screen()
    mycanvas.bgcolor('black')
    myturtle = turtle.Turtle(shape='turtle')
    myturtle.speed(0)
    myturtle.penup()
    myturtle.goto(0,-350)
    myturtle.left(90)
    myturtle.pendown()
    myturtle.pensize(5)
    myturtle.color('green')
    myturtle.forward(350)
    myturtle.pensize(2)
    colors = ['white', 'yellow', 'green', 'red', 'blue']
    c = 0
    for i in range (200):
        myturtle.color(colors[c])
        for l in range (4):
            myturtle.forward(150)
            myturtle.right(90)
        c = c + 1
        if (c > 4):
            c = 0
        myturtle.right(11)
    myturtle.penup()
    myturtle.goto(0,310)
    myturtle.color("white")
    myturtle.write("Eric's Turtle Mini Project :-)", None, "center", "16pt")
    myturtle.goto(0,340)

draw()
