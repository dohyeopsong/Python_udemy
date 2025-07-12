from turtle import Turtle, Screen
screen = Screen()

snake_segments = []

class SnakeSegment(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        if snake_segments:
            last_segment = snake_segments[-1]
            self.goto(last_segment.xcor() - 20, last_segment.ycor())
        else:
            self.goto(0, 0)
        self.setheading(0)  # Facing right
        self.speed(1)
        snake_segments.append(self)

    def move_snake():
        # Move each segment to the position of the segment in front of it
        for seg_num in range(len(snake_segments) - 1, 0, -1):
            new_x = snake_segments[seg_num - 1].xcor()
            new_y = snake_segments[seg_num - 1].ycor()
            snake_segments[seg_num].goto(new_x, new_y)
        
        # Move the head forward
        snake_segments[0].forward(20)
        screen.update()  # NOW update the screen to show all movements at once

    

