import turtle


def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(200)
        some_turtle.left(135)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("purple")
    emma = turtle.Turtle()
    emma.shape("turtle")
    emma.speed(20)
    emma.color("white")
    for i in range (1,37):
        draw_triangle(emma)
        emma.right(10)
"""
    #next turtle
    connor = turtle.Turtle()
    connor.shape("arrow")
    connor.color("Green")
    connor.circle(150)
    #next turtle
    kenneth = turtle.Turtle()
    kenneth.shape("arrow")
    kenneth.color("pink")
    draw_triangle(kenneth)
"""

draw_art()
turtle.getscreen()._root.mainloop()
