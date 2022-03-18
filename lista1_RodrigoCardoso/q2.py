import turtle

def draw_poly(t,n, sz):
    angulo = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(angulo)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")
tess = turtle.Turtle()
tess.pencolor('red')

draw_poly(tess,8,50)
wn.mainloop()

