import turtle as t
import random

tim = t.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

def main():
    t.colormode(255)
    tim.speed("fastest")
    draw_spirograph(5)

if __name__ == "__main__":
    main()
    screen = t.Screen()
    screen.exitonclick()