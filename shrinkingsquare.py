import turtle

drawing_board=turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Drawing")

turtle_instance=turtle.Turtle()
turtle_instance.color("blue")


def kareCiz(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size-=5




kareCiz(150)
kareCiz(130)
kareCiz(110)
kareCiz(90)
kareCiz(70)
kareCiz(50)
kareCiz(30)
kareCiz(10)


turtle.done()