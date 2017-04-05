import turtle

def draw_stuff():
    window=turtle.Screen()
    window.bgcolor("red")

    obj1 = turtle.Turtle()
    obj1.shape("arrow")
    for x in range(0, 4):
        obj1.forward(100)
        obj1.right(90)

    obj2 = turtle.Turtle()
    obj2.shape("circle")
    obj2.color("blue")
    obj2.circle(100)

    obj3 = turtle.Turtle()
    obj3.shape("triangle")
    obj3.color("yellow")
    for y in range(0,2):
        obj3.left(90)
        obj3.forward(100)
    obj3.home()

    window.exitonclick()

draw_stuff()
