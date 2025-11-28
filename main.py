import turtle

drawing_board=turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Turtle Drawing")
drawing_board.title("Turtle Drawing Screen")

turtle_instance=turtle.Turtle()


# polygon

num_slides=5
angle=360.0/num_slides*2
side_length=200

for i in range(num_slides):
    turtle_instance.left(angle)
    turtle_instance.forward(side_length)

turtle.done()