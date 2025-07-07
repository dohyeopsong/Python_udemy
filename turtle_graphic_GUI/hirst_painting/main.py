# import colorgram

# colors = []

# color_list = colorgram.extract(r'C:\Users\user\Desktop\project\Python_udemy\turtle_graphic_GUI\hirst_painting\image.jpg', 30)
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors.append((r, g, b))

# print(colors)

        
import turtle as t
import random

colours = [(236, 236, 234), (140, 22, 67), (77, 107, 190), (142, 151, 43), (235, 211, 82), (218, 164, 56), (110, 151, 220), (232, 205, 218), (60, 128, 
64), (178, 68, 142), (3, 67, 152), (207, 105, 56), (152, 99, 66), (228, 229, 233), (149, 37, 36), (232, 235, 233), (230, 177, 202), (45, 81, 
166), (183, 79, 145), (193, 141, 169), (34, 34, 34), (175, 186, 218), (133, 174, 136), (91, 150, 94), (213, 182, 176), (176, 202, 185)]  

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_number in range(1,  number_of_dots + 1 ):
    tim.dot(20, random.choice(colours))
    tim.forward(50)

    if dot_number % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = t.Screen()
screen.exitonclick()
