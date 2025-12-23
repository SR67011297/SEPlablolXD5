from turtle import *
def drawrect(t,x,y,w,h):
    t.goto(x,y)
    t.pendown()
    t.setheading(0)


    t.forward(w/2)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w/2)

    t.penup()


class Disk(object):
    def __init__(self,name="",xpos=0,ypos=0,height=20,width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.t = Turtle()
    def showdisk(self):
        
        self.t.goto(self.dxpos,self.dypos)
        self.t.pendown()
        self.t.setheading(0)
        self.t.forward(self.dwidth/2)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth/2)
        self.t.penup()
    def newpos(self,x,y):
        self.dxpos = x
        self.dypos = y

    def cleardisk(self):
        self.t.goto(self.dxpos,self.dypos)
        self.t.setheading(0)
        self.t.clear()

if __name__ == '__main__':
    d = Disk("lol")
    d.showdisk()
    l = input()

