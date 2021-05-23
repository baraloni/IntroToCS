###########################################################
# FILE : hello_turtle.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex1 2016-2017
# DESCRIPTION:  A simple program which draws 3 separated flowers
#  to the screen, using the turtle library.
#############################################################
import turtle


def draw_petal():
    """this function draws a petal using turtle"""
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)


def draw_flower():
    """draws a single flower using turtle"""
    turtle.right(45)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(135)
    turtle.forward(150)


def draw_flower_advanced():
    """draws a single flower using turtle, then stops drawing and
     moves the marker to the flower's side to create separation """
    draw_flower()
    turtle.left(90)
    turtle.up()
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.down()


def draw_flower_bed():
    """draws 3 separated flowers"""
    turtle.up()
    turtle.left(180)
    turtle.forward(200)
    turtle.right(180)
    turtle.down()
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()


turtle.done()