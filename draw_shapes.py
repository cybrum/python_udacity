import turtle

def draw_square() :
    window = turtle.Screen()
    window.bgcolor("red")

    obj1 = turtle.Turtle()
    obj1.shape("turtle")
    obj1.color("yellow")
    obj1.speed(2)
    
    obj1.forward(100)
    obj1.right(90)

    obj1.forward(100)
    obj1.right(90)
    
    obj1.forward(100)
    obj1.right(90)
    
    obj1.forward(100)
    obj1.right(90)

    obj2 = turtle.Turtle()
    obj2.shape("arrow")
    obj2.color("blue")
    obj2.circle(100)
    

    window.exitonclick()

draw_square()
