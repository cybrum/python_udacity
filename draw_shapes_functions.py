import turtle
#ctrl+ [ for back tab
def draw_square():
    rect = turtle.Turtle()
    rect.shape("turtle")
    rect.color("red")
    rect.speed(4)

    turns = 0
    while turns < 4:
            rect.forward(100)
            rect.right(90)
            turns = turns + 1
    
def draw_circle():
    circle = turtle.Turtle()
    circle.shape("arrow")
    circle.color("blue")
    circle.circle(100)              
                
def draw_triangle():
    triangle = turtle.Turtle()
    triangle.shape("circle")
    triangle.color("green")
    
    turns = 0
    while turns < 3:
            triangle.right(120)
            triangle.forward(100)   
            turns = turns + 1

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("#B0F0F8")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()
                
draw_shapes()
