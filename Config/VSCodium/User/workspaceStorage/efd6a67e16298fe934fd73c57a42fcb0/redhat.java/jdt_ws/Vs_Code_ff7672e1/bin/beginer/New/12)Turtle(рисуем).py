import turtle

window = turtle.Screen()
# задаём окно 

pen = turtle.Turtle()
# pen - задали карандашик
# почему turtle, потмоу что pen и есть черпешка
speed = 1

def Speed_up():
	global speed
# обьявляем speed глобальной  
	speed + 10


def Speed_down():
	global speed
#
	speed - 10

#----------------------------------------------------------------------------------------------------------------------------------------

def Move_up():
	x = pen.position()[0]
# ?мы поднимаем черепашку по кординатом(y) на 1, а по (x) на 0
	y = pen.position()[1]
	pen.setposition(x,y + 5)
#todo мы говорим pen, что ему надо двигаться на 5 кординат в право по y 


def Move_down():
	x = pen.position()[0]
	y = pen.position()[1]
	pen.setposition(x,y - 5)
#todo мы говорим pen, что ему надо двигаться на -5 кординат в право по y


def Move_left():
	x = pen.position()[0]
	y = pen.position()[1]
	pen.setposition(x-5,y)
#todo мы говорим pen, что ему надо двигаться на -5 кординат в право по x


def Move_right():
	x = pen.position()[0]
	y = pen.position()[1]
	pen.setposition(x+5,y)
#todo мы говорим pen, что ему надо двигаться на 5 кординат в право по x

#--------------------------------------------------------------------------------------------------------------------------------------------

def chenge():
	if pen.isvisible(): 
#? pen.isvisible(): используется для возрата черпахи(true) и для того чтобы его скрыть(folse)
#! если бы мы это не прописали, то при поднятии пера мы бы видили саму черепашку, т.к. мы это прописали, мы не будем видить саму черепашку(то-есть перо)
		pen.up()
		pen.hideturtle()
	else:
		pen.down()
		pen.showturtle()

#----------------------------------------------------------------------------------------------------------------------------------------

window.onkey(Move_up, "w")
window.onkey(Move_down, "s")
window.onkey(Move_left, "a")
window.onkey(Move_right, "d")
window.onkey(chenge, "space")
window.onkey(Speed_up, "Up")
window.onkey(Speed_down, "Down")
window.listen()

#----------------------------------------------------------------------------------------------------------------------------------------

window.mainloop()