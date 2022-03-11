import turtle

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")
alex = turtle.Turtle()
alex.pencolor('red')
draw_square(alex,20)
alex.up()
alex.setposition(-10.0,-10.0)
alex.down()
draw_square(alex,40)
alex.up()
alex.setposition(-20.0,-20.0)
alex.down()
draw_square(alex,60)
alex.up()
alex.setposition(-30.0,-30.0)
alex.down()
draw_square(alex,80)
alex.up()
alex.setposition(-40.0,-40.0)
alex.down()
draw_square(alex,100)
wn.mainloop()


