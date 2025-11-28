import turtle

drawing_board=turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Drawing")

turtle_instance=turtle.Turtle()
turtle_instance.color("blue")

turtle_colors=["red","purple","green","yellow","blue","magenta","cyan"]

for i in range(15):
    turtle_instance.color(turtle_colors[i%7])
    turtle_instance.circle(20*i)
    turtle_instance.circle(-20*i)
    turtle_instance.left(i)




turtle.done()