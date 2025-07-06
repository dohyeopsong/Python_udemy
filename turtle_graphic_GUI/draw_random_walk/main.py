import turtle as t
import random

tim = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "Wheat", "SlateGray", "SeaGreen"]

def random_walk(steps):
    for _ in range(steps):
        tim.color(random.choice(colours))
        tim.forward(30)
        tim.setheading(random.choice([0, 90, 180, 270]))

def main():
    t.colormode(255)
    tim.pensize(10)
    tim.speed("fastest")
    random_walk(200)
    t.done()      