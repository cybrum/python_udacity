import turtle

def draw_leaves(some_turtle):
    some_turtle.begin_fill()
    some_turtle.right(45)
    some_turtle.circle(110,90)
    some_turtle.left(90)
    some_turtle.circle(110,90)
    some_turtle.end_fill()
    
def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")
        
    obj1 = turtle.Turtle()
    obj1.shape("turtle")
    obj1.speed(20)

    # draw stalk
    obj1.color("#8BC03C", "#A7E748")
    obj1.begin_fill()
    obj1.right(45)
    obj1.circle(-260,90)
    obj1.setheading(180)
    obj1.forward(10)
    obj1.right(135)
    obj1.circle(260,90)
    obj1.setheading(0)
    obj1.forward(10)
    obj1.end_fill()

    # draw centre of flower
    obj1.color("#FFAB5D", "#FFEB5D")
    obj1.right(90)
    obj1.penup()
    obj1.forward(50)
    obj1.pendown()
    obj1.left(90)
    obj1.begin_fill()
    obj1.circle(50)
    obj1.end_fill()
    obj1.penup()
    obj1.home()
    obj1.pendown()
    
    # draw leaves
    intNumLeaves = 12
    obj1.color("#926FDA", "#C090FF")
    
    for intLeaves in range(1, intNumLeaves+1):
        obj1.penup()
        obj1.forward(50)
        obj1.pendown()
        draw_leaves(obj1)
        obj1.penup()
        obj1.home()
        obj1.right(intLeaves*(360/intNumLeaves))

    obj1.left(90)
    obj1.color("#FFAB5D", "#FFEB5D")
    
    window.exitonclick()

draw_flower()
