import turtle
t=turtle.Turtle()
t.shape('turtle')
t.color('white')
ts=turtle.getscreen()
ts.bgcolor('black')
t.pencolor('yellow')
t.speed(0)

while True:
    n=int(input('다각형'))
    i=n
    while (i>0):
        t.fd(100)
        t.lt(360/n)
        i-=1
