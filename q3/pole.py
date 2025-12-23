import turtle

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length
    
    def showpole(self):
        p = turtle.Turtle()
        p.penup()
        p.goto(self.pxpos, self.pypos)
        p.pendown()

        p.setheading(0)
        p.forward(self.pthick/2)
        p.setheading(90)
        p.forward(self.plength)
        p.setheading(180)
        p.forward(self.pthick)
        p.setheading(270)
        p.forward(self.plength)
        p.setheading(0)
        p.forward(self.pthick/2)

        turtle.done()

    def pushdisk(self, disk):
        # end of the list is the top
        self.stack.append(disk)

    def popdisk(self):
        return self.stack.pop()
        
if __name__ == "__main__":
    Pole().showpole()
    # x = Turtle()
    # y = 5
    # z = 50
    # a = 360.0 / y
    # for i in range(y):
    #     x.forward(z)
    #     x.right(a)

    # done()