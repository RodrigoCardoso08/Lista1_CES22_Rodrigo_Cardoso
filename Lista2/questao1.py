import turtle  # Tess becomes a traffic light. 2


turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be 28 
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor. 

# This variable holds the current state of the machine 42
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:  # Transition from state 0 to state 1 48
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:  # Transition from state 1 to state 2 52
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0


# Bind the event handler to the space key.
def turn_red():
    tess.fillcolor("red")


def turn_green():
    tess.fillcolor("green")


def turn_orange():
    tess.fillcolor("orange")


def turn_up_pen_size():
    new_size_up = tess.pensize() + 1
    if new_size_up > 20:
        new_size_up = 20

    tess.pensize(new_size_up)


def turn_down_pen_size():
    new_size_down = tess.pensize() - 1
    if new_size_down < 1:
        new_size_down = 1

    tess.pensize(new_size_down)


def turn_invisible():
    tess.hideturtle()


def turn_visible():
    tess.showturtle()


wn.onkey(turn_red, "r")
wn.onkey(turn_orange, "o")
wn.onkey(turn_green, "g")
wn.onkey(turn_up_pen_size, "+")
wn.onkey(turn_down_pen_size, "-")
wn.onkey(advance_state_machine, "space")
wn.onkey(turn_visible, "s")
wn.onkey(turn_invisible, "i")

wn.listen()  # Listen for events
wn.mainloop()
