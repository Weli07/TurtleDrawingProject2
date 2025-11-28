import turtle

drawing_board=turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Drawing")

turtle_instance=turtle.Turtle()
turtle_instance.color("blue")

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading() + 10)
    #turtle_instance.right(10)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading() - 10)
    #turtle_instance.left(10)

def clear():
    turtle_instance.clear()
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()




drawing_board.listen()

drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotate_angle_right,key="Down")
drawing_board.onkey(fun=rotate_angle_left,key="Up")

drawing_board.onkey(fun=clear,key="c")






drawing_board.mainloop()

