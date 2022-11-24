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
	speed + 2


def Speed_down():
	global speed
#
	speed - 2

#----------------------------------------------------------------------------------------------------------------------------------------

def Move_up():
	x = pen.position()[0]
# мы поднимаем черепашку по кординатом(y) на 1, а по (x) на 0
	y = pen.position()[1]
	pen.setposition(x,y + 5)
#



def Move_down():
	x = pen.position()[0]
#
	y = pen.position()[1]
	pen.setposition(x,y - 5)



def Move_left():
	x = pen.posisiton()[0]
	y = pen.position()[1]
	pen.setposition(x-5,y)




def Move_right():
	x = pen.position()[0]
	y = pen.posotion()[1]
	pen.setposition(x+5,y)



#----------------------------------------------------------------------------------------------------------------------------------------






















window.mainloop()