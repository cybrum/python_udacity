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
    
    draw_square(obj1)

    obj2 = turtle.Turtle()
    obj2.shape("arrow")
    obj2.color("blue")
    obj2.circle(100)
    

    window.exitonclick()

#if you use draw_square() below, then you will get below error
#TypeError: draw_square() missing 1 required positional argument: 'some_turtle'
draw_art()
