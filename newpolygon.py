import turtle

bob = turtle.Turtle()
print(bob)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)
    #for i in range(n):
        #t.fd(length)
        #t.lt(angle)


polygon(bob, 7, 70)

import math

#def circle(t, radius):
    #circumference = 2.0 * math.pi * radius
    #n = 50
    #length = circumference / n
    #polygon(t, n, length)




def arc(t, r, angle):
    arc_length = 2.0 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

    #for i in range(n):
        #t.fd(step_length)
        #t.lt(step_angle)

arc(bob, 30, 45)


def circle(t, r):
    arc(t, r, 360)


circle(bob, 100)


turtle.mainloop()