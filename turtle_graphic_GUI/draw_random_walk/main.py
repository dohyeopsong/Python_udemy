import turtle as t
import random

tim = t.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color



def random_walk(steps):
    for _ in range(steps):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice([0, 90, 180, 270]))

def main():
    t.colormode(255)
    tim.pensize(10)
    tim.speed("fastest")
    random_walk(200)

if __name__ == "__main__":
    main()
    screen = t.Screen()
    screen.exitonclick()  # Click on the window to close it