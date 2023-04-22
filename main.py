import turtle as t
import random





tim = t.Turtle()
t.colormode(255)
color_list = [(252, 251, 251), (254, 247, 247), (240, 253, 253), (244, 248, 248), (243, 236, 236), (198, 12, 12), (220, 160, 160), (43, 80, 80), (237, 229, 229), (238, 40, 40), (38, 215, 215), (32, 41, 41), (205, 73, 73), (21, 149, 149), (204, 33, 33), (74, 10, 10), (181, 17, 17), (217, 140, 140), (216, 161, 161), (56, 15, 15)]


tim.penup()
tim.setheading(220)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()

# #10X10 50 spaces
start = tim.pos()
for i in range(0,10):
    start = tim.pos()
    for j in range(0,10):
        tim.dot(15,random.choice(color_list))
        tim.penup()
        tim.forward(50)

    tim.goto(start[0],start[1]+40)

t.exitonclick()