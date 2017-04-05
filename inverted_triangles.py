import turtle

def triangle(side, level):
    if level == 1:
        for i in range(3):
            turtle.fd(side)
            turtle.left(120)
    else:
        triangle(side/2, level-1)
        turtle.fd(side/2)
        triangle(side/2, level-1)
        turtle.bk(side/2)
        turtle.left(60)
        turtle.fd(side/2)
        turtle.right(60)
        triangle(side/2, level-1)
        turtle.left(60)
        turtle.bk(side/2)
        turtle.right(60)
def main():
    triangle(200, 4)

if __name__ == '__main__':
    main()
    turtle.mainloop()
