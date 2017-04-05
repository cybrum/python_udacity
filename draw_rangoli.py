import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art() :
    window = turtle.Screen()
    window.bgcolor("red")

    obj1 = turtle.Turtle()
    obj1.shape("turtle")
    obj1.color("yellow")
    obj1.speed(2)

    # for 360 degree, you need 36 times at 10 degree rotation
    for i in range (1,37) :     
        draw_square(obj1)
        obj1.right(10)

    window.exitonclick()

#if you use draw_square() below, then you will get below error
#TypeError: draw_square() missing 1 required positional argument: 'some_turtle'
draw_art()
